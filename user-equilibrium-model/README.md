# User Equilibrium Traffic Assignment Model

This module implements a user equilibrium (UE) traffic assignment model solved via the Frank-Wolfe algorithm. In this study, user equilibrium is applied as a comparative modeling layer to evaluate how route-assignment assumptions affect estimated recovery-stage travel-time impacts in the Berkeley Hills corridor.

## Overview

User equilibrium is defined by Wardrop's first principle: at equilibrium, no traveler can reduce travel time by unilaterally changing routes given the prevailing congestion pattern (Wardrop, 1952). The model solves the equivalent convex optimization formulation using the Frank-Wolfe algorithm.

For the mathematical formulation and proof, see [User-Equilibrium-Solution.pdf](static/user-equilibrium-solution.pdf).

### Why User Equilibrium?

The quasi-equilibrium assignment in the [residual demand model](../residual-demand-model/) updates link travel times at 15-minute intervals and treats conditions as piecewise constant within each interval. In the simplified cross-hills network with few viable alternatives, this can produce oscillatory loading patterns that may understate the stabilized travel-time penalty.

The user-equilibrium model solves for a stabilized congestion pattern where flow is spread across all feasible routes until used alternatives have comparable travel times. This provides a behavioral benchmark for self-optimizing route choice under congestion.

### Key Comparison Results

| Scenario | Quasi-Equilibrium | User Equilibrium |
|----------|:-----------------:|:----------------:|
| Baseline (100% demand) | 11.1 min | 15.6 min |
| 654-yr return period (25% demand) | 18.2 min | 24.1 min |

The user equilibrium produces higher travel times but requires more computation (13.7s vs 1.1s).

## Network Configuration

The model is configured for the simplified Berkeley Hills cross-hills network with:

- **Node 0**: Origin (east side of hills)
- **Nodes 8, 9, 10**: Destinations (west side of hills)
- Key corridors represented: SR 24 / Caldecott Tunnel, Claremont Avenue, Fish Ranch Road, and other local hillside roads

Link performance follows the BPR (Bureau of Public Roads) function:

```
t(v) = t_free * (1 + alpha * (v / capacity)^beta)
```

where `alpha = 0.15` and `beta = 4` by default.

## File Structure

```
.
├── main.py         # Entry point: loads data, solves UE, prints report
├── model.py        # TrafficFlowModel class with Frank-Wolfe solver
├── graph.py        # Graph representation and path enumeration
├── data.py         # Network data for the Berkeley Hills case study
├── static/
│   ├── NETWORK.png                    # Network topology diagram
│   └── user-equilibrium-solution.pdf  # Mathematical formulation
├── run_model.ipynb # Jupyter notebook for interactive use
└── LICENSE
```

## Usage

```bash
python main.py
```

This will:
1. Load the network data from `data.py`
2. Solve the user equilibrium assignment using the Frank-Wolfe algorithm
3. Print a report of link flows, travel times, and volume-to-capacity ratios

### Customization

Modify `data.py` to change network topology, capacities, free-flow times, OD pairs, or demand levels. The `params.py` in the [UQ module](../user-equilibrium-uq/) shows how capacity parameters can be externalized for scenario analysis.

## Dependencies

- Python 3.x
- NumPy

## References

- Wardrop, J. G. (1952). Some theoretical aspects of road traffic research. *Proceedings of the Institution of Civil Engineers*, Part II, 1(3), 325-378.
- Sheffi, Y. (1985). *Urban Transportation Networks: Equilibrium Analysis with Mathematical Programming Methods*. Prentice Hall.
