"""
Usar la API de Spotify y obtener información de un artista.
"""

import requests
import json

if __name__ == '__main__':
    url = 'https://api.spotify.com/v1/artists/5C4PDR4LnhZTbVnKWXuDKD'
    headers = {'Content-Type': 'application/json','Authorization':'token'}

    response = requests.get(url, headers=headers) 

    if response.status_code == 200:
        print(response.headers)
        #print(response.content)

        json_response = response.json()
        name = json_response.get('name')
        genre = json_response.get('genres')
        print('Artist: {} \nMusical genres: {}'.format(name, genre))

    else:
        print(response.content)