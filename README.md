# George Orwell Skill

> *An analytical agent skill that equips your AI with George Orwell's mental models to deconstruct jargon, evaluate claims, and analyze text with unsparing clarity.*

[![Skill version](https://img.shields.io/badge/skill%20version-v0.3.0-0a6b5e)](SKILL.md)
[![Skill license](https://img.shields.io/badge/skill%20license-MIT-green)](LICENSE)

This skill reconstructs George Orwell's thinking frameworks and voice. It is not just a quote bot, but an analytical tool. The persona was built from over 170 sources, the majority being primary texts: the full texts of Orwell's six novels and three standard book-length works of nonfiction, plus essays, letters, diaries, and *Tribune* columns. That nine-work set is not a claim that these were all the books published during his lifetime. To maintain an honest perspective, it deliberately incorporates critiques from his harshest critics.

## What you get

- **6 core mental models** — Each includes verified textual evidence, application guidance, and documented limitations.
- **10 decision heuristics** — Each anchored to a real historical choice, such as the POUM reversal or the BBC resignation.
- **Expression DNA** — Synthesized from ~30,000 words of essays to accurately capture his opening gambits, sentence statistics, humour rules, and verbal tics.
- **An agentic answer workflow** — The persona researches before it pronounces. It fetches the document, checks the historical record, finds the numbers, and then judges.
- **A plain-style writing workshop** — The editing method of "Politics and the English Language", turned into a procedure: diagnose the stale phrases, rewrite in the author's own voice, verify nothing true was lost. Comes with a drop-in ruleset for reader-facing agent prose (`references/plain-style.md`).
- **A verified quotes library and misattribution blacklist** — Every quotation is string-verified against a full text. The skill also names and corrects the four most commonly circulated fake Orwell quotes.
- **Honest boundaries** — Orwell died in 1950. The skill explicitly marks any post-1950 judgments as inference and refuses to play the "Orwell would have supported X" game.

## Installation

This skill works in any skills-compatible AI agent runtime.

### Option 1: One-liner (recommended)

Use `npx skills` to download the skill into your agent's directory automatically:

```bash
npx skills add Emberwhirl/george-orwell-skill
```

Or ask your agent directly:

```text
Install this skill for me: https://github.com/Emberwhirl/george-orwell-skill
```

### Option 2: Manual clone

Clone this repository into your agent's skills folder:

```bash
git clone https://github.com/Emberwhirl/george-orwell-skill.git
```

Then point your agent at the global or project-level skill directory.

## Usage

Once installed, simply ask your agent to apply the Orwellian perspective to a document, concept, or situation:

```text
"Apply the George Orwell language audit to this press release."
```

```text
"What would the George Orwell say about this document?"
```

```text
"Rewrite this release note in plain English, Orwell's way."
```

```text
"Give me Orwell-inspired writing rules I can paste into my AGENTS.md."
```

## Repository layout

```text
.
├── SKILL.md                     # the skill itself
└── references/
    ├── research/                # six research dossiers
    │   ├── 01-writings.md       #   books & recurring themes
    │   ├── 02-conversations.md  #   letters, columns, changed minds
    │   ├── 03-expression-dna.md #   prose mechanics + quotes library
    │   ├── 04-external-views.md #   critics, controversies, biographers
    │   ├── 05-decisions.md      #   life decisions, reasoning
    │   └── 06-timeline.md       #   1903-1950 + legacy to 2026
    ├── plain-style.md           # the writing workshop: rules, swindle
    │                            #   catalogue, procedure, house ruleset
    ├── catalog.md               # works consulted + copyright notes
    └── attribution/             # secondary disputed-quote evidence
```

The research files tag every claim for credibility: `[PRIMARY]` (Orwell's own words, verified against a full text), `[SECONDARY]` (named critics), `[INFERRED]`, or `[EMBEDDED-UNVERIFIED]`. Contradictions between sources are recorded transparently rather than harmonized. What the skill was built on is listed in `references/catalog.md`.

## License and copyright note

The agent skill is licensed under the [MIT License](LICENSE).

Orwell's works entered the public domain in life+70 countries (the UK, the EU, Australia, Canada) on 1 January 2021. US copyright still covers later books: *Animal Farm* until 2041, *Nineteen Eighty-Four* until 2045. This repository does not include full texts. The skill ships brief excerpts with clear attribution, which falls under fair use for commentary and analysis. Works consulted while building the skill are listed in `references/catalog.md`.

## Provenance

Initial research date: 20 July 2026. 

This skill was built using a parallel research process across Project Gutenberg Australia, orwell.ru, the Orwell Diaries project, Wikisource, telelib, Partisan Review scans, and critical texts. Quote-aggregator sites were strictly banned as sources.

## Acknowledgements

The skill was initially built with [Nuwa Skill](https://github.com/alchaincyf/nuwa-skill).

## Changelog

### v0.3.0

Adds a **Writing Workshop** for the job the 1946 essay was written for: making someone else's prose clearer, not sounding like Orwell. The skill reads the whole text, names each stale phrase by class, rewrites in the author's register, and checks that no fact or needed qualification was lost.

- New `references/plain-style.md`: six rules and writer's questions, string-verified, with variants recorded; 1946 vices beside modern and machine-prose habits.
- A paste-in **house-style ruleset** for reader-facing agent prose; labeled as a modern adaptation, not Orwell's text.
- Triggers on Orwell-invoked plain-style edits and Orwell-inspired agent writing standards. Generic writing-improvement requests still do not.

### v0.2.0

- Inventory moved from `references/sources/INDEX.md` to `references/catalog.md`. The GitHub tree no longer describes a shipped `sources/` archive.
- `references/attribution/` holds secondary evidence for the four blacklisted misquotations (`not_found_in_checked_corpus` vs `demonstrated_misattribution`).
- `.gitignore` excludes the whole local corpus directory.
- Books: six novels and three standard book-length works of nonfiction, not "all 8 books" (*A Clergyman's Daughter* is in the set).
- Catalog: 9 books and 67 essays (was 8 and 31), including the complete *Fifty Orwell Essays* split. Frank Richards's Reply is not Orwell and is not archived.
- Deferred: *Partisan Review* London Letters and remaining *As I Please* columns. Bibliographic only: *The English People*, the 1946 Macdonald letter, the 1949 Henson statement, further diaries.
- Research dossiers (`01-writings.md`, `02-conversations.md`, `06-timeline.md`) and `SKILL.md` provenance match that inventory and those limits.
