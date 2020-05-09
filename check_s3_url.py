import boto3
from http import client
from urllib.parse import urlparse
from conf import AWS_SECRET_KEY, AWS_ACCESS_KEY, S3_BUCKET, S3_LOCATION


def url_exists(url):
    _, host, path, _, _, _ = urlparse(url)
    conn = client.HTTPConnection(host)
    conn.request('HEAD', path)
    return conn.getresponse().status < 400


def meta_data_object(file_url):
    try:
        # create a connection for S3 AWS service
        s3_conn = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

        bucket_file_prefix = S3_LOCATION.format(S3_BUCKET)

        file_key_name = file_url[len(bucket_file_prefix) + 1:]

        meta_data_obj = s3_conn.head_object(
            Bucket=S3_BUCKET,
            Key=file_key_name,
        )
        return meta_data_obj

    except Exception as e:
        raise Exception("Some Exception occurred while getting the meta data of the file. Error is : {0}".format(str(e)))


if __name__ == "__main__":
    file_url = input()

    # Check whether the particular S3 url exists or not
    is_valid = url_exists(file_url)

    # if url is valid, get its meta-data object
    if is_valid:
        obj = meta_data_object(file_url)
        print(obj)
