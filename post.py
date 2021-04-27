"""
Crear un recurso dentro del servidor:
Con el atributo json post se encartga de serializar los datos
Para enviar datos dentro del atributo data se deben serializar
Si se usa data=payload se pasan los parametros al atributo form
"""

import requests
import json

if __name__ == '__main__':
    url='http://httpbin.org/post'
    payload = {'nombre':'Laura', 'curso':'Python'}

    """
    response = requests.post(url, json=payload)
    response = requests.post(url, data=payload)  
    """

    response = requests.post(url, data=json.dumps(payload)) 
    print(response.url)


    if response.status_code == 200:
        print(response.content)