
f = open('dataset.txt', 'r')
for line in f:
    print(line)
    print(type(line))
    print("----")
    print(f.read())



import boto3
s3 = boto3.resource('s3')
s3_client =boto3.client('s3')
s3_bucket_name='imobiliario'
my_bucket=s3.Bucket(s3_bucket_name)
bucket_list = {}


#iterates through the files in the bucket
my_bucket=s3.Bucket(s3_bucket_name)
bucket_list = []
#se deixar tupla nao funciona
for file in my_bucket.objects.filter(Delimiter='/', Prefix='json/'):
    print(file)
    print(file.key)
    file_name=file.key
    if file_name.find(".json")!=-1:
        bucket_list.append(file)
        print(type(bucket_list))

    print("ii")
    for arquivo in bucket_list:
        print(arquivo)
