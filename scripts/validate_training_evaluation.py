"""Validate all template-to-form/policy references and the bounded dynamic form vocabulary."""
import json
from pathlib import Path
from training_contract import summarize
R=Path(__file__).resolve().parents[1]
def read(path):return json.loads((R/path).read_text())
def check():
 registry=read('training/evaluation/profiles.json');policies=read('training/engagement/policies.json');profiles={p['id']:p for p in registry['profiles']};assert len(profiles)==len(registry['profiles'])==4
 known_types=set(registry['supportedFieldTypes']);counts=[0,0]
 for p in profiles.values():
  ids={f['id'] for f in p['fields']};assert len(ids)==len(p['fields'])
  for f in p['fields']:
   assert f['type'] in known_types and type(f['required']) is bool
   for k in ['visibleWhen','requiredWhen']:
    if k in f:
     c=f[k];assert c['fieldId'] in ids and set(c)-{'fieldId'} in [{'equals'},{'inValues'}]
     target=next(x for x in p['fields'] if x['id']==c['fieldId']);opts={o['value'] for o in target['options']};assert set(c.get('inValues',[c.get('equals')]))<=opts
   if f['type']=='single_select':assert len({x['value'] for x in f['options']})==len(f['options'])
   if f['type']=='repeater':assert f['minItems']==1 and f['maxItems']==100 and all(x['type']=='single_select' for x in f['fields'])
  s=p['scoring'];assert s['inputField'] in ids
  for c in s['excludeWhen']:assert c['fieldId'] in ids
  for rule in p['validationRules']:assert rule['type']=='require_value_when' and rule['fieldId'] in ids and rule['when']['fieldId'] in ids
  if s['type']=='independent_success_rate':assert s['numeratorValues']==['independent'] and s['denominatorValues']==['independent','assisted','not_yet'] and s['zeroDenominator']=='null' and s['scale']==100
  else:assert s['type'] in ['duration_summary','milestone_summary','observation_summary'] and s['score']=='null'
 assert policies['policyVersion']==3
 ranks=policies['ranks']
 assert [x['minimumTotalXp'] for x in ranks]==[0,50,150,350,700,1200]
 assert [x['order'] for x in ranks]==list(range(6)) and len({x['id'] for x in ranks})==6
 assert [x['tier'] for x in ranks]==['starter','bronze','silver','gold','platinum','diamond']
 rp=policies['rankProgression'];assert rp['schemaVersion']==1 and rp['scope']=='owner_pet' and rp['extraXpOnUpgrade']==0 and rp['includeAllPolicyVersions'] and rp['inactivityXpDeduction']==0 and rp['restOrSkippedPenalty']==0
 assert len(policies['badges'])==6 and len({b['id'] for b in policies['badges']})==6
 for b in policies['badges']:
  assert b['extraXp']==0 and b['scope']=='owner_pet' and b['awardOnce']
  assert b['rule']['type'] in ['eligible_session_count','distinct_practice_days','distinct_routine_practice_days'] and b['rule']['minimum']>0
 assert policies['badgeEvaluation']['practiceDaySource']=='reward_ledger_entries_with_positive_xp'
 assert policies['badgeEvaluation']['requiresConsecutiveDays'] is False
 ledger=read('training/schemas/reward-ledger.schema.json')
 assert set(ledger['properties']['badgeIds']['items']['enum'])=={b['id'] for b in policies['badges']}
 reward={p['id']:p for p in policies['rewards']};routines={p['id']:p for p in policies['routines']};sharing={p['id']:p for p in policies['sharing']};badges={p['id'] for p in policies['badges']}
 for r in reward.values():assert not r['performanceScoreAffectsXp'] and r['stoppedSessionPenalty']==0 and r['xpPerEligibleSession']==10 and set(r['badgeIds'])<=badges and r['cap']['maxRewardedSessionsPerRolling24Hours']==1 and r['cap']['maxRewardedSessions']==1
 for s in sharing.values():assert s['requiresExplicitUserAction'] and s['requiresPreview'] and not s['autoPost'] and not set(s['allowedFields'])&set(s['excludedFields']) and not s['claims']['allowAutomaticMasteryClaim']
 for p in (R/'training/templates').glob('*.json'):
  for t in read(p.relative_to(R))['templates']:
   counts[0]+=1;e=t['evaluation'];assert e['schemaVersion']==2 and e['scope']=='exercise_session' and e['source']=='user_reported' and e['profileRegistryPath']=='training/evaluation/profiles.json' and e['profileRegistryVersion']==registry['registryVersion']
   assert 'lessonForms' not in e and all('evaluation' not in lesson for lesson in t['lessons'])
   f=e['form'];counts[1]+=1
   assert set(f)=={'profileId','profileVersion','behaviorLabel','criteriaSource'}
   assert f['profileId'] in profiles and f['profileVersion']==profiles[f['profileId']]['version']
   assert f['behaviorLabel']==t['title'] and f['criteriaSource']=={'path':'successCriteriaPolicy'}
   if t['speciesId'] in ['fish','snake','spider','other']:assert f['profileId']=='observation_based'
   assert not e['masteryPolicy']['autoMasteryEnabled'] and e['masteryPolicy']['numericPassThreshold'] is None
   for key,lookup in [('rewards',reward),('routine',routines),('sharing',sharing)]:assert t[key]['policyPath']=='training/engagement/policies.json' and t[key]['policyVersion']==policies['policyVersion'] and t[key]['policyId'] in lookup
   assert (R/e['sessionRecordSchemaPath']).is_file()
 assert counts==[100,100];print('Validated 100 evaluation configurations, 100 exercise-session forms, four profiles and reward/routine/share policies.')
if __name__=='__main__':check()
