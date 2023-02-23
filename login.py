"""
Created on Thu Feb 23 12:45:05 2023
@author: rajiv gupta
"""

import requests, json, pyotp
from kiteconnect import KiteConnect
from urllib.parse import urlparse
from urllib.parse import parse_qs
from keys import *

def login():
    http_session = requests.Session()
    url = http_session.get(url='https://kite.trade/connect/login?v=3&api_key='+api_key).url
    response = http_session.post(url='https://kite.zerodha.com/api/login', data={'user_id':user_id, 'password':user_password})
    resp_dict = json.loads(response.content)
    http_session.post(url='https://kite.zerodha.com/api/twofa', data={'user_id':user_id, 'request_id':resp_dict["data"]["request_id"], 'twofa_value':pyotp.TOTP(totp_key).now()})
    url = url + "&skip_session=true"
    response = http_session.get(url=url, allow_redirects=True).url
    request_token = parse_qs(urlparse(response).query)['request_token'][0]

    kite = KiteConnect(api_key=api_key)
    data = kite.generate_session(request_token, api_secret=api_secret)
    kite.set_access_token(data["access_token"])

    return kite
