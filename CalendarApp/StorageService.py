from google.cloud import storage
# Authenticate ourselves using the service account private key
path_to_private_key = 'calendarapp-388309-71213f772994.json'
client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)


def store_files(path):
    bucket = storage.Bucket(client, 'diploma-bucket')
    # Name of the file on the GCS once uploaded
    blob = bucket.blob(path)
    # Path of the local file
    blob.upload_from_filename(path)
