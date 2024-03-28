import boto3

def download_file_from_s3(bucket_name, filename, local_file_path):
    """
    Download a file from an AWS S3 bucket to a local file path.

    Parameters:
        bucket_name (str): The name of the S3 bucket.
        filename (str): The filename in the bucket.
        local_file_path (str): The local file path where the downloaded file will be saved.
    """

    try:
        resource = boto3.resource('s3')
        my_bucket = resource.Bucket(bucket_name)
        my_bucket.download_file(filename, local_file_path)
        print(f"File '{filename}' downloaded successfully to '{local_file_path}'")
    except Exception as e:
        print(f"Error downloading file '{filename}' from S3 bucket '{bucket_name}': {e}")


if __name__ == "__main__":
    bucket_name = 'pdfbundle'
    filename = '2401.15050.pdf'
    local_file_path = './sample_test.pdf'
    
    download_file_from_s3(bucket_name, filename, local_file_path)
