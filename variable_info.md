# Variable Description and Explanation

This document provides a detailed explanation of the variables related to soil water content (SWC) and their positional qualifiers.

## Data Source

- Citation: [FLUXNET Data Variables](https://fluxnet.org/data/aboutdata/data-variables/)
- Citation: [GitHub Repository - Open-ET/flux-data-qaqc](https://github.com/Open-ET/flux-data-qaqc/blob/b22ce2e71f75f3eba20139fcfdbf08c25e0f7107/examples/Config_options/config_for_multiple_soil_vars.ini#L145)

## Variable Explanation Table

| Variable | H (Horizontal Index) | V (Vertical Index) | R (Replicate Index) | Depth (m) | Explanation | Theta Mapping | Units |
|----------|----------------------|----------------------|----------------------|-----------|-------------|--------------|-------|
| SWC_1_1_1 | 1 | 1 | 1 | -0.10 | Soil water content at horizontal position 1, vertical position 1, replicate 1 | theta_1 | (%) |
| SWC_1_2_1 | 1 | 2 | 1 | -0.25 | Soil water content at horizontal position 1, vertical position 2, replicate 1 | theta_3 | (%) |
| SWC_1_3_1 | 1 | 3 | 1 | -0.50 | Soil water content at horizontal position 1, vertical position 3, replicate 1 | theta_9 | (%) |
| SWC_1_4_1 | 1 | 4 | 1 | -1.00 | Soil water content at horizontal position 1, vertical position 4, replicate 1 | theta_10 | (%) |
| SWC_2_1_1 | 2 | 1 | 1 | -0.10 | Soil water content at horizontal position 2, vertical position 1, replicate 1 | theta_2 | (%) |
| SWC_2_2_1 | 2 | 2 | 1 | -0.25 | Soil water content at horizontal position 2, vertical position 2, replicate 1 | theta_4 | (%) |
| SWC_2_3_1 | 2 | 3 | 1 | -0.50 | Soil water content at horizontal position 2, vertical position 3, replicate 1 | theta_13 | (%) |
| SWC_2_3_2 | 2 | 3 | 2 | -0.50 | Soil water content at horizontal position 2, vertical position 3, replicate 2 | theta_14 | (%) |
| SWC_3_1_1 | 3 | 1 | 1 | -0.10 | Soil water content at horizontal position 3, vertical position 1, replicate 1 | theta_5 | (%) |
| SWC_3_2_1 | 3 | 2 | 1 | -0.25 | Soil water content at horizontal position 3, vertical position 2, replicate 1 | theta_7 | (%) |
| SWC_4_1_1 | 4 | 1 | 1 | -0.10 | Soil water content at horizontal position 4, vertical position 1, replicate 1 | theta_6 | (%) |
| SWC_4_2_1 | 4 | 2 | 1 | -0.25 | Soil water content at horizontal position 4, vertical position 2, replicate 1 | theta_8 | (%) |

## Explanation of Qualifiers

- **H (Horizontal Position Index)**: Represents the horizontal location where the sensor is placed.
- **V (Vertical Position Index)**: Represents the vertical depth where the measurement is taken.
- **R (Replicate Index)**: Identifies multiple sensors measuring the same location to account for instrument variability.
- **Depth (m)**: Depth at which the soil water content measurement is taken.

### Example

Using the provided dataset, the following mappings apply:

- `theta_1 = SWC_1_1_1`, representing soil water content at position (1,1,1)
- `theta_2 = SWC_2_1_1`, representing soil water content at position (2,1,1)
- `theta_3 = SWC_1_2_1`, representing soil water content at position (1,2,1)

These values are measured as volumetric soil water content (%) ranging from 0-100.

---

For more details on positional qualifiers and aggregation methods, refer to the official [FLUXNET Data Variables documentation](https://fluxnet.org/data/aboutdata/data-variables/).
