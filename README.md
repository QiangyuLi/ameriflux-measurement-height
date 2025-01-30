# AmeriFlux Measurement Height Data Processing

This repository provides tools for downloading, processing, and analyzing AmeriFlux Measurement Height data. The dataset contains height/depth and instrument model information for AmeriFlux BASE data products.

## About the Dataset
Measurement Height is a temporary data product being offered while the AmeriFlux BADM infrastructure is upgraded. The downloaded CSV file contains information provided directly by site teams or from historical records.

### Data Fields:
| Field Name          | Description |
|---------------------|-------------|
| Site_ID            | Site identifier. |
| Variable           | Name of the variable in the BASE file. |
| Start_Date         | Date when the information first applies. No value means it applies from the start of the site’s full data record. |
| Height            | Distance from the ground in meters. Positive values are heights; negative values are depths. |
| Instrument_Model   | Instrument model used to collect the data variable. |
| Instrument_Model2  | A second instrument model, used for flux variables. |
| Comment           | Additional information provided by site teams. |
| BASE_Version      | The most recent AmeriFlux BASE data product version number for which the information applies. |

## Data Source
Data is sourced from AmeriFlux:
[AmeriFlux Measurement Height](https://ameriflux.lbl.gov/data/measurement-height/)

## Citation
AmeriFlux. "Measurement Height Data." Available at: [https://ameriflux.lbl.gov/data/measurement-height/](https://ameriflux.lbl.gov/data/measurement-height/)

---
### Setup Instructions:
1. Clone the repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/ameriflux-measurement-height.git
   cd ameriflux-measurement-height
   ```
2. Install dependencies (if using Python):
   ```sh
   pip install pandas requests
   ```
3. Run the script to download and process data:
   ```sh
   python scripts/process_data.py
   ```

---

### Next Steps:
- Automate data downloads via API or web scraping.
- Develop visualization tools to analyze height measurements.
- Integrate data cleaning scripts.

---

### License
This project is licensed under the MIT License.
