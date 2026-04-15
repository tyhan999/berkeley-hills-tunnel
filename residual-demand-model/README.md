# Semi-Dynamic Traffic Assignment with Residual Demand

This module implements the semi-dynamic traffic assignment simulation developed in RIMI Phase 1 ([Soga et al., 2024](https://doi.org/10.7922/G2NZ860C)). It serves as the primary transportation simulation platform for evaluating cross-hills mobility impacts under earthquake disruption and recovery scenarios.

## Overview

The model performs quasi-equilibrium traffic assignment with residual demand at sub-hourly time steps. Link travel times are held fixed within each simulation time step; routes are assigned based on shortest-path travel times, and travel times are updated between time steps as flows change. Agents that cannot complete their trips within a time step carry over as residual demand into the next period.

### Features

- Quasi-equilibrium traffic assignment with residual demand
- Efficient routing using [contraction hierarchy](https://github.com/UDST/pandana/blob/dev/examples/shortest_path_example.py) and priority-queue-based Dijkstra algorithm ([sp](https://github.com/cb-cities/sp))
- Temporal dynamics at sub-hourly time steps (15-minute intervals)
- Compatible with road networks from [OSMnx](https://github.com/gboeing/osmnx)
- Support for link closures and capacity reductions (for disruption scenarios)

## Application in This Study

The simulation evaluates how disruption of BART service through the Berkeley Hills Tunnel affects cross-hills mobility. The road network is spatially subset to the Berkeley Hills study area and simplified to representative cross-hills corridors:

- **SR 24 / Caldecott Tunnel** -- the primary regional highway facility
- **Local Berkeley Hills roadways** -- low-capacity hillside roads (e.g., Claremont Avenue, Tunnel Road)

Earthquake impacts are represented as time-dependent capacity multipliers derived from Hazus damage states and restoration functions.

## Directory Structure

```
.
├── scripts/
│   ├── residual_demand_assignment.py   # Core assignment engine
│   └── run_simulation_template.ipynb   # Template notebook for running simulations
├── mtc_od_generator/
│   ├── mtc_od_generator.ipynb          # OD demand generation from MTC data
│   ├── aggregated_demand.ipynb         # Demand aggregation pipeline
│   ├── bayarea_nodes.csv               # Bay Area network nodes
│   ├── bayarea_edges.csv               # Bay Area network edges
│   └── od.csv                          # Generated OD demand matrix
├── projects/test/
│   ├── demand_inputs/
│   │   └── od.csv                      # OD demand for the test scenario
│   ├── network_inputs/
│   │   ├── nodes.csv                   # Network node coordinates
│   │   ├── edges.csv                   # Network edge attributes
│   │   ├── updated_nodes.csv           # Processed nodes
│   │   ├── updated_edges.csv           # Processed edges with capacity
│   │   ├── closed_edges.csv            # Edges closed due to disruption
│   │   ├── tunnel.csv                  # Caldecott Tunnel edges
│   │   ├── mountain.csv                # Mountain road edges
│   │   ├── claremont.csv               # Claremont Avenue edges
│   │   └── network_prepossessor.ipynb  # Network preprocessing pipeline
│   └── simulation_outputs/
│       ├── edge_vol/                   # Link-level volume outputs per time step
│       ├── trip_info/                  # Agent-level trip records
│       └── closed_links_Tunnel.csv     # Closed links for tunnel scenario
├── plot/                               # Visualization scripts and outputs
├── images/                             # Reference images
├── environment.yml                     # Conda environment specification
└── tunnel.qgz                          # QGIS project file
```

## Input Data

| Input | Description |
|-------|-------------|
| `nodes.csv` | Node ID, x/y coordinates |
| `edges.csv` | Edge ID, start/end node, length, free-flow travel time, capacity, lanes |
| `closed_edges.csv` | List of edge IDs closed due to earthquake damage |
| `od.csv` | Origin node, destination node, departure hour, agent ID |

## Output Data

| Output | Description |
|--------|-------------|
| `edge_vol/edge_vol_hr{H}_qt{Q}_{scenario}.csv` | Link-level traffic volumes per time step |
| `trip_info/trip_info_{scenario}.csv` | Agent-level trip records (origin, destination, travel time, route) |

## Setup

```bash
conda env create -f environment.yml
conda activate residual_demand
```

### Additional Dependencies

- [pandana](https://github.com/UDST/pandana) -- network analysis for shortest paths
- [gmpy2](https://gmpy2.readthedocs.io/) -- hashing for agent tracking
- [OSMnx](https://github.com/gboeing/osmnx) -- road network extraction from OpenStreetMap

## Usage

1. Prepare network inputs using `projects/test/network_inputs/network_prepossessor.ipynb`
2. Generate OD demand using `mtc_od_generator/mtc_od_generator.ipynb`
3. Run simulations using `scripts/run_simulation_template.ipynb`

## References

- Soga, K., Comfort, L., Zhao, B., Tang, Y., & Han, T. (2024). *Assessing the functionality of transit and shared mobility systems after earthquakes* (Report No. UC ITS RIMI 4K). [https://doi.org/10.7922/G2NZ860C](https://doi.org/10.7922/G2NZ860C)
- Boeing, G. (2017). OSMnx: New methods for acquiring, constructing, analyzing, and visualizing complex street networks. *Computers, Environment and Urban Systems*, 65, 126-139.
