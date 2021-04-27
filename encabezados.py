"""
Le permiten al cliente y servidor tener una comunicacion correcta
"""

import requests
import json

if __name__ == '__main__':
    url='http://httpbin.org/post'
    payload = {'nombre':'Laura', 'curso':'Python'}
    headers = {'Conten-Type':'application/json', 'Access-Token':'12563'} #Enviar datos en formato json

    response = requests.post(url, data=json.dumps(payload), headers=headers) 
    print(response.url)

    if response.status_code == 200:
        headers_response = response.headers
        print(headers_response)

        server = headers_response['Server']
        print(server)