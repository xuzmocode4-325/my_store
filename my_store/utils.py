import requests
from django.conf import settings
    

def get_access_token():
    url = "https://developers.cjdropshipping.com/api2.0/v1/authentication/getAccessToken"
    payload = {
        "email": settings.CJ_API_EMAIL,
        "password": settings.CJ_API_PASSWORD
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
       
    if response.status_code == 200 and response.json().get('result'):
        data = response.json().get('data')
        return data['accessToken'], data['refreshToken']
    else:
        raise Exception(f"Authentication failed: {response.json().get('message')}")

def refresh_access_token(refresh_token):
    url = "https://developers.cjdropshipping.com/api2.0/v1/authentication/refreshAccessToken"
    payload = {
        "refreshToken": refresh_token
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
       
    if response.status_code == 200 and response.json().get('result'):
        data = response.json().get('data')
        return data['accessToken'], data['refreshToken']
    else:
        raise Exception(f"Token refresh failed: {response.json().get('message')}")

def logout(access_token):
    url = "https://developers.cjdropshipping.com/api2.0/v1/authentication/logout"
    headers = {
        "CJ-Access-Token": access_token
    }
    response = requests.post(url, headers=headers)
       
    if response.status_code == 200 and response.json().get('result'):
        return True
    else:
        raise Exception(f"Logout failed: {response.json().get('message')}")

