# s3_to_SharePoint
After uploading all the files to the s3 bucket, the files are zipped and then uploaded to SharePoint.

**Steps to create the App in Azure for SharePoint access**

**Step 1 :**   First Register your application in  
              
               https://portal.azure.com 

**Step 2 :**   In the portal

               In the “Azure portal” --> “App Registrations” 
               
               Then go to New registration 
               
**Step  3:**   Enter the Name for the application    

               For example : “Europa_Sharepoint”  --> Select “Single tenant” --> Register 
      
               You will be Redirected to following page where all the credentials will be mentioned 
               
**Step  4:**  Generating the Client Secret 

               Go to “Certificates & Secrets”  --> “New Client Secret” --> Give “Description” -->then “Add” 
               
               It will generate Client Secret ( Remember to save the Client Secret once generated because you will not be able to view once you navigate away )	 
               
**Step  5:**  Generating API Permissions 

               Go to  “API Permissions”  we will have following permission  
               
               Now we have to add the permission 
              
               Go to “Add a permission” --> “Microsoft Graph” -->“Delegated permissions” --> Search for “Users” -->  Select “Sites.ReadWrite.All” --> then  “Add the permission” 

               Again go to  “Add a permission” --> “Microsoft Graph” --> “Applications permissions”    --> Search for “Sites” -->  Select “Sites.ReadWrite.All” --> then  “Add the permission” 
               
               Again go to  “Add a permission” --> Select “SharePoint” --> Click  “Application” --> Search for “Sites” -->  Select “Sites.ReadWrite.All” -->then “Add the permission”
               
               After adding all the Permissions --> “Grant the Permission” 

**In python file**

               In config.py file enter all your credentials
               
               In sharepoint_service.py file enter site_name and folder_name
               
               In sharepoint_controller.py file enter bucket_name and zip_file_name
