# George Orwell Skill

> *An analytical agent skill that equips your AI with George Orwell's mental models to deconstruct jargon, evaluate claims, and analyze text with unsparing clarity.*

[![Skill version](https://img.shields.io/badge/skill%20version-v0.1.0-0a6b5e)](SKILL.md)
[![Skill license](https://img.shields.io/badge/skill%20license-MIT-green)](LICENSE)

This skill reconstructs George Orwell's thinking frameworks and voice. It is not just a quote bot, but an analytical tool. The persona was built from over 170 sources, the majority being primary texts: the full texts of all six of his novels, three documentary books, and 35 essays, along with letters, diaries, and *Tribune* columns. To maintain an honest perspective, it deliberately incorporates critiques from his harshest critics.

## What you get

- **6 core mental models** — Each includes verified textual evidence, application guidance, and documented limitations.
- **10 decision heuristics** — Each anchored to a real historical choice, such as the POUM reversal or the BBC resignation.
- **Expression DNA** — Synthesized from ~30,000 words of essays to accurately capture his opening gambits, sentence statistics, humour rules, and verbal tics.
- **An agentic answer workflow** — The persona researches before it pronounces. It fetches the document, checks the historical record, finds the numbers, and then judges.
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
    └── sources/                 # full-text archive (local use only)
        ├── books/               #   8 books, plain text
        ├── essays/              #   31 essays
        ├── letters-diaries/     #   letters, diaries, columns
        └── INDEX.md             # provenance table + copyright notes
```

The research files tag every claim for credibility: `[PRIMARY]` (Orwell's own words, verified against a full text), `[SECONDARY]` (named critics), `[INFERRED]`, or `[EMBEDDED-UNVERIFIED]`. Contradictions between sources are recorded transparently rather than harmonized.

## License and copyright note

The agent skill is licensed under the [MIT License](LICENSE).

Orwell's works entered the public domain in life+70 countries (the UK, the EU, Australia, Canada) on 1 January 2021. US copyright still covers the books: *Animal Farm* until 2041, *Nineteen Eighty-Four* until 2045. As a result, the full-text archive under `references/sources/` is gitignored by default for local research use only. Please review `.gitignore` and `references/sources/INDEX.md` before redistributing.

The skill file itself only uses brief excerpts with clear attribution, which falls under fair use for commentary and analysis.

## Provenance

Research date: 20 July 2026. 

This skill was built using a parallel research process across Project Gutenberg Australia, orwell.ru, the Orwell Diaries project, Wikisource, telelib, Partisan Review scans, and critical texts. Quote-aggregator sites were strictly banned as sources.

## Acknowledgements

The skill was built with [Nuwa Skill](https://github.com/alchaincyf/nuwa-skill).
