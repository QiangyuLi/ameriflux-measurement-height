# Variable Information

This document explains the structure and meaning of the provided variable names based on FLUXNET guidelines. 
For reference, see [FLUXNET Data Variables](https://fluxnet.org/data/aboutdata/data-variables/).

## Explanation of Variable Structure

Each variable follows the format `_H_V_R`, where:
- `H` is the **Horizontal Position Index**
- `V` is the **Vertical Position Index**
- `R` is the **Replicate Index** (if applicable)

Additionally, some variables contain:
- `_N`: Number of samples in spatial variability
- `_SD`: Standard deviation of spatial variability
- `_A`: Aggregated replicates
- `_#`: Aggregation per layer

## Variable Table

| Variable | H (Horizontal Index) | V (Vertical Index) | R (Replicate Index) | Explanation |
|----------|----------------------|----------------------|----------------------|-------------|
| SWC_1_1_1 | 1 | 1 | 1 | Soil water content (volumetric), range 0-100% |
| SWC_1_2_1 | 1 | 2 | 1 | Soil water content (volumetric), range 0-100% |
| SWC_1_3_1 | 1 | 3 | 1 | Soil water content (volumetric), range 0-100% |
| SWC_1_4_1 | 1 | 4 | 1 | Soil water content (volumetric), range 0-100% |
| SWC_PI_1_N | PI | 1 | N | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_1_SD | PI | 1 | SD | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_2_1_1 | 2 | 1 | 1 | Soil water content (volumetric), range 0-100% |
| SWC_2_2_1 | 2 | 2 | 1 | Soil water content (volumetric), range 0-100% |
| SWC_2_3_1 | 2 | 3 | 1 | Soil water content (volumetric), range 0-100% |
| SWC_2_4_1 | 2 | 4 | 1 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_2_N | PI | 2 | N | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_2_SD | PI | 2 | SD | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_3_1_1 | 3 | 1 | 1 | Soil water content (volumetric), range 0-100% |
| SWC_3_2_1 | 3 | 2 | 1 | Soil water content (volumetric), range 0-100% |
| SWC_3_3_1 | 3 | 3 | 1 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_3_4_1 | 3 | 4 | 1 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_3_N | PI | 3 | N | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_3_SD | PI | 3 | SD | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_4_N | PI | 4 | N | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_4_SD | PI | 4 | SD | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_1 | PI | F | 1 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_1_1_1 | PI | F | 1 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_1_2_1 | PI | F | 1 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_1_3_1 | PI | F | 1 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_1_4_1 | PI | F | 1 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_2 | PI | F | 2 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_2_1_1 | PI | F | 2 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_2_2_1 | PI | F | 2 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_2_3_1 | PI | F | 2 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_2_4_1 | PI | F | 2 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_3 | PI | F | 3 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_3_1_1 | PI | F | 3 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_3_2_1 | PI | F | 3 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_3_3_1 | PI | F | 3 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_3_4_1 | PI | F | 3 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
| SWC_PI_F_4 | PI | F | 4 | Three-index positional qualifier representing Horizontal position, Vertical position, and Replicate index. |
