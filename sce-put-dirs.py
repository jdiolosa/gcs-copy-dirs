# requires pip install google-cloud-storage
from google.cloud import storage
gcs_client = storage.Client(project='project')
bucket = gcs_client.get_bucket('bucket')
for x in range(100, 143):
    blob = bucket.blob(str(x) + '/archive/')
    blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')
    blob = bucket.blob(str(x) + '/errors/')
    blob.upload_from_string('', content_type='application/x-www-form-urlencoded;charset=UTF-8')
