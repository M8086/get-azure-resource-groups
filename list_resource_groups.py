# get a list of all resource groups in an Azure subscription
import os
import traceback

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from msrestazure.azure_exceptions import CloudError

# You will want to supply the values in this function as environment variables
def get_credentials():
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )
    return credentials, subscription_id

credentials, subscription_id = get_credentials()
client = ResourceManagementClient(credentials, subscription_id)

# gathers all resource groups and prints them to the terminal
def get_resource_groups():
    try:
        rg = client.resource_groups.list()
        while True:
            print(f"{rg.next().name}")
    except StopIteration:
        print("\nGathered all resource groups.")

if __name__ == "__main__":
    get_resource_groups()