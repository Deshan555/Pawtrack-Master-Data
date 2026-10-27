"""Reference validation/scoring for the declarative evaluation contract, not an app backend."""
from decimal import Decimal, ROUND_HALF_UP
import math

def matches(condition, answers):
    value = answers.get(condition['fieldId'])
    if 'equals' in condition:
        return value == condition['equals']
    if 'inValues' in condition:
        return value in condition['inValues']
    raise ValueError('Unsupported condition')

def validate_answers(profile, answers):
    if not isinstance(answers, dict):
        raise ValueError('Answers must be an object')
    def validate_fields(fields, values):
        if set(values) - {f['id'] for f in fields}:
            raise ValueError('Unknown answer field')
        for field in fields:
            key = field['id']
            present = key in values
            visible = 'visibleWhen' not in field or matches(field['visibleWhen'], values)
            required = field['required'] or ('requiredWhen' in field and matches(field['requiredWhen'], values))
            if not visible:
                if present:
                    raise ValueError('Hidden answer supplied: ' + key)
                continue
            if required and not present:
                raise ValueError('Required answer: ' + key)
            if not present:
                continue
            value = values[key]
            kind = field['type']
            if kind == 'single_select':
                if value not in [o['value'] for o in field['options']]:
                    raise ValueError('Invalid option: ' + key)
            elif kind in ['text', 'textarea']:
                if not isinstance(value, str) or len(value) > field['maxLength']:
                    raise ValueError('Invalid text: ' + key)
            elif kind == 'number':
                if type(value) not in [int, float] or not math.isfinite(value) or not field['minimum'] <= value <= field['maximum']:
                    raise ValueError('Invalid number: ' + key)
            elif kind == 'repeater':
                if not isinstance(value, list) or not field['minItems'] <= len(value) <= field['maxItems']:
                    raise ValueError('Invalid row count: ' + key)
                for row in value:
                    if not isinstance(row, dict):
                        raise ValueError('Invalid row')
                    validate_fields(field['fields'], row)
            else:
                raise ValueError('Unsupported field type')
    validate_fields(profile['fields'], answers)
    for rule in profile['validationRules']:
        if rule['type'] != 'require_value_when':
            raise ValueError('Unsupported validation rule')
        if matches(rule['when'], answers) and answers.get(rule['fieldId']) != rule['equals']:
            raise ValueError('Conditional value required')

def summarize(profile, answers):
    validate_answers(profile, answers)
    scoring = profile['scoring']
    excluded = any(matches(c, answers) for c in scoring['excludeWhen'])
    result = dict(performanceScore=None, scoreIsMastery=False, excludedFromScoring=excluded)
    kind = scoring['type']
    if kind == 'independent_success_rate':
        responses = [row[scoring['responseField']] for row in answers.get(scoring['inputField'], [])]
        count = sum(r in scoring['denominatorValues'] for r in responses)
        successes = sum(r in scoring['numeratorValues'] for r in responses)
        result.update(recordedAttemptCount=count, independentAttemptCount=successes)
        if count and not excluded:
            result['performanceScore'] = int((Decimal(successes) * scoring['scale'] / count).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    elif kind in ['duration_summary', 'milestone_summary', 'observation_summary']:
        result['observedValue'] = answers.get(scoring['inputField'])
    else:
        raise ValueError('Unsupported scoring rule')
    return result
