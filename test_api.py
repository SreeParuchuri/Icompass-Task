import pytest
import requests
import json
import jsonpath
from requests.api import request
import api
url = 'http://127.0.0.1:5000/user'

def test_sanitized():
    file=open('v1/input/sanitizedData.json')
    
    request_json=json.load(file)
    
    response=requests.post(url,json=request_json)
    assert response.status_code==201

def test_unsanitized():
    file=open('v1/input/unsanitizedData.json')
    request_json=json.load(file)
    response=requests.post(url,json=request_json)
    assert response.status_code==200
