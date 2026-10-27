# Dynamic exercise evaluation and engagement v2

This release configures one exercise-session form for each of the 100 templates; 205 lessons remain instructional steps. It contains no application screens, user records, media uploads, social-account connection or reward service. These are product heuristics for user-reported progress, not expert-validated assessments or veterinary advice. Existing instructions, welfare criteria, review status and artwork are unchanged.

## Loading and compatibility

1. Validate the release manifest and atomically activate the complete data set.
2. Read `template.evaluation`; resolve `profileRegistryPath` against the data base URL.
3. Require evaluation schemaVersion 2 and scope `exercise_session`. Resolve `evaluation.form.(profileId, profileVersion)` in the pinned registry version. There is one form per exercise session, never one per lesson.
4. Render that profile's fields once after practice. Show `form.behaviorLabel` and exercise-level `successCriteriaPolicy`. `form.criteriaSource.path=successCriteriaPolicy` is a bounded reference to that template property, not executable code. Lessons retain their own guidance/criteria and can be practiced selectively without creating separate evaluation forms.
5. Resolve reward/routine/share references by policy path, ID and policyVersion. Pin the release dataVersion and policy/profile versions in saved records.
6. Unknown versions, field kinds, rule kinds or missing references must disable evaluation/rewards for that exercise and show a recoverable message. Existing exercise instructions can still display. Never silently switch profile or award points from an unknown policy.

Templates retain schemaVersion 2 and catalog envelopes retain schemaVersion 1; the additions are optional for existing clients that ignore unknown fields. Evaluation and session records now declare schemaVersion 2; other nested contracts retain their existing versions. This is a breaking evaluation change. Clients supporting only v1 must disable evaluation on v2 rather than fall back to lesson forms. Only exercise-session v2 records are supported by this release; no legacy v1 record schema is provided. Strict deserializers need an application update. Do not generate new lessons or replace the existing success criteria to fit a form.

## Bounded form vocabulary

`single_select` uses stable option `value` strings; display `label` text. `text` and `textarea` apply maxLength. `number` applies finite numeric min/max and optional units; booleans are not numbers. `repeater` is an ordered array of row objects using its nested `fields`.

Conditions inspect sibling answers using exactly one operator: `equals` or `inValues`. No JavaScript, eval, arbitrary expressions, downloaded code or HTML is permitted. `visibleWhen` controls rendering; hidden values must be removed from the submitted answer object. `requiredWhen` supplements `required`. Missing optional fields are omitted, not submitted as null. Unknown answer keys, invalid option values and out-of-range inputs are rejected.

`validationRules` supports `require_value_when`: if `when` matches, the target field must equal the configured value. Observed discomfort requires `session_result=stopped`; this records the user's report without diagnosing the animal. A stopped session requires a reason but can omit the exercise measurement. A completed attempt form requires at least one actual row. Do not prepopulate attempts with successes. The 100-row and 86,400-second limits are technical input bounds, not recommended practice targets or durations.

## Profiles and scoring

| Profile | Input | Result |
|---|---|---|
| attempt_based | independent / assisted / not_yet per recorded attempt | Independent responses ÷ all recorded attempts × 100, rounded half up to an integer |
| duration_based | Observed comfortable seconds | Duration summary; performanceScore=null |
| milestone_based | Furthest comfortable observation | Milestone summary; performanceScore=null |
| observation_based | User's participation observation | Observation summary; performanceScore=null |

`assisted` and `not_yet` remain in the attempt denominator. Three independent, one assisted and one not-yet response give 60, not 75. Zero attempts produce null, never zero percent. Stopped sessions and comfort values unsure/discomfort/not_observed exclude performance scoring. Preserve the descriptive record but do not turn it into a failure or mastery claim. No score automatically advances a lesson, unlocks a harder task or marks mastery.

