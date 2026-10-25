# PawTrack Training SVG Artwork — Dog & Cat

Status: **Research / visual prototype**. Not approved as technique-specific instructional imagery.

## Inventory
- Dog: 20 covers + 80 lesson illustrations (100 named SVG symbols in `dog/illustrations.svg`)
- Cat: 15 covers + 60 lesson illustrations (75 named SVG symbols in `cat/illustrations_1.svg` through `illustrations_3.svg`)
- Every template's `media.cover` and `media.lessons` points to its symbol ID and sprite path.
- Index files: `dog/index.json` and `cat/index.json`.

## Important rendering note
These are **named SVG symbols within sprite files**, not 175 standalone SVG files. A normal `SvgPicture.asset(spritePath)` will render the sprite's default `<use>` illustration, NOT the symbol selected in JSON. To render a specific illustration in Flutter, preprocess the sprite and extract the selected `<symbol id="...">` into a standalone SVG string or generate standalone assets at build time. Do not assume fragment URLs render in flutter_svg.

## Illustration rules
- 560 × 420 viewBox, rounded pastel background, outlined cartoon character, simple task prop
- Dog: soft blue; Cat: pale pink; no photo assets or third-party image licenses
- SVG is decorative and schematic, NOT a validated demonstration of veterinary procedures, animal body positioning or handling.
- Current lesson scenes use the same character and contextual prop with a lesson-number indicator; they **do not yet illustrate distinct physical actions in every step**. Those require an instructional illustration review.

## Before production
1. Extract and visually inspect all 175 named symbols.
2. Replace schematic images with behavior-specific, stage-specific diagrams where necessary.
3. Review instructional accuracy and accessibility alt text.
4. Add SVG sanitization and rendering tests in Flutter.
5. Recompute manifest SHA-256/byte counts for all changed JSON and new SVG files, then submit a PR.
