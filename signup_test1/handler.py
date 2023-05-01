import json
import boto3


def hello(event, context):

    # Specify the user pool ID of the existing user pool
    user_pool_id = 'ap-south-1_5oarstmvw'

    # Create an Amazon Cognito Identity Provider client for the specified user pool
    client = boto3.client('cognito-idp', region_name='ap-south-1')

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    # Use the client to list all the users in the specified user pool
    response = client.list_users(
        UserPoolId = user_pool_id
    )

    # Process the response and print the usernames
    for user in response['Users']:
        print(user['Username'])

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "user_pool": user['Username']
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
