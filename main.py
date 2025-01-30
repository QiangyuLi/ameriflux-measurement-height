import pandas as pd

# Script to process AmeriFlux Measurement Height data
# This script reads a CSV file, filters for site 'USNE1', and saves the filtered data to a new file.

# Define file paths
input_file = "BASE_MeasurementHeight_20241204.csv"
output_file = "USNE1_MeasurementHeight.csv"

# Load the dataset
df = pd.read_csv(input_file)

# Filter the data for site 'USNE1'
usne1_df = df[df['Site_ID'] == 'USNE1']

# Save the filtered data to a new CSV file
usne1_df.to_csv(output_file, index=False)

print(f"Filtered data for site 'USNE1' saved to {output_file}")
