import requests

if __name__ == '__main__':
    url='http://httpbin.org/get'

    #Obtener el recurso del servidor
    response = requests.get(url) 

    if response.status_code == 200:
        content = response.content
        print(content)

    #Crear query http://httpbin.org/get?nombre=laura&curso=python
    #Estos datos se añaden en arg, usando la url

    args = {'nombre':'Laura', 'curso':'Python'}
    response = requests.get(url, params=args) 

    #Validar url
    print(response.url)
