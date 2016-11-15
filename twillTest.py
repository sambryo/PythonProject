from twill.commands import *
go("https://piazza.com")
b = get_browser()

b.showforms()

fv("1", "email", '********')
fv("1", "password", "******")

submit('0')