Dog/Cat exercise forms use the main exercise measurement profile; preparation steps do not require separate observation submissions. Profiles vary by exercise. Fish, Snake, Spider and generic Other templates use observation forms throughout. Duration is an observation, not a countdown target. Existing observational progression criteria remain authoritative; the generic milestone labels do not replace them. Users may return to an easier lesson or stop at any time.

`scripts/training_contract.py` is a dependency-free reference for answer validation and summaries. It is not the production reward backend. Applications should reproduce its tested behavior and validate private records against the supplied Draft 2020-12 JSON Schemas with format checking enabled. Additional semantic checks include valid calendar dates/IANA zones, endedAt >= startedAt, pet ownership, exercise/template membership, optional practicedLessonIds membership and matching pinned exercise profile. Answers must also pass profile validation; JSON Schema alone does not resolve that dynamic relationship.

## XP and badges

`practice_xp_v1` awards 10 engagement XP for a valid completed or stopped session, independent of performance. A stopped session has no penalty. A draft, abandoned form, invalid record, skipped routine or rest day awards no XP. Never increase pet repetitions to earn XP.

Only one rewarded session per owner and pet across ALL exercises per local calendar day, and at most one in any rolling 24-hour window. Both limits apply. Persist the IANA zone and derive reward date from trusted acceptedAt, not editable historical session dates. Changing zones must not reset either cap. Offline records can synchronize, but the accepting application transaction must deduplicate and apply the caps consistently; do not mint authoritative XP on multiple devices independently.

Validate pet ownership before accepting records. Award the ledger entry, XP balance and badges in one idempotent application transaction keyed by `(ownerId, sessionId, policyId, policyVersion)`. Additionally enforce permanent award uniqueness on `(ownerId, sessionId)` across policy versions. Retrying cannot award twice. Treat scores/XP submitted by clients as untrusted and recompute. Cap rejection does not delete the session or its progress history. Existing ledger awards are not reissued after edits or policy upgrades. Editing/deleting records must not create new rewards or silently roll back historical awards.

Badges are scoped to owner+pet and awarded once: First Practice Log (first rewarded session), Steady Week (three rewarded practice days in seven calendar days), Practice Partner (10 lifetime rewarded practice days), Growing Together (30 lifetime rewarded practice days), Routine Starter (first rewarded routine practice day), and Routine Companion (seven lifetime rewarded routine practice days). Compute badge days from trusted accepted dates in the persisted zone and awarded ledger sessions. Badge awards have zero additional XP. There is no public leaderboard, missed-day deduction or streak-reset penalty.

## Routine records

Scheduling is disabled by default. The user chooses exercises, days and optional time; the catalog prescribes no universal frequency. ISO weekdays are Monday=1 to Sunday=7. Empty weekdays mean unscheduled; localTime may be null. Store timeZone as an IANA zone and handle daylight-saving transitions using the application's established scheduling policy; do not interpret localTime as UTC.

Use `routine-record.schema.json` for the plan and `routine-event.schema.json` for dated completed/rest/skipped history. Completed occurrences reference one or more persisted session IDs belonging to the same owner/pet and an exercise in the routine. Rest/skipped events have no sessions. Deduplicate occurrence events at application level; a routine event must not itself award XP again. Show completed sessions and weekly distinct practice days without punishing rest or skipped days.

## Sharing

`practice_card_v1` configures a private preview that the user explicitly shares through the platform share sheet. It never automatically posts to an account. Allow only policy-listed summary fields and user-edited captions; omit missing metrics rather than inventing scores. Pet display name, owner-selected photo/video and date must be editable or removable before sharing.

Private IDs, location, private notes, comfort answers and stopping reasons are excluded. Attach media only after explicit user selection; remove location metadata from exported media. Export only the selected card and attachments, not raw session records. Do not label a pet trained, mastered or expert-reviewed automatically. Any capture/upload, local storage permissions and social integration remain application work.

## Private record contracts

