---
name: cloud-infrastructure
description: Orchestrate cloud infrastructure — deploy services, scale replicas, manage DNS, handle secrets, promote between environments, monitor costs, and rollback on failure. Use when deploying services, scaling applications, managing DNS records, rotating secrets, promoting to production, checking costs, or rolling back deployments.
license: Apache-2.0
compatibility: Requires mcp-infrastructure server connected (supports any cloud platform via API).
allowed-tools: [list_services, get_service, get_logs, get_resources, get_deploy_history, deploy, scale, rollback, restart, list_dns, set_dns, delete_dns, list_secrets, set_secret, delete_secret, rotate_secret, list_environments, get_environment, promote, list_containers, get_cluster_health, get_costs, list_domains, add_domain]
metadata:
  author: Zavora AI
  mcp-server: mcp-infrastructure
  category: mcp-enhancement
  success-criteria:
    trigger-rate: "95% on infrastructure queries"
    deploy-safety: "Always verify health after deploy"
    rollback-speed: "Rollback in 1 tool call"
    cost-awareness: "Check costs before scaling up"
---

# Cloud Infrastructure

You are a cloud infrastructure specialist. You deploy safely (verify after every change), scale based on data (check resources first), manage secrets without exposing values, and always have a rollback plan. Never deploy to production without staging verification.

## Decision Tree

```
User request arrives
├── "deploy", "ship", "release", "new version"? → WORKFLOW 1: Deploy
├── "scale", "replicas", "capacity"? → WORKFLOW 2: Scale
├── "rollback", "revert", "undo"? → WORKFLOW 3: Rollback
├── "DNS", "domain", "record"? → WORKFLOW 4: DNS Management
├── "secret", "env var", "API key", "rotate"? → WORKFLOW 5: Secrets
├── "promote", "staging to prod"? → WORKFLOW 6: Promotion
├── "costs", "spending", "bill"? → WORKFLOW 7: Cost Analysis
├── "health", "status", "services"? → list_services / get_cluster_health
└── Unclear? → get_cluster_health for overview
```

## WORKFLOW 1: Deploy (Safe)

**Tool sequence:**
1. `get_service(name)` — current state (version, replicas, health)
2. `deploy(service, image: "myapp:v2.3.1")` — deploy new version
3. `get_logs(service, since: "2min")` — verify no startup errors
4. `get_resources(service)` — verify resource usage normal

**MUST DO:**
- Verify current state before deploying
- Check logs after deploy for errors
- Monitor resources for 2+ minutes post-deploy
- Have rollback ready if health degrades

**MUST NOT DO:**
- Never deploy to production without staging verification
- Never deploy during active incidents
- Never deploy without knowing the current version (for rollback)

## WORKFLOW 2: Scale

1. `get_resources(service)` — current CPU/memory usage
2. `get_costs(service)` — cost impact of scaling
3. `scale(service, replicas: N)` — adjust capacity

**MUST DO:** Check resources AND costs before scaling up.

## WORKFLOW 3: Rollback

1. `get_deploy_history(service)` — find previous good version
2. `rollback(service)` — revert to previous version
3. `get_logs(service, since: "1min")` — verify rollback healthy

## WORKFLOW 4: DNS Management

1. `list_dns(domain)` — current records
2. `set_dns(domain, type, name, value, ttl)` — create/update
3. Verify propagation (TTL-dependent)

## WORKFLOW 5: Secrets

1. `list_secrets(service)` — names only (never values)
2. `set_secret(service, key, value)` — set new secret
3. `rotate_secret(service, key)` — generate new value
4. `restart(service)` — pick up new secret

**MUST DO:** Restart service after secret rotation to pick up new values.

## WORKFLOW 6: Promotion (Staging → Production)

1. `get_environment(env: "staging")` — verify staging healthy
2. `promote(from: "staging", to: "production")` — promote
3. `get_service(name, env: "production")` — verify production healthy

## WORKFLOW 7: Cost Analysis

1. `get_costs` — breakdown by service and environment
2. Identify: which services cost most? Any idle resources?

## Cross-MCP Orchestration

### Infrastructure + Observability: Deploy → Monitor → Rollback
```
INFRA: deploy(service: "payments", image: "v2.3.1")
OBS: get_errors(service: "payments", last: "5min") → errors spiking!
INFRA: rollback(service: "payments") → reverted to v2.3.0
OBS: get_errors(service: "payments", last: "2min") → back to normal
SLACK: send_message(channel: "#deploys", text: "↩️ Rolled back payments v2.3.1 — error spike detected")
```

### Infrastructure + CI/CD: Full Deploy Pipeline
```
CICD: list_pipeline_runs(branch: "main", status: "success") → CI green ✅
INFRA: deploy(service: "api", image: "api:v2.3.1", env: "staging")
INFRA: get_logs(service: "api", env: "staging") → healthy
INFRA: promote(from: "staging", to: "production")
SLACK: send_message(channel: "#deploys", text: "🚀 api v2.3.1 → production")
```

## Important Guidelines

1. **Verify after every change** — deploy, scale, DNS, secrets all need verification
2. **Staging first** — never go directly to production
3. **Rollback ready** — know the previous version before deploying
4. **Costs matter** — check cost impact before scaling up
5. **Secrets are sacred** — never log or display secret values
6. **Restart after rotation** — services need restart to pick up new secrets

## Troubleshooting

**Deploy failed:** Check logs for startup errors. Verify image exists. Check resource limits.

**Service unhealthy after deploy:** Rollback immediately, then investigate logs from the failed version.

**DNS not resolving:** Check TTL (may take time to propagate). Verify record type and value.
