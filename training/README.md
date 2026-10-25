# PawTrack Training Master Data

100 proposed training and husbandry templates for 12 species. **All pending expert review**. Reward-based, voluntary participation only. Fish, snake and spider entries emphasize husbandry and enrichment, not obedience. Session duration null indicates no general duration can safely be specified. Keep user progress in the local database.


## Unified template v2 structure

All 100 templates across 12 species now use template-level `schemaVersion: 2`. The catalog envelope retains `schemaVersion: 1`, matching the existing dog/cat catalogs. Common fields include `summary`, `duration`, `evidence`, `media`, `lessonEvidence`, and `successCriteriaPolicy`.

The 65 templates outside dog/cat retain their existing single lesson and instructions; schema parity does not require four lessons. Their evidence is `not_assessed`, expert review remains pending, and unverified duration bounds are null. Legacy estimatedSessionMinutes values are retained for compatibility, not promoted to verified guidance. Lesson evidence entries map to existing lesson IDs but claim no independently validated steps. Image fields are empty/null. Consumers must support variable lesson counts and missing images/duration bounds.
