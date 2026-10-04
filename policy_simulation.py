"""
Week 5 - Policy Impact Analysis and Simulation
Topic: E-Governance Digital Service Efficiency

This simple simulation studies how service response time and digital
service reliability can influence public engagement and service efficiency.
It uses synthetic data and is intended for learning/demo purposes.
"""

import random
import statistics

def run_simulation(response_time_minutes, reliability_percent,
                   users=1000, seed=42):
    random.seed(seed)

    # Synthetic probability model:
    # Faster service and higher reliability increase successful engagement.
    time_factor = max(0, min(1, (60 - response_time_minutes) / 60))
    reliability_factor = reliability_percent / 100

    engagement_probability = (
        0.35
        + 0.35 * time_factor
        + 0.30 * reliability_factor
    )
    engagement_probability = max(0, min(1, engagement_probability))

    successful = sum(
        1 for _ in range(users)
        if random.random() < engagement_probability
    )

    engagement_rate = successful / users * 100
    avg_service_time = response_time_minutes * (
        1 + random.uniform(-0.05, 0.05)
    )

    return engagement_rate, avg_service_time


def compare_scenarios():
    scenarios = {
        "Baseline": {"response": 60, "reliability": 80},
        "Improved Response": {"response": 30, "reliability": 80},
        "Improved Reliability": {"response": 60, "reliability": 95},
        "Combined Improvement": {"response": 30, "reliability": 95},
    }

    print("\nWEEK 5 POLICY IMPACT SIMULATION")
    print("-" * 65)
    print(f"{'Scenario':<25}{'Engagement %':>15}{'Avg Time (min)':>20}")
    print("-" * 65)

    results = {}

    for name, values in scenarios.items():
        engagement, avg_time = run_simulation(
            values["response"], values["reliability"]
        )
        results[name] = {
            "engagement_rate": round(engagement, 2),
            "avg_service_time": round(avg_time, 2),
        }
        print(f"{name:<25}{engagement:>15.2f}{avg_time:>20.2f}")

    print("-" * 65)
    return results


if __name__ == "__main__":
    compare_scenarios()
