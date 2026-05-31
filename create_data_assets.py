#!/usr/bin/env python3
"""
Script to create data assets in Azure ML workspace
"""

from azure.ai.ml import MLClient
from azure.ai.ml.entities import Data
from azure.identity import DefaultAzureCredential
import os

# Configuration
subscription_id = "bdbb8a45-24e5-4c9e-ad2b-953d393a4388"
resource_group = "rg-ai300-l1c473c822c4c482c83"
workspace_name = "mlw-ai300-l1c473c822c4c482c83"

# Authenticate
credential = DefaultAzureCredential()
ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)

print(f"Connected to workspace: {workspace_name}")

# Create dev data asset
try:
    dev_data = Data(
        path="experimentation/data",
        type="uri_folder",
        name="diabetes-dev-folder",
        description="Dev training data for diabetes model"
    )
    ml_client.data.create_or_update(dev_data)
    print("✅ Created data asset: diabetes-dev-folder")
except Exception as e:
    print(f"⚠️ Error creating dev data asset: {e}")

# Create prod data asset
try:
    prod_data = Data(
        path="production/data",
        type="uri_folder",
        name="diabetes-prod-folder",
        description="Prod training data for diabetes model"
    )
    ml_client.data.create_or_update(prod_data)
    print("✅ Created data asset: diabetes-prod-folder")
except Exception as e:
    print(f"⚠️ Error creating prod data asset: {e}")

print("\nData assets created successfully!")
