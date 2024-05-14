
#Uploading the zip file to sharepoint 
# Enter the site name (create a site in the sharepoint)
# Enter the folder name (create a the folder inside the site )

import requests
import os

from config import tenant_id,client_id,client_secret,site_id,drive_id
from sharepoint_controller import zip_file_name

# provide following name
site_name ='Enter the site_name'
folder_name = 'Enter the folder_name'

def sharepoint_service2():
    # Upload the zip file to SharePoint
    auth_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(auth_url, data=data)
    access_token = response.json()['access_token']

    upload_url = f'https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/items/root:/{site_name}/site/{folder_name}/{zip_file_name}:/content'

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/octet-stream',
        'Content-Length': str(os.path.getsize(zip_file_name))
    }
    print("headers :", headers)
    with open(zip_file_name, 'rb') as file:
        response = requests.put(upload_url, headers=headers, data=file)
        print(f"Uploaded {zip_file_name}: {response.json()}")
       
        