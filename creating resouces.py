# IMporting asset class of azure
from azureml.core import Workspace, Datastore, Dataset

# --------------------------------------------------------------------------------------
# Creating workspace and writng config file to root directory
# --------------------------------------------------------------------------------------

ws = Workspace.create(
    name="AML-WS01",
    subscription_id="xxxxxxxxxxx-4298-8f59-xxxxxxxxxxxxx5d2",
    resource_group="AML-RG01",
    create_resource_group=True,
    location="centralindia",
)


# saving config file to root directory
ws.write_config(path=".")

# -----------------------------------------------------------------------------------------
# Creating datastore connection for CIA datset
# --------------------------------------------------------------------------------------
access_key="xxxxxxxxxxxxxxxxxxxxxxxxxx.........].................xxxxxxxxxxxxxxx"
az_cia_data_store = Datastore.register_azure_blob_container(
    workspace=ws,
    datastore_name="cia_data_data_store",
    account_name="mldatatest01",
    container_name="ml-blob-01",
    accxxxxx_keyxxx=access_key,
)


# --------------------------------------------------------------------------------------
# Creating and registerin dataset using datastore connection
# --------------------------------------------------------------------------------------

# Accessing datastore connection in variable
cia_datastore = Datastore.get(ws, "cia_data_data_store")

# path of data file in azure clound along with datastore name
csv_path = [(cia_datastore, "CIA_Country_Facts.csv")]

# creating dataset from data connection and file name
cia_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)

# Registering dataset in workspace
cia_dataset = cia_dataset.register(
    workspace=ws, name="cia_dataset_sdk", create_new_version=True
)

# -------------------------------------------------------------------------------------------------------------------------------------------------
