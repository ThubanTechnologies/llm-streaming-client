import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.file_manager_client.client import FileManagerClient
from src.file_manager_client.config import config

def main():
    # Initialize the client
    client = FileManagerClient(base_url=config.BASE_URL, timeout=30)

    try:
        examples_directory = os.path.dirname(__file__)
        
        # 1. Upload a file
        print("1. Uploading file...")
        create_file_name = "example.txt"
        create_file_dir = os.path.join(examples_directory, create_file_name)
        
        result = client.upload_file(
            bucket_id="my-bucket",
            directory="documents",
            file=create_file_dir
        )
        
        print(f"File uploaded: {result}")

        # 2. Get a file
        print("\n2. Getting file...")
        file_response = client.get_file(
            bucket_id="my-bucket",
            file_path="documents/example.txt"
        )
        print(f"File content: {file_response.content}")

        # 3. Update a file
        print("\n3. Updating file...")
        update_file_name = "updated_example.txt"
        update_file_dir = os.path.join(examples_directory, update_file_name)
        
        result = client.update_file(
            bucket_id="my-bucket",
            directory="documents/example.txt",
            file=update_file_dir
        )
        
        print(f"File updated: {result}")

        # 4. List files
        print("\n4. Listing files...")
        structure = client.list_files(
            bucket_id="my-bucket",
            extensions=["txt"]
        )
        print(f"Files: {structure}")

        # 5. Delete a file
        print("\n5. Deleting file...")
        if client.delete_file(
            bucket_id="my-bucket",
            file_path="documents/example.txt"
        ):
            print("File successfully deleted")

    except Exception as e:
        print(f"Error handling files: {e}")

if __name__ == "__main__":
    main()