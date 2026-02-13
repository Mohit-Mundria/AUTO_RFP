import boto3
import os

from botocore.exceptions import ClientError

S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

def download_index_from_s3(bucket_name, local_folder):
    s3 = boto3.client('s3')
    try:
        if not os.path.exists(local_folder):
            os.makedirs(local_folder)
        
        # FAISS saves as index.faiss and index.pkl
        s3.download_file(bucket_name, 'faiss_index/index.faiss', os.path.join(local_folder, 'index.faiss'))
        s3.download_file(bucket_name, 'faiss_index/index.pkl', os.path.join(local_folder, 'index.pkl'))
        print("Successfully downloaded vector index from S3.")
        return True
    except ClientError as e:
        print(f"S3 Download Error (Starting fresh if 404): {e}")
        return False
    except Exception as e:
        print(f"Unexpected error downloading from S3: {e}")
        return False

def upload_index_to_s3(bucket_name, local_folder):
    if not bucket_name:
        print("S3_BUCKET_NAME not set, skipping upload.")
        return
    s3 = boto3.client('s3')
    try:
        s3.upload_file(os.path.join(local_folder, 'index.faiss'), bucket_name, 'faiss_index/index.faiss')
        s3.upload_file(os.path.join(local_folder, 'index.pkl'), bucket_name, 'faiss_index/index.pkl')
        print("Successfully uploaded vector index to S3.")
    except Exception as e:
        print(f"Error uploading to S3: {e}")
