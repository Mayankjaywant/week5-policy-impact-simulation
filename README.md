# Week 5 - Policy Impact Analysis and Simulation

## Project Title
**E-Governance Digital Service Efficiency: Policy Impact Simulation**

## Objective
This project demonstrates how changes in digital public-service parameters can affect public engagement and service efficiency. It uses a simple Python scenario-based simulation with synthetic data.

## Policy Issue
The selected e-governance issue is **digital service efficiency**. Citizens are more likely to use online government services when services are responsive, reliable, and easy to access.

## Scenarios
1. **Baseline** – 60-minute response time and 80% reliability.
2. **Improved Response** – response time reduced to 30 minutes.
3. **Improved Reliability** – reliability increased to 95%.
4. **Combined Improvement** – response time reduced to 30 minutes and reliability increased to 95%.

## Model Assumptions
- The simulation uses synthetic users rather than real government records.
- 1,000 simulated users are considered in each scenario.
- Faster response time increases the probability of engagement.
- Higher service reliability also increases engagement.
- Random variation is included to make the simulation more realistic.
- Results are illustrative and should not be treated as actual government statistics.

## How to Run
```bash
python policy_simulation.py
```

No external Python packages are required.

## Expected Outcome
The combined improvement scenario is expected to produce the strongest public engagement because both response time and reliability improve. The results can help policymakers compare possible interventions before allocating resources.

## Technologies
- Python
- Scenario-based simulation
- Basic probability/statistics
- Data-driven policy analysis

## Repository Structure
```text
week5-policy-impact-simulation/
├── policy_simulation.py
├── README.md
└── requirements.txt
```

## Policy Relevance
The simulation provides a simple decision-support framework for e-governance. Policymakers can modify the parameters and compare possible outcomes before implementing a digital-service change.
