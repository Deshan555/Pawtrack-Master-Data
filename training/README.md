# PawTrack Training Master Data

100 proposed training and husbandry templates for 12 species. **All pending expert review**. Reward-based, voluntary participation only. Fish, snake and spider entries emphasize husbandry and enrichment, not obedience. Session duration null indicates no general duration can safely be specified. Keep user progress in the local database.


## Unified template v2 structure

All 100 templates across 12 species now use template-level `schemaVersion: 2`. The catalog envelope retains `schemaVersion: 1`, matching the existing dog/cat catalogs. Common fields include `summary`, `duration`, `evidence`, `media`, `lessonEvidence`, and `successCriteriaPolicy`.

The 65 templates outside dog/cat retain their existing single lesson and instructions; schema parity does not require four lessons. Their evidence is `not_assessed`, expert review remains pending, and unverified duration bounds are null. Legacy estimatedSessionMinutes values are retained for compatibility, not promoted to verified guidance. Lesson evidence entries map to existing lesson IDs but claim no independently validated steps. Media references now point to transparent PNG covers and WebP lesson artwork. Consumers must still support variable lesson counts and missing images/duration bounds.

## Dynamic evaluation and engagement (additive v1 contract)

Every template now declares `evaluation`, `rewards`, `routine`, and `sharing`. Existing template schemaVersion 2 and catalog schemaVersion 1 remain unchanged because existing fields are preserved. The new nested evaluation contract has its own schemaVersion 1. Strict clients must add support before enabling these features. Image paths and all existing training/evidence metadata are preserved.

See [EVALUATION_CONTRACT.md](EVALUATION_CONTRACT.md) for the renderer contract, formulas, reward caps, routine records, sharing and private record schemas. Load `evaluation.profileRegistryPath` and the policy paths through manifest-verified files. User records and reward balances belong in the application database, never this public repository.
