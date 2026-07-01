# Private Directors — Reference Index

Read this file first. Then open only the references needed for the current phase.

## When to Read Which File

| File/Directory | Read When |
| --- | --- |
| `advisors/00-advisor-system.md` | Before calling any advisor subagent — contains universal rules and output template |
| `advisors/01-12-*.md` | When calling that specific advisor — contains mission, decision logic, must-ask questions, anti-patterns |
| `protocols/agent-orchestration.md` | When Phase 3 (advisor calls) or Phase 6 (judge call) — contains exact Agent tool call formats |
| `protocols/judge-scorecard.md` | When Phase 6 (scoring) — contains all 10 dimensions, weights, and hard-cap rules |
| `protocols/iteration-loop.md` | When Phase 7 (iteration below 95) — contains Revision Brief template and escalation rules |
| `protocols/decision-case-routing.md` | When Phase 2-3 (advisor selection + WebSearch) — contains mandatory advisors per scenario and search data requirements |
| `protocols/source-map.md` | When fact-checking or looking for domain reference resources |
| `templates/decision-brief.md` | When generating the Phase 2 Decision Brief |
| `templates/advisor-subagent-prompt.md` | When building advisor subagent prompts |
| `templates/judge-prompt.md` | When building the judge subagent prompt |
| `templates/final-report.md` | When generating the Phase 5 candidate report |
| `evals/evals.json` | When running regression or comparing against the baseline eval suite |
| `evals/test-prompts.json` | When constructing a test prompt (测试 prompt) for smoke-testing the skill |
| `evals/smoke-tests.json` | When performing quick smoke validation before a release |
| `scripts/save-session.py` | When saving a session result to decisions/results.tsv after the judge passes |

## Eval Run Modes

- **smoke**: Run `evals/smoke-tests.json` only (5 critical cases). Use before any release.
- **full_test**: Run all 3 eval files (evals.json + test-prompts.json + smoke-tests.json = 21 cases). Use for comprehensive regression.
- **baseline**: Record the score before editing for comparison.
| `examples/*.md` | When the user's scenario matches an example — use for few-shot grounding |

## Do NOT Load Everything

This skill has 30+ files. Load only what the current phase requires. Progressive disclosure keeps context lean and prevents earlier advisor outputs from contaminating later advisors.

## Read Order Per Phase

```
Phase 0-1: SKILL.md (already loaded)
Phase 2: protocols/decision-case-routing.md → templates/decision-brief.md
Phase 3: protocols/agent-orchestration.md → advisors/00-advisor-system.md → advisors/[selected].md
Phase 4: (analyze subagent outputs — no new files needed)
Phase 5: templates/final-report.md
Phase 6: protocols/judge-scorecard.md → templates/judge-prompt.md → protocols/agent-orchestration.md §5
Phase 7 (if needed): protocols/iteration-loop.md
```
