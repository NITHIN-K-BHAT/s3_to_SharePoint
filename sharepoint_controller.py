
# Downloading zip from files which are uploaded in the s3 bucket.
# Enter the bucket name
# Enter the zip_file_name 

import boto3
import zipfile
import os

from config import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_REGION

#name the following
bucket_name = 'Enter your bucket name '
zip_file_name = '"Enter name of zip file" .zip'

def sharepoint_controller1():
    # Initialize S3 client
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)
    print("s3 :", s3)
    
    # raise Exception("wrong")
    objects = s3.list_objects_v2(Bucket=bucket_name)['Contents']
    with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
        for obj in objects:
            file_name = obj['Key']
            print("file_name :", file_name)
            # Download file from S3
            local_file_path = os.path.basename(file_name)  
            print("local_file_path :", local_file_path)
            s3.download_file(bucket_name, file_name, local_file_path)
            # Add file to zip 
            zip_file.write(local_file_path)
            os.remove(local_file_path)
            
    

    
