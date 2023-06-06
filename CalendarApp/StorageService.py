from google.cloud import storage
# Authenticate ourselves using the service account private key
path_to_private_key = 'calendarapp-388309-71213f772994.json'
client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)

my_path = "C:/Users/Andrii Skosyr/Documents/Zoom/2023-06-05 20.30.52 Андрій Скосир's Zoom Meeting/audio1897025678.wav"
def store_files(path):
    bucket = storage.Bucket(client, 'diploma-bucket')
    # Name of the file on the GCS once uploaded
    blob = bucket.blob(path)
    # Path of the local file
    blob.upload_from_filename(path)
store_files(my_path)
print("done")