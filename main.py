import boto3

acces_key_id = 'create one if you do not have one'
secret_access_key = 'create one if you do not have one' 

video = 'your_image.jpeg'

client = boto3.client(
    'rekognition',
    region_name='your_region', 
    aws_access_key_id=acces_key_id,
    aws_secret_access_key=secret_access_key)

response = client.recognize_celebrities(Image={'S3Object':{
    'Bucket': 'your_bucket_name',
    'Name': video
}})

print(response)
