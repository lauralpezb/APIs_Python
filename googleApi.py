import requests

if __name__ == '__main__':
    url='https://www.google.com'

    #Obtener el recurso del servidor
    response = requests.get(url) 

    if response.status_code == 200:
        print(response.content) #Si la respuesta es exitosa, imprimir el contenido que envia el servidor

        #Almacenar el contenido
        content = response.content
        file = open('google.html', 'wb')
        file.write(content)
        file.close()

    

    
    

