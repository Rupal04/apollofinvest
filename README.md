**Requirements and Technologies Used**
--->Python version - 3.8.2
--->?Install boto3 using the command "pip install boto3"

Use file "conf_sample.py" and create a "conf.py" that has S3 access key, secret key, bucket name and location. 

Pass the url in input from console.

For the method that checks whether the url is valid/invalid, following cases are possible: 
    --->If valid then the method returns True
    --->If invalid then the method returns False
    --->If not a s3 url for the desired bucket, raises Exception.

For the method that fetches the meta-data of the s3 object, pass the url along with the bucket prefix and it returns the meta-data object and raises and exception otherwise.
