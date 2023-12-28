import requests
from django.conf import settings

client_id = settings.PAYPAL_CLIENT_ID
secret_key = settings.PAYPAL_SECRET_KEY

auth_url = "https://api.sandbox.paypal.com/v1/oauth2/token"

data = {
    'grant_type': "client_credentials",
}

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en_US',
}

def get_auth_token():
    response = requests.post(url=auth_url, headers=headers, data=data, auth=(client_id, secret_key))
    print(response.json())
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        return access_token
    else:
        raise Exception    