#!/usr/bin/env python3
"""Check deployment readiness — validate service health, replicas, and resource availability."""
import json, sys

def check_readiness(data):
    services = data.get("services", [])
    target_env = data.get("target_env", "staging")

    blockers = []
    warnings = []
    for svc in services:
        healthy = svc.get("healthy_replicas", 0)
        desired = svc.get("desired_replicas", 1)
        cpu_pct = svc.get("cpu_usage_pct", 0)

        if healthy < desired:
            blockers.append(f"{svc['name']}: {healthy}/{desired} replicas healthy")
        if cpu_pct > 80:
            warnings.append(f"{svc['name']}: CPU at {cpu_pct}% — may not handle deploy surge")

    if target_env == "production" and not data.get("approval"):
        blockers.append("Production deploy requires approval")

    ready = len(blockers) == 0
    return {"ready": ready, "environment": target_env, "blockers": blockers, "warnings": warnings}

if __name__ == "__main__":
    print(json.dumps(check_readiness(json.loads(sys.argv[1])), indent=2))
