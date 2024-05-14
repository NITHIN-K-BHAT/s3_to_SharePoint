import sharepoint_service
import sharepoint_controller

def main():
    try: 
        sharepoint_controller.sharepoint_controller1()
        try:
            sharepoint_service.sharepoint_service2()
            print("file uploaded successfully to sharepoint")
        except :
            print("failed to run sharepoint_service2:")
    except:
        print("failed to run sharepoint_controller1:")
        
if __name__ == "__main__":
    main()