import os
import pandas as pd
from azureml.core import Run, Workspace, Dataset

# Check if file exists
if not os.path.exists("cia.csv"):
    raise FileNotFoundError("The file 'cia.csv' does not exist in the working directory.")

# Acessign workspace and dataset
ws= Workspace.from_config(".azureml\config")

dataset = Dataset.get_by_name(ws,'cia_dataset_sdk')
df = dataset.to_pandas_dataframe()

# Handle missing values
null_df = df.isnull().sum()
data_pre_processed = df.dropna()

# Log basic info
new_run = Run.get_context()

new_run.log("shape of dataset", df.shape)

# Log missing values per column
for col in df.columns:
    new_run.log(f"{col}", null_df[col])

# Save preprocessed data to outputs directory of root folder
output_path = "outputs/cia_pre_processed_data.csv"
data_pre_processed.to_csv(output_path, index=False)

# Complete the run
new_run.complete()
