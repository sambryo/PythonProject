import requests
with requests.Session() as c:
        url = "https://piazza.com"
        USERNAME = "nehe8v10"
        PASSWORD = "valid password"
        c.get(url)
        login_data = dict(username=USERNAME,
        password=PASSWORD, next='/')
        c.post(url, data=login_data, headers={"Referer":"HOMEPAGE"})
        page = c.get("PROTECTED LEVEL OF WEBSITE")

        print page.content