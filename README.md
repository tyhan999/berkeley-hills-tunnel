# Assessing Transportation Impacts of Berkeley Hills Tunnel Disruption Under Earthquakes

This repository contains the transportation modeling and analysis code developed for the UC ITS RIMI (Resilient and Innovative Mobility Initiative) Phase 2 project. The study presents an integrated framework that links seismic performance assessment of the BART Berkeley Hills Tunnel to transportation-system consequences during the recovery stage.

**Report:** Soga, K., Comfort, L., Zhao, B., Tang, Y., & Han, T. (2025). *Assessing Transportation Impacts of Berkeley Hills Tunnel Disruption Under Earthquakes* (Report No. UC ITS RIMI 2024-14). Institute of Transportation Studies, University of California, Berkeley.

## Overview

Earthquakes pose a major threat to the San Francisco Bay Area transportation system. The Berkeley Hills Tunnel is a critical BART asset that supports cross-hills connectivity between the inner East Bay and Contra Costa County. This project develops a transferable workflow that links fault-displacement-based tunnel performance modeling to transportation impacts and recovery-stage planning.

The framework integrates three components:

1. **Seismic performance analysis** of the Berkeley Hills Tunnel (conducted by collaborators at UCLA; see [Zengin, Bozorgnia, & Stewart, 2025](https://doi.org/10.7922/G22J697K))
2. **Seismic performance assessment of alternative cross-hill routes**, including the Caldecott Tunnel (SR 24) and local Berkeley Hills roadways, using Hazus fragility relationships and the NHERI SimCenter R2D workflow
3. **Transportation consequence analysis**, using a semi-dynamic traffic assignment simulation with residual demand, a user-equilibrium assignment model, and uncertainty quantification

## Repository Structure

```
.
├── residual-demand-model/      # Semi-dynamic traffic assignment with residual demand
├── user-equilibrium-model/     # User equilibrium traffic assignment (Frank-Wolfe)
└── user-equilibrium-uq/        # Uncertainty quantification for user equilibrium model
```

### [`residual-demand-model/`](residual-demand-model/)

Semi-dynamic traffic assignment simulation developed in RIMI Phase 1. It implements a quasi-equilibrium assignment with residual demand at sub-hourly time steps, using road networks from OpenStreetMap. This component evaluates cross-hills mobility impacts under various disruption and recovery scenarios, including BART tunnel closure, Caldecott Tunnel capacity reductions, and local road damage.

### [`user-equilibrium-model/`](user-equilibrium-model/)

User equilibrium traffic assignment model based on Wardrop's first principle, solved using the Frank-Wolfe algorithm. In this study, user equilibrium is applied as a comparative modeling layer to evaluate whether the quasi-equilibrium assignment plausibly represents route competition and detour saturation under constrained cross-hills capacity.

### [`user-equilibrium-uq/`](user-equilibrium-uq/)

Uncertainty quantification module that couples the user equilibrium model with the NHERI SimCenter quoFEM tool. It uses forward propagation with Latin hypercube sampling to evaluate how variability in key inputs (roadway capacity, demand suppression) propagates to cross-hills travel-time outcomes.

## Earthquake Scenarios

The study evaluates four fault-displacement scenarios for the Berkeley Hills Tunnel:

| Fault Displacement | Return Period | Berkeley Hills Tunnel | Caldecott Tunnel | Local Roads |
|:------------------:|:------------:|:---------------------:|:----------------:|:-----------:|
| 0.2 m              | 327 years    | 90% capacity          | 90% capacity     | 90% capacity |
| 0.5 m              | 384 years    | 50% capacity          | 25% capacity     | 90% capacity |
| 1.0 m              | 500 years    | 25% capacity          | 25% capacity     | 90% capacity |
| 1.5 m              | 654 years    | 0% (full closure)     | 0% (full closure)| 90% capacity |

## Key Findings

- Reductions in cross-hills capacity can substantially increase travel times even when travel demand is suppressed during recovery
- User-equilibrium assignment produces higher average travel times than the quasi-equilibrium approach (e.g., 24.1 min vs. 18.2 min under severe disruption), reflecting more realistic congestion balancing across routes
- Under +/-20% input variability, some combinations can approximately double the average cross-hills travel time
- Sensitivity analysis indicates that Caldecott Tunnel capacity is the dominant contributor to travel-time variability

## Related Publications

- Soga, K., Comfort, L., Zhao, B., Tang, Y., & Han, T. (2024). *Assessing the functionality of transit and shared mobility systems after earthquakes* (Report No. UC ITS RIMI 4K). Institute of Transportation Studies, University of California, Berkeley. [https://doi.org/10.7922/G2NZ860C](https://doi.org/10.7922/G2NZ860C)
- Zengin, E., Bozorgnia, Y., & Stewart, J. P. (2025). *Evaluating the seismic vulnerability and resilience of BART's Berkeley Hills Tunnel*. Institute of Transportation Studies, University of California. [https://doi.org/10.7922/G22J697K](https://doi.org/10.7922/G22J697K)

## Acknowledgments

This work was supported by the UC Institute of Transportation Studies Resilient and Innovative Mobility Initiative (RIMI). The seismic performance analysis of the Berkeley Hills Tunnel was conducted by collaborators at UCLA (Zengin, Bozorgnia, & Stewart). Stakeholder engagement included interviews with staff from BART, Caltrans, the Metropolitan Transportation Commission, the Alameda County Transportation Commission, and SPUR.

## License

See the [LICENSE](user-equilibrium-model/LICENSE) file for details.
