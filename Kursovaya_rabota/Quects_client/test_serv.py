import requests
import json

def server_request():
    #response = requests.get('https://api.github.com').content.decode("UTF8")
    #print(response.status_code)
    #json_data = json.loads(response)
    #print(json.dumps(json_data, indent=2))

    response = requests.get('https://api.github.com')
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

server_request()
