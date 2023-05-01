import boto3
from botocore.exceptions import ClientError

client = boto3.client('cognito-idp', region_name='ap-south-1')

def authenticate_user(username, password):
    try:
        response = client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': 'nilesh_kumar_tiwari',
                'PASSWORD': 'Bonds@1234',
            },
            ClientId='6qnp1l7b7ao3jdam23v3hh0mmn',
        )
        return response['AuthenticationResult']['AccessToken']
    except ClientError as e:
        print(e)
        return None
