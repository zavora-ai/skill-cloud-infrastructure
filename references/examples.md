# Cloud Infrastructure Examples

## Example 1: "Deploy the new API version"
```
get_service(name: "api") → {version: "v2.3.0", replicas: 3, healthy: true}
deploy(service: "api", image: "api:v2.3.1")
get_logs(service: "api", since: "2min") → "Server started on :8080"
```
Response: "✅ Deployed api v2.3.1 (was v2.3.0). 3 replicas healthy. No errors in logs."

## Example 2: "How much are we spending?"
```
get_costs() → {total: 4500, by_service: [{name: "api", cost: 1200}, {name: "db", cost: 2000}, {name: "worker", cost: 800}], by_env: [{env: "production", cost: 3500}, {env: "staging", cost: 1000}]}
```
Response: "Monthly costs: $4,500 total. DB: $2,000 (44%), API: $1,200 (27%), Worker: $800 (18%). Production: $3,500, Staging: $1,000."

## Example 3: "Scale the API to handle more traffic"
```
get_resources(service: "api") → {cpu: 82%, memory: 65%, replicas: 3}
get_costs(service: "api") → {current: 1200, per_replica: 400}
scale(service: "api", replicas: 5) → scaled
```
Response: "Scaled api: 3 → 5 replicas. CPU was 82% (high). Cost impact: +$800/month ($1,200 → $2,000)."
