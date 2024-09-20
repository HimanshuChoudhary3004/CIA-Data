from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment, Run, Environment

ws = Workspace.from_config(".azureml/config")

# Creating experiment
new_experiment = Experiment(ws,"CIA_dataset_experiment")


# Access the Azure ML workspace
ws = Workspace.from_config(".azureml/config")

# Create a new environment from the YAML file
from azureml.core.environment import Environment
env = Environment.get(workspace=ws, 
                      name="AzureML-ACPT-pytorch-1.13-py38-cuda11.7-gpu"
                      )


# Define the ScriptRunConfig, specifying the environment and script to run
script_run_config = ScriptRunConfig(source_directory=".",
                                    script="Dataprocessing.py",
                                    environment = env
                                    )

# Submitting script to run
new_run = new_experiment.submit(config=script_run_config)


new_run.wait_for_completion()
