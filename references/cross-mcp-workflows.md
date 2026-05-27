# Cloud Infrastructure Cross-MCP Workflows

## Infrastructure + Observability: Deploy → Monitor → Rollback
```
INFRA: deploy(service: "payments", image: "v2.3.1")
OBS: get_errors(service: "payments", last: "5min") → spike!
INFRA: rollback(service: "payments")
SLACK: send_message(channel: "#deploys", text: "↩️ Rolled back payments — error spike")
```

## Infrastructure + CI/CD: Full Pipeline
```
CICD: list_pipeline_runs(branch: "main", status: "success") → green
INFRA: deploy(service: "api", image: "v2.3.1", env: "staging")
INFRA: get_logs(service: "api", env: "staging") → healthy
INFRA: promote(from: "staging", to: "production")
```

## Infrastructure + Credentials: Secret Rotation
```
CREDENTIALS: rotate_credential(name: "db-password")
INFRA: set_secret(service: "api", key: "DB_PASSWORD", value: new_password)
INFRA: restart(service: "api") → pick up new secret
```
