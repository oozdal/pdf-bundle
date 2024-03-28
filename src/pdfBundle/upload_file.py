import boto3

def upload_file_to_s3(file_path, bucket_name, object_name=None):
    """
    Download a file from an AWS S3 bucket to a local file path.

    Parameters:
        bucket_name (str): The name of the S3 bucket.
        file_path (str): The local file path of the file to upload.
        object_name (str): Optional - The key (path) of the object in the bucket. 
                           If not specified, the file name will be used.
    """

    if object_name is None:
        object_name = file_path.split('/')[-1]  # Use the file name if object_name is not provided

    try:
        resource = boto3.resource('s3')
        my_bucket = resource.Bucket(bucket_name)
        with open(file_path, 'rb') as data:
            my_bucket.upload_fileobj(data, object_name)
        print(f"File '{file_path}' uploaded successfully to S3 bucket '{bucket_name}' as '{object_name}'")
    except Exception as e:
        print(f"Error uploading file '{file_path}' to S3 bucket '{bucket_name}': {e}")


if __name__ == "__main__":
    filepath = './transformer.py'
    bucket_name = 'pdfbundle'
    
    upload_file_to_s3(filepath, bucket_name)