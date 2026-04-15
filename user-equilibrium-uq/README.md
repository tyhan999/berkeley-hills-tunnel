# Uncertainty Quantification for User Equilibrium Model

This module couples the user equilibrium traffic assignment model with uncertainty quantification (UQ) to evaluate how variability in post-earthquake operating conditions propagates to cross-hills travel-time outcomes.

## Overview

Post-earthquake mobility impacts are sensitive to uncertainty in infrastructure operability and recovery-stage conditions. This module applies forward propagation with Latin hypercube sampling (LHS) to produce a defensible range of travel-time impacts rather than a single deterministic estimate.

The UQ workflow is implemented using the [NHERI SimCenter quoFEM](https://simcenter.designsafe-ci.org/research-tools/quofem/) tool, which interfaces with the Dakota uncertainty quantification engine (McKenna et al., 2025).

## Method

### Forward Propagation with LHS

- **Sample size**: 200 realizations with a fixed random seed for reproducibility
- **Input variability**: Each uncertain factor varies within +/-20% of its scenario value
- **Uncertain inputs**:
  - Usable roadway capacity on SR 24 / Caldecott Tunnel
  - Usable capacity on local cross-hills alternatives
  - Degree of travel-demand suppression during recovery
- **Assignment method**: User equilibrium (for each realization)

### Sensitivity Analysis

Global sensitivity analysis using Sobol main-effect and total-effect indices identifies which uncertain inputs most strongly drive travel-time variability. Adjacent roadway links with similar operational roles are grouped to reduce dimensionality.

### Key Results

- Mean travel time under the tested recovery scenario: **20.2 minutes** (1,212 seconds)
- Upper tail: travel time can reach **41.5 minutes** (2,490 seconds) under unfavorable combinations
- **Caldecott Tunnel capacity** is the dominant contributor to travel-time variance

## Network Configuration

The network uses a simplified representation of the Berkeley Hills cross-hills corridors (same topology as the [UE model](../user-equilibrium-model/)), with capacity parameters externalized in `params.py` for quoFEM integration:

| Parameter | Description | Baseline Value |
|-----------|-------------|:--------------:|
| C1 | SR 24 / Caldecott main | 1800 veh/hr |
| C2 | Claremont Avenue | 450 veh/hr |
| C3 | SR 24 approach | 1800 veh/hr |
| C4-C7 | Local hillside roads | 300-450 veh/hr |
| C8 | Western arterial | 1800 veh/hr |
| D | Total cross-hills demand | 3750 veh/hr |

## File Structure

```
.
├── main.py         # Entry point (same structure as UE model)
├── model.py        # TrafficFlowModel class with Frank-Wolfe solver
├── graph.py        # Graph representation and path enumeration
├── data.py         # Network data with parameterized capacities
├── params.py       # Capacity and demand parameters (quoFEM interface)
├── Edges/          # Edge-level analysis results
│   ├── C*.csv      # Capacity scenario outputs for each edge group
│   └── C*.qmd      # Quarto visualization scripts
├── Untitled-1.ipynb          # Analysis notebook
├── Note for UQ.xlsx          # UQ configuration notes
├── edges_UQ.png              # Edge grouping visualization
├── osm_road_network.png      # OSM road network reference
├── stage1_UQ.csv             # Stage 1 UQ results
├── static/
│   ├── NETWORK.png                    # Network topology diagram
│   └── user-equilibrium-solution.pdf  # Mathematical formulation
└── LICENSE
```

## Integration with quoFEM

The module is designed to be called by quoFEM as an external analysis engine:

1. quoFEM generates LHS samples for the uncertain parameters
2. For each sample, quoFEM writes parameter values to `params.py`
3. `data.py` imports parameters from `params.py` and solves the UE assignment
4. Results are written to `results.out` for quoFEM to collect
5. quoFEM aggregates results and computes sensitivity indices

## Usage

### Standalone

```bash
python main.py
```

### With quoFEM

Configure the quoFEM forward propagation workflow to point to this directory, specifying `params.py` parameters as random variables and `results.out` as the output file.

## Dependencies

- Python 3.x
- NumPy
- [NHERI SimCenter quoFEM](https://simcenter.designsafe-ci.org/research-tools/quofem/) (for UQ workflow)

## References

- McKenna, F., Gavrilovic, S., Zsarnoczay, A., Zhong, K., & Elhaddad, W. (2025). NHERI SimCenter R2DTool (Version 1.2.0). Zenodo. [https://doi.org/10.5281/zenodo.14800304](https://doi.org/10.5281/zenodo.14800304)
- McKay, M. D., Beckman, R. J., & Conover, W. J. (1979). A comparison of three methods for selecting values of input variables in the analysis of output from a computer code. *Technometrics*, 21(2), 239-245.
