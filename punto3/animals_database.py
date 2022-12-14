import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='Animals2',
    KeySchema=[
        {
            'AttributeName': 'indice',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'route',
            'KeyType': 'RANGE'  
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'indice',
            'AttributeType': 'S'  #Partition key
        },
        {
            'AttributeName': 'route',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
