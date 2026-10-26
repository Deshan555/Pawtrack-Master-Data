# Cat artwork validation

Final inventory: **75 images**, 15 transparent RGBA PNG covers and 60 opaque WebP lesson scenes. Largest file: **499,171 bytes**; total: **32,146,453 bytes**.

Checks: all images decode; each file is below 500,000 bytes; covers contain actual alpha transparency; dimensions, byte counts and SHA-256 match the Cat index; IDs and hashes are unique; all 15 templates reference one cover and four matching lesson images; non-media training content is unchanged; manifest validation passes. GitHub blob uploads are checked against local Git object hashes.

Visual review included cat anatomy/framing, nose targeting, untethered indoor harness practice, voluntary handling, brush/hand contact, carrier geometry and size, low perches and toy release. Replaced the undersized carrier cover, refreshed the initial four litter-box scenes for consistent styling, and clarified the toy-release lesson.

Flutter rendering has not been tested. Artwork remains illustrative; existing pending expert-review metadata is preserved.

| Asset | Bytes | Dimensions |
|---|---:|---|
| cat_litter_box_habits/cover.png | 415,381 | 640 × 640 |
| cat_litter_box_habits/lesson_01.webp | 383,860 | 1536 × 1024 |
| cat_litter_box_habits/lesson_02.webp | 437,180 | 1536 × 1024 |
| cat_litter_box_habits/lesson_03.webp | 373,570 | 1536 × 1024 |
| cat_litter_box_habits/lesson_04.webp | 432,704 | 1536 × 1024 |
| cat_scratching_post_use/cover.png | 458,221 | 576 × 576 |
| cat_scratching_post_use/lesson_01.webp | 468,940 | 1536 × 1024 |
| cat_scratching_post_use/lesson_02.webp | 423,658 | 1536 × 1024 |
| cat_scratching_post_use/lesson_03.webp | 431,166 | 1536 × 1024 |
| cat_scratching_post_use/lesson_04.webp | 468,654 | 1536 × 1024 |
| cat_name_response/cover.png | 496,547 | 640 × 640 |
| cat_name_response/lesson_01.webp | 460,910 | 1536 × 1024 |
| cat_name_response/lesson_02.webp | 377,426 | 1536 × 1024 |
| cat_name_response/lesson_03.webp | 493,758 | 1536 × 1024 |
| cat_name_response/lesson_04.webp | 468,540 | 1536 × 1024 |
| cat_come_when_called/cover.png | 474,359 | 640 × 640 |
| cat_come_when_called/lesson_01.webp | 393,314 | 1536 × 1024 |
| cat_come_when_called/lesson_02.webp | 376,174 | 1536 × 1024 |
| cat_come_when_called/lesson_03.webp | 374,970 | 1536 × 1024 |
| cat_come_when_called/lesson_04.webp | 415,556 | 1536 × 1024 |
| cat_carrier_comfort/cover.png | 426,243 | 640 × 640 |
| cat_carrier_comfort/lesson_01.webp | 319,476 | 1536 × 1024 |
| cat_carrier_comfort/lesson_02.webp | 419,100 | 1536 × 1024 |
| cat_carrier_comfort/lesson_03.webp | 350,056 | 1536 × 1024 |
| cat_carrier_comfort/lesson_04.webp | 474,170 | 1536 × 1024 |
| cat_hand_target/cover.png | 466,709 | 640 × 640 |
| cat_hand_target/lesson_01.webp | 417,668 | 1536 × 1024 |
| cat_hand_target/lesson_02.webp | 325,132 | 1536 × 1024 |
| cat_hand_target/lesson_03.webp | 319,952 | 1536 × 1024 |
| cat_hand_target/lesson_04.webp | 461,318 | 1536 × 1024 |
| cat_clicker_introduction/cover.png | 478,786 | 640 × 640 |
| cat_clicker_introduction/lesson_01.webp | 427,646 | 1536 × 1024 |
| cat_clicker_introduction/lesson_02.webp | 355,262 | 1536 × 1024 |
| cat_clicker_introduction/lesson_03.webp | 429,890 | 1536 × 1024 |
| cat_clicker_introduction/lesson_04.webp | 455,766 | 1536 × 1024 |
| cat_harness_familiarity/cover.png | 448,714 | 640 × 640 |
| cat_harness_familiarity/lesson_01.webp | 473,270 | 1536 × 1024 |
| cat_harness_familiarity/lesson_02.webp | 449,380 | 1536 × 1024 |
| cat_harness_familiarity/lesson_03.webp | 426,860 | 1536 × 1024 |
| cat_harness_familiarity/lesson_04.webp | 433,776 | 1536 × 1024 |
| cat_gentle_brushing/cover.png | 414,319 | 576 × 576 |
| cat_gentle_brushing/lesson_01.webp | 418,476 | 1536 × 1024 |
| cat_gentle_brushing/lesson_02.webp | 425,738 | 1536 × 1024 |
| cat_gentle_brushing/lesson_03.webp | 425,258 | 1536 × 1024 |
| cat_gentle_brushing/lesson_04.webp | 445,614 | 1536 × 1024 |
| cat_nail_care_cooperation/cover.png | 452,076 | 576 × 576 |
| cat_nail_care_cooperation/lesson_01.webp | 436,122 | 1536 × 1024 |
| cat_nail_care_cooperation/lesson_02.webp | 436,934 | 1536 × 1024 |
| cat_nail_care_cooperation/lesson_03.webp | 450,922 | 1536 × 1024 |
| cat_nail_care_cooperation/lesson_04.webp | 447,474 | 1536 × 1024 |
| cat_puzzle_feeder_exploration/cover.png | 498,924 | 640 × 640 |
| cat_puzzle_feeder_exploration/lesson_01.webp | 380,444 | 1536 × 1024 |
| cat_puzzle_feeder_exploration/lesson_02.webp | 391,984 | 1536 × 1024 |
| cat_puzzle_feeder_exploration/lesson_03.webp | 440,010 | 1536 × 1024 |
| cat_puzzle_feeder_exploration/lesson_04.webp | 422,926 | 1536 × 1024 |
| cat_perch_recall/cover.png | 467,926 | 640 × 640 |
| cat_perch_recall/lesson_01.webp | 437,152 | 1536 × 1024 |
| cat_perch_recall/lesson_02.webp | 387,564 | 1536 × 1024 |
| cat_perch_recall/lesson_03.webp | 406,904 | 1536 × 1024 |
| cat_perch_recall/lesson_04.webp | 373,786 | 1536 × 1024 |
| cat_station_on_mat/cover.png | 428,086 | 640 × 640 |
| cat_station_on_mat/lesson_01.webp | 443,004 | 1536 × 1024 |
| cat_station_on_mat/lesson_02.webp | 448,948 | 1536 × 1024 |
| cat_station_on_mat/lesson_03.webp | 408,500 | 1536 × 1024 |
| cat_station_on_mat/lesson_04.webp | 425,392 | 1536 × 1024 |
| cat_voluntary_vet_handling/cover.png | 495,769 | 576 × 576 |
| cat_voluntary_vet_handling/lesson_01.webp | 398,686 | 1536 × 1024 |
| cat_voluntary_vet_handling/lesson_02.webp | 437,020 | 1536 × 1024 |
| cat_voluntary_vet_handling/lesson_03.webp | 407,434 | 1536 × 1024 |
| cat_voluntary_vet_handling/lesson_04.webp | 389,124 | 1536 × 1024 |
| cat_toy_retrieval/cover.png | 499,171 | 640 × 640 |
| cat_toy_retrieval/lesson_01.webp | 436,912 | 1536 × 1024 |
| cat_toy_retrieval/lesson_02.webp | 445,788 | 1536 × 1024 |
| cat_toy_retrieval/lesson_03.webp | 493,512 | 1536 × 1024 |
| cat_toy_retrieval/lesson_04.webp | 444,492 | 1536 × 1024 |
