# Exercise and engagement web preview

Serve the repository over HTTP. `config.json` selects the data base URL. The exercise dialog renders one evaluation v2 form per exercise, with conditional fields, actual attempt rows and descriptive summaries. No answers, sessions, pet identities or XP balances are persisted or uploaded. The XP input is a rank explorer, not an award ledger. Badges are explanatory previews.

Icons use locally bundled Lucide 0.468.0 (ISC; see vendor/LUCIDE-LICENSE), so icon rendering does not require a CDN. Dynamic content is inserted as text/DOM nodes, not interpreted markup. Fonts retain the existing Google Fonts configuration.

Rank illustrations use the JSON artwork paths. The existing manifest and data release are unchanged by UI edits. Production transaction, reward caps, ownership, routine persistence and sharing remain application responsibilities.
