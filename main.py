import pandas as pd

# Script to process AmeriFlux Measurement Height data
# This script reads a CSV file, filters for site 'USNE1' and variables containing 'Theta', and saves the filtered data to a new file.

# Define file paths
input_file = "BASE_MeasurementHeight_20241204.csv"
output_file = "USNE1_Theta_MeasurementHeight.csv"

# Load the dataset
df = pd.read_csv(input_file)

# Filter the data for site 'USNE1' and variables containing 'Theta'
usne1_theta_df = df[(df['Site_ID'] == 'US-Ne1') & (df['Variable'].str.contains('SWC', case=False, na=False))]

# Save the filtered data to a new CSV file
usne1_theta_df.to_csv(output_file, index=False)

usne1_theta_df.head()
