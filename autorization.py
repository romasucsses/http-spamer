import requests
from bs4 import BeautifulSoup
import pickle


def send_authenticated_request(url, username, password):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8"
    }

    login_page = requests.get(url)

    soup = BeautifulSoup(login_page.content, 'html.parser')

    csrf_token = soup.find('input', {'name': 'csrf-token'}).get('value')
    csrf_time = soup.find('input', {'name': 'csrf-time'}).get('value')
    csrf_user = soup.find('input', {'name': 'csrf-user'}).get('value')
    return_url = soup.find('input', {'name': 'returnUrl'}).get('value')

    login_data = {
        'csrf-token': csrf_token,
        'csrf-time': csrf_time,
        'csrf-user': csrf_user,
        'Username': username,
        'Password': password,
        'returnUrl': return_url,
        'inline': 'False'
    }

    # Выполнение POST-запроса для аутентификации
    session = requests.Session()
    log = session.post(url, data=login_data, headers=headers)
    print(log.status_code)
    return session


login_url = 'https://www.wireclub.com/account/doLogin'
username = 'dtngpps@gmail.com'
password = 'programtest2023'
Session = send_authenticated_request(login_url, username, password)

with open('session_cookies.txt', 'wb') as session_file:
    pickle.dump(Session, session_file)



