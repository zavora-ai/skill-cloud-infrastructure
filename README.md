# Cloud Infrastructure Skill

> Cloud operations for AI agents — deploy services, scale replicas, manage DNS, rotate secrets, promote between environments, monitor costs, and rollback on failure.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--infrastructure-green)](https://github.com/zavora-ai/mcp-infrastructure)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates 29 cloud infrastructure tools into **safe deployment workflows** — verify after every change, staging before production, rollback always ready.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Deploy | 3-4 | Deploy → verify logs → check resources |
| Scale | 2-3 | Check resources → check costs → scale |
| Rollback | 2 | Revert → verify healthy |
| DNS | 2 | List → set/update record |
| Secrets | 2-3 | Set/rotate → restart service |
| Promotion | 3 | Verify staging → promote → verify prod |
| Costs | 1 | Breakdown by service and environment |

### Without this skill:
- Deploys without post-deploy verification
- Scaling without checking cost impact
- Secrets rotated without restarting services
- Production deployed without staging test
- No rollback plan when things break

### With this skill:
- Every deploy verified with logs + resources
- Cost checked before scaling decisions
- Services restarted after secret rotation
- Staging always verified before production
- Rollback in 1 call with health verification

## Installation

```bash
git clone https://github.com/zavora-ai/skill-cloud-infrastructure.git \
  ~/.skills/skills/cloud-infrastructure
```

## Requirements

**Required:** `mcp-infrastructure` (29 tools)

**Cross-MCP:**
- `mcp-observability` — monitor after deploys, trigger rollback on errors
- `mcp-cicd` — CI verification before deploy
- `mcp-credentials-vault` — secret rotation coordination
- `mcp-slack` — deploy notifications

## Folder Structure

```
cloud-infrastructure/
├── SKILL.md                       # 168 lines — 7 workflows + safety rules
├── scripts/
│   └── validate.py                # Deploy readiness checker
├── references/
│   ├── tool-sequences.md          # 29 tools across 6 categories
│   ├── cross-mcp-workflows.md     # Infra + Obs + CI/CD + Credentials
│   └── examples.md                # Deploy, costs, scale
├── README.md
└── LICENSE
```

## Example

**User:** "Deploy the new API version"

**Agent behavior:**
1. Checks current state (version, health)
2. Deploys new image
3. Verifies logs (no errors)
4. Checks resources (normal)

**Result:**
```
✅ Deployed api v2.3.1 (was v2.3.0)
3 replicas healthy. No errors in logs.
Rollback available: rollback(service: "api") → v2.3.0
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Deploy safety | Verify health after every deploy |
| Rollback speed | Revert in 1 tool call |
| Cost awareness | Check costs before scaling |
| Staging gate | Never skip staging verification |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
