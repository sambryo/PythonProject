import requests
from twill.commands import *
with requests.Session() as c:
        url = "https://piazza.com"
        USERNAME = "******"
        PASSWORD = "******"
        c.get(url)
        login_data = dict(username=USERNAME,
        password=PASSWORD, next='/')
        c.post(url, data=login_data, headers={"Referer":"HOMEPAGE"})
        c.get
        page = c.get("https://piazza.com")
        go(url);
        showforms()
        print page.content