import requests
import json

if __name__ == '__main__':
    url='http://httpbin.org/put'
    #url='http://httpbin.org/delete'
    payload = {'nombre':'Laura', 'curso':'Python'}
    headers = {'Conten-Type':'application/json', 'Access-Token':'12563'} #Enviar datos en formato json

    response = requests.put(url, data=json.dumps(payload), headers=headers) 
    #response = requests.delete(url, data=json.dumps(payload), headers=headers) 
    print(response.url)

    if response.status_code == 200:
        headers_response = response.headers
        server = headers_response['Server']
        print(server)