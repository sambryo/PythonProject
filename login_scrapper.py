import requests, webbrowser, cookielib
from lxml import html


from twill.commands import *
go("https://piazza.com")
b = get_browser()
b.showforms()

USERNAME = "**********"
PASSWORD = "**********"

LOGIN_URL = "https://piazza.com/"
load_cookies("./cookie.jar")
def main():
    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)

    payload = {
        "action": 'login',
        "username" : USERNAME,
        "password" : PASSWORD
    }


    result = session_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))
    print(result)
    save_cookies("./cookie.jar")
    r = session_requests.get('https://piazza.com/class/is2hozuzije420')
webbrowser.open_new_tab(LOGIN_URL)
if __name__ == '__main__':
    main()
