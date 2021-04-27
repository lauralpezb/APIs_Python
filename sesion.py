import requests

if __name__ == '__main__':
    url = 'url_del_sitio_web'

    session = requests.session()
    session.auth = ('email','password')

    response = session.get(url)

    if response.ok:
        print(response.content)
    else:
        print(response.content)


