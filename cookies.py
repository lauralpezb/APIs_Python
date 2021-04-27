import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/cookies'
    cookies = {'my-cookie': 'true'}

    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        cookiess = response.cookies
        print(cookiess)

        print('El contenido es:')
        print(response.content)