- `schemas/session-record.schema.json`: session identity, pinned release/profile versions, dates and dynamic answers.
- `schemas/routine-record.schema.json`: pet-specific opt-in schedule.
- `schemas/routine-event.schema.json`: completed/rest/skipped occurrence history.
- `schemas/reward-ledger.schema.json`: application-authoritative, immutable award entry; xpAwarded=0 can record a cap-limited eligible session without another award.

Do not commit actual user records, pet identities, balances, photos or videos to this repository.

## Verification

Run `python scripts/validate_manifest.py`, `python scripts/validate_training_evaluation.py`, and `python scripts/test_training_evaluation.py`. CI runs the same checks. Mobile rendering, persistence, ownership enforcement, XP transactions, scheduling and sharing must be implemented and tested in the application repository.

## Exercise-session integration

Select an exercise, follow any appropriate lessons, then submit one evaluation for the whole practice session. `templateId` identifies the exercise. Optional `practicedLessonIds` records context only; omit it when not needed. No lesson is required to save a session. Do not multiply forms, XP or routine events by the number of lessons. One saved session has one sessionId and one idempotent reward decision, subject to the existing cross-exercise caps. For preparation-only practice, the user may stop safely or choose an appropriate descriptive result; never fabricate attempts or measurements to satisfy a form. Existing profile validation remains mandatory.

## Badge policy version 2

Read `badgeEvaluation` and badge rules from engagement policies v2. Lifetime rules omit windowDays and use period=all_time. Count distinct localRewardDate values from positive-XP ledger entries only. Routine days additionally require a valid completed occurrence linking the same owner/pet/session and a template selected in that routine. Aggregate across routines, counting each date once; one linked exercise is practice, not completion of every planned exercise. Recheck after session acceptance and valid routine linking; late linking can grant a badge but never extra XP. Evaluate existing valid history on upgrade without reissuing XP. Persist each owner/pet/badge award once, atomically on the triggering session ledger entry; retries, multiple routines, rest/skipped days and deletion of a routine must not revoke or duplicate earned badges. Unknown rule types disable badge awards with a recoverable error. No consecutive-day requirement. Existing v1 award entries remain historical; new awards pin policyVersion 2. No badge artwork paths are published until the corresponding files exist.

## XP ranks (engagement policy version 3)

Ranks are separate from achievement badges. Read `ranks` and `rankProgression` from the pinned policy version. Thresholds are cumulative owner/pet XP: Little Explorer / Starter 0; Budding Buddy / Bronze 50; Clever Companion / Silver 150; Super Pet / Gold 350; Paw Hero / Platinum 700; Paw Legend / Diamond 1200. These are practice journey labels, not assessments of intelligence, obedience, health or mastery. There is no leaderboard or bonus XP on rank upgrade.

Sum persisted ledger xpAwarded across policy versions for the same owner/pet, deduplicated by ownerId/sessionId. Do not sum client balances, count sessions as XP, reissue awards on restore, or deduct XP for inactivity/rest/skips or deleting session display records. Keep immutable reward history. Apply existing cross-exercise award caps. Recompute after accepted awards, restore and policy activation. Select the greatest threshold <= total XP. Next rank is the next ordered entry; XP remaining is max(0,next threshold-total XP). Tier progress is (total-current threshold)/(next threshold-current threshold), clamped to [0,1]. At maximum rank nextRank=null, remainingXp=0 and progress=1. Formula strings document fixed semantics; never eval downloaded strings. For example, 420 XP is Super Pet (Gold), 280 XP remaining and tier progress 0.2. Display cumulative total separately from tier progress. Unknown progression versions disable rank display with a recoverable error. Rank artwork is available through ranks[].artwork: resolve its repository-relative path against the same release base URL, verify bytes and SHA-256 before caching, and render with contain fit. Each 512px transparent WebP is below 200,000 bytes. Use rank ID for mapping, never array position or filename guessing.
