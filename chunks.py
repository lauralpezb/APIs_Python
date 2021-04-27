import requests

if __name__ == '__main__':
    url = 'https://ideasparaviajar.com/wp-content/uploads/2021/01/noche.jpg'

    response = requests.get(url, stream=True) #Con stream deja la conexión abierta sin descargar el contenido
    with open('nocheEstrellada.jpg', 'wb') as file:
        #Tomar todo el contenido del servidor y descargarlo
        for chunk in response.iter_content(): 
            file.write(chunk)
    response.close()