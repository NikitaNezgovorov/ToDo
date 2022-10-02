import requests
from requests.auth import HTTPBasicAuth

# auth = HTTPBasicAuth(username='Nick', password='1')
# response = requests.get('http://localhost:8000/api/projects/', auth=auth)
data = {"username": "Nick", "password": "1"}
response = requests.post('http://localhost:8000/api-token-auth/', data=data)

token = response.json().get('token')
response_project = requests.get('http://localhost:8000/api/projects/',
                                headers={'Authorization': f'Token {token}'})

print(response_project.json())
