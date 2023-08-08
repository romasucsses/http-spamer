import requests
from bs4 import BeautifulSoup
import pickle
import time

# Load session cookies
with open('session_cookies.txt', 'rb') as session_file:
    loaded_session = pickle.load(session_file)

# Headers for requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8"
}


def extract_csrf_values(soup):
    return (
        soup.find('input', {'name': 'csrf-token'}).get('value'),
        soup.find('input', {'name': 'csrf-time'}).get('value'),
        soup.find('input', {'name': 'csrf-user'}).get('value'),
        soup.find('input', {'name': 'nonce'}).get('value'),
    )


def send_message(msg_send_to):
    link_for_request = 'https://www.wireclub.com/messages/send'
    page = loaded_session.get(link_for_request)
    soup = BeautifulSoup(page.text, 'html.parser')
    csrf_token, csrf_time, csrf_user, nonce = extract_csrf_values(soup)

    msg_title = "hello"
    msg_body = 'where are you?'

    data = {
        'csrf-token': csrf_token,
        'csrf-time': csrf_time,
        'csrf-user': csrf_user,
        'nonce': nonce,
        'Data.Recipients': msg_send_to,
        'Data.Title': msg_title,
        'Data.Body': msg_body,
        'null': 'Send Message'
    }

    send = loaded_session.post(url=link_for_request, data=data, headers=headers)


with open('users_urls.txt', 'r') as users_file:
    for line_user in users_file:
        user = line_user.strip()
        print(user)
        send_message(user)
        time.sleep(220)

