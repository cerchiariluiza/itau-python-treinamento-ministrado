import boto3

def lambda_handler(event, context):
    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource('dynamodb')

    # this will search for dynamoDB table 
    # your table name may be different
    table = client.Table("nomedatable")
    print(table.table_status)

    table.put_item(Item= {'id': '34','company':  'microsoft'})