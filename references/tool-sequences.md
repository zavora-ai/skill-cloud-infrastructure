# Cloud Infrastructure Tool Sequences (29 tools)

## Services (5)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_services` | All services with status | read |
| `get_service` | Details: replicas, image, URL | read |
| `get_logs` | Service logs | read |
| `get_resources` | CPU, memory, network | read |
| `get_deploy_history` | Deployment history | read |

## Deployments (4)
| Tool | Purpose | Risk |
|------|---------|------|
| `deploy` | Deploy new image/tag | **production** |
| `scale` | Scale replicas | production |
| `rollback` | Revert to previous | production |
| `restart` | Rolling restart | production |

## DNS (3)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_dns` | DNS records for domain | read |
| `set_dns` | Create/update record | production |
| `delete_dns` | Delete record | destructive |

## Secrets (4)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_secrets` | Names only (not values) | read |
| `set_secret` | Set secret/env var | write |
| `delete_secret` | Delete secret | destructive |
| `rotate_secret` | Generate new value | write |

## Environments (3)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_environments` | All envs (prod, staging, dev) | read |
| `get_environment` | Env details + services | read |
| `promote` | Staging → production | **production** |

## Platform (5)
| Tool | Purpose |
|------|---------|
| `list_containers` | Running containers/pods |
| `get_cluster_health` | Platform health overview |
| `get_costs` | Cost breakdown by service/env |
| `list_domains` | Custom domains + SSL |
| `add_domain` | Add custom domain |

## Sequence: Safe Deploy (4 calls)
```
1. get_service(name: "api") → {version: "v2.3.0", replicas: 3, healthy: true}
2. deploy(service: "api", image: "api:v2.3.1")
3. get_logs(service: "api", since: "2min") → no errors
4. get_resources(service: "api") → CPU/memory normal
```

## Sequence: Rollback (2 calls)
```
1. rollback(service: "api") → reverted to v2.3.0
2. get_logs(service: "api", since: "1min") → healthy
```
