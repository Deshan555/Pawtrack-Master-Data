# PawTrack Master Data — Starter Pack

Offline-first species and breed/classification seed data for 12 PawTrack animal groups. This is a **curated starter catalog, not an exhaustive or veterinary-authoritative taxonomy**. Review classifications before production release.

## Files
- `manifest.json` — release metadata and SHA-256 checksums for the 13 data files.
- `species/species.json` — 12 species/category definitions, SVG paths, UI labels.
- `breeds/*.json` — one catalog per animal group.

## Notes
- `schemaVersion` describes the JSON contract; `dataVersion` describes content revisions.
- IDs are stable within each species: use the composite key `(speciesId, entryId)` in pet records.
- `kind=selection` values (`unknown`, `other`, `mixed`) are UI choices, **not biological taxa**.
- For bird, fish, rodent, snake, and spider, entries can denote different biological ranks or domesticated varieties. The `classificationLabel` is a user-facing convenience, not a formal taxonomic rank.
- `other.json` contains only Unknown and Other / Custom; capture a custom animal type separately.
- `breed` is optional during onboarding; do not coerce unknown to a real breed.
- Avoid silently deleting or renaming IDs already referenced by pets; mark entries inactive instead.
- Use bundled data as fallback. Download new releases to a temporary location, validate checksums and schema, then atomically activate.
- Hashes detect accidental changes relative to the manifest; they do not authenticate a compromised manifest.
- JSON files contain no user data.

## Updating
1. Edit catalog(s) while preserving existing IDs.
2. Increment `dataVersion` in the changed catalogs and manifest.
3. Regenerate `manifest.json` SHA-256 checksums and sizes.
4. Increment `schemaVersion` only for incompatible structural changes.
5. Validate and publish as a complete release.

## Version 2: search aliases

Every classification entry contains an `aliases` array of alternative names and common search terms. Entries without reliable synonyms intentionally have an empty array (`[]`); never fabricate aliases. Search the canonical `name` and `aliases`, but persist the stable `id`. This release keeps schemaVersion 1 and increases dataVersion to 2. SHA-256 hashes and byte counts in manifest.json have been regenerated. Review biological classifications before production use.
