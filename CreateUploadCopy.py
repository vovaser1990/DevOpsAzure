import os ,uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

local_path = "C:/Users/vovas/Desktop/Microsoft/Test1"
os.mkdir(local_path)

1 = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=vovaserstorageaccount1;AccountKey=aLDFCJ5ofGN02A3iPvrTOuQUpT5czbyc134U169yfmZqxOVLcaZapKrqfMRJe5yB4tV4FxwqywxiZqZZudslEg==;EndpointSuffix=core.windows.net")
blob_service_client2 = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=vovaserstorageaccount2;AccountKey=5fYtb3q1ZPCl+538r8wBBEE81altiOkps2fKeXcIrvS7ce2T0s9t2O5FtcFbeNW9uZtHXYSqFN1xdARtvaclug==;EndpointSuffix=core.windows.net")


container_client1 = blob_service_client1.create_container("storageaccount1container1")
container_client2 = blob_service_client2.create_container("storageaccount2container1")

container = ContainerClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=vovaserstorageaccount1;AccountKey=aLDFCJ5ofGN02A3iPvrTOuQUpT5czbyc134U169yfmZqxOVLcaZapKrqfMRJe5yB4tV4FxwqywxiZqZZudslEg==;EndpointSuffix=core.windows.net","vovatest")

for i in range(100):
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)
    cwd = os.getcwd()
    # Write text to the file
    file = open(upload_file_path, 'w')
    file.write("Hello, World!")
    file.close()
    blob_client = blob_service_client1.get_blob_client(container="storageaccount1container1", blob=local_file_name)
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

def save_blob(file_name,file_content):
    download_file_path = os.path.join(local_path+"/test2/",file_name)
    os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
    with open(download_file_path, "wb") as file:
        file.write(file_content)

blob_list = container.list_blobs()
for blob in blob_list:
    bytes = container_client1.get_blob_client(blob).download_blob().readall()
    save_blob(blob.name, bytes)

def upload_blob(file_name):
    upload_file_path = os.path.join(local_path+"/test2/",file_name)
    blob_client2 = blob_service_client2.get_blob_client(container="storageaccount2container1", blob=file_name)
    with open(upload_file_path, "rb") as data:
        blob_client2.upload_blob(data)

blob_list = container.list_blobs()
for blob in blob_list:
    upload_blob(blob.name)