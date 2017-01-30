from __future__ import print_function

import json
import urllib
import boto3

print('Loading function')

lam = boto3.client('lambda')

def lambda_handler(event, context):

    payload = {}
    payload['key1'] = "It's a beautiful"
    payload['key2'] = "day in the"
    payload['key3'] = "NEIGHborhood!"

    try:
        response = lam.invoke(FunctionName='hello-world',
                    InvocationType='RequestResponse',
                    Payload=json.dumps(payload))
    except Exception as e:
        print(e)
        raise e
