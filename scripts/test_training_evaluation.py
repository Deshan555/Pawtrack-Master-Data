import copy,json,unittest
from pathlib import Path
from training_contract import summarize,validate_answers
R=Path(__file__).resolve().parents[1]
P={p['id']:p for p in json.loads((R/'training/evaluation/profiles.json').read_text())['profiles']}
class ContractTests(unittest.TestCase):
 def test_exercise_forms_and_v2_only_session_schema(self):
  count=0
  for path in (R/'training/templates').glob('*.json'):
   for template in json.loads(path.read_text())['templates']:
    e=template['evaluation'];self.assertEqual(e['scope'],'exercise_session');self.assertNotIn('lessonForms',e)
    self.assertIn(e['form']['profileId'],P);self.assertEqual(e['form']['criteriaSource'],{'path':'successCriteriaPolicy'});count+=1
  self.assertEqual(count,100)
  current=json.loads((R/'training/schemas/session-record.schema.json').read_text())
  self.assertFalse((R/'training/schemas/session-record-v1.schema.json').exists())
  self.assertEqual(current['properties']['schemaVersion']['const'],2)
  self.assertNotIn('lessonId',current['required']);self.assertNotIn('practicedLessonIds',current['required'])
  self.assertTrue(current['properties']['practicedLessonIds']['uniqueItems'])
 def base(self):return dict(session_result='completed',comfort='comfortable')
 def test_attempt_score_denominator_and_rounding(self):
  a=self.base();a['attempts']=[dict(response=x) for x in ['independent','independent','assisted']];self.assertEqual(summarize(P['attempt_based'],a)['performanceScore'],67)
  a['attempts'].append(dict(response='not_yet'));self.assertEqual(summarize(P['attempt_based'],a)['performanceScore'],50)
 def test_stopped_zero_attempts_is_valid_and_unscored(self):
  a=dict(session_result='stopped',comfort='discomfort',stop_reason='avoidance');s=summarize(P['attempt_based'],a);self.assertIsNone(s['performanceScore']);self.assertEqual(s['recordedAttemptCount'],0)
 def test_completed_empty_attempts_rejected(self):
  for rows in [None,[]]:
   a=self.base()
   if rows is not None:a['attempts']=rows
   with self.assertRaises(ValueError):validate_answers(P['attempt_based'],a)
 def test_discomfort_requires_stopping(self):
  a=self.base();a.update(comfort='discomfort',attempts=[dict(response='independent')])
  with self.assertRaises(ValueError):validate_answers(P['attempt_based'],a)
 def test_unsure_excludes_performance(self):
  a=self.base();a.update(comfort='unsure',attempts=[dict(response='independent')]);self.assertIsNone(summarize(P['attempt_based'],a)['performanceScore'])
 def test_stop_reason_required_and_hidden_fields_rejected(self):
  with self.assertRaises(ValueError):validate_answers(P['observation_based'],dict(session_result='stopped',comfort='comfortable'))
  a=self.base();a.update(participation='no_change',stop_reason='other')
  with self.assertRaises(ValueError):validate_answers(P['observation_based'],a)
 def test_other_profiles_do_not_invent_scores(self):
  for id,field,value in [('duration_based','observed_seconds',12.5),('milestone_based','milestone','engaged'),('observation_based','participation','no_change')]:
   a=self.base();a[field]=value;s=summarize(P[id],a);self.assertIsNone(s['performanceScore']);self.assertFalse(s['scoreIsMastery'])
 def test_invalid_types_options_and_unknown_fields(self):
  for value in [True,-1,float('nan'),'12',86401]:
   a=self.base();a['observed_seconds']=value
   with self.assertRaises(ValueError):validate_answers(P['duration_based'],a)
  a=self.base();a['attempts']=[dict(response='guessed')]
  with self.assertRaises(ValueError):validate_answers(P['attempt_based'],a)
  a=self.base();a.update(participation='no_change',xp=999)
  with self.assertRaises(ValueError):validate_answers(P['observation_based'],a)
if __name__=='__main__':unittest.main()
