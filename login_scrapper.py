import requests, webbrowser
from lxml import html


from twill.commands import *
go("https://piazza.com")
b = get_browser()
b.showforms()

USERNAME = "*******"
PASSWORD = "*******"

LOGIN_URL = "https://piazza.com/"

def main():
    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)

    payload = {
        "username" : USERNAME,
        "password" : PASSWORD
    }

    result = session_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))

webbrowser.open_new_tab(LOGIN_URL)
if __name__ == '__main__':
    main()