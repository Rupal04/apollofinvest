import boto3
from http import client
from urllib.parse import urlparse
from conf import AWS_SECRET_KEY, AWS_ACCESS_KEY, S3_BUCKET, S3_LOCATION


def url_exists(file_url, bucket_file_prefix):

    # check if file_url starts with bucket file prefix
    if not file_url.startswith(bucket_file_prefix):
        raise Exception("%s not starts with %s. \nThus its not a s3 url for the desired bucket." % (file_url,
                        bucket_file_prefix))

    _, host, path, _, _, _ = urlparse(file_url)
    conn = client.HTTPConnection(host)
    conn.request('HEAD', path)
    return conn.getresponse().status < 400


def meta_data_object(file_url, bucket_file_prefix):
    try:
        # create a connection for S3 AWS service
        s3_conn = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

        file_key_name = file_url[len(bucket_file_prefix) + 1:]

        meta_data_obj = s3_conn.head_object(
            Bucket=S3_BUCKET,
            Key=file_key_name,
        )
        return meta_data_obj

    except Exception as e:
        raise Exception("Some error occurred while fetching the meta-data of the s3 object."
                        "Error is : {0}".format(str(e)))


if __name__ == "__main__":
    file_url = input()

    # Prefix having the s3 location along with s3 bucket in it.
    bucket_file_prefix = S3_LOCATION.format(S3_BUCKET)

    # Check whether the particular S3 url exists or not
    is_valid = url_exists(file_url, bucket_file_prefix)

    # if url is valid, get its meta-data object
    if is_valid:
        print("This is a valid url.")
        obj = meta_data_object(file_url, bucket_file_prefix)
        print(obj)
    else:
        print("This isn't a valid url.")
