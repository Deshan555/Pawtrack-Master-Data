# Dog Sit hand-drawn pilot

## Generation
Five separate built-in ChatGPT image-generation calls, no paid external API, no composite extraction or cropping. User reference guided the hand-drawn 2D golden retriever style: pale golden fills, pink collar, thin brown outlines, soft pencil texture and pastel sage/lavender surroundings. No embedded text or watermarks.

Prompt set: cover — relaxed natural full-body sit on genuine transparency; lesson 01 — relaxed standing dog, quiet nonslip rug and seated trainer holding a reward; lesson 02 — voluntary sit with reward offered at mouth height; lesson 03 — familiar-room sit during quiet cue/reward practice; lesson 04 — comfortable rewarded sit in a quiet fenced garden. All prompts requested accurate anatomy, full dog within margins, no restraint or pressure, one scene per image.

## Validation
- All five files decode successfully and are strictly under 500,000 bytes (decimal KB).
- Cover: 768 x 768 RGBA PNG, original alpha preserved through proportional resize, alpha minimum 0 / maximum 255. No background removal approximation used.
- Lessons: 1536 x 1024 WebP, quality 95, method 6; lossy encoding, visually inspected for readable outlines and actions. Originals retained outside the repo.
- Generated images visually reviewed: no obvious extra limbs or unsafe handling observed; full paws and tail within frame. Cartoons simplify anatomy and are not expert-validated instructional diagrams.
- Core dog appearance and palette are consistent. Minor variation remains in trainer hair and the small collar tag in lesson 01.
- Still images cannot establish whether a sit was spontaneous, cue timing, repeated reliability, or that practice happened on a different day. Existing lesson text provides that context.
- Existing dog_sit lesson/evidence metadata and all other dog templates preserved.
- Image references, dimensions, per-asset bytes and SHA-256 stored in dog asset index; changed JSON manifest checksums updated. Full manifest validation passes.

## Integration
Consumers should resolve media.cover.rasterPath and media.lessons[].rasterPath against the repository base URL and render PNG/WebP. No SVG fallback exists. Other templates retain empty media states. No Flutter application source is present in this repository, so device rendering has not been tested. This is a research/pilot branch; root release metadata is unchanged and nothing is merged into master.
