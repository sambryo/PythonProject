import twill, io
from twill.commands import *

debug("http","on")
#SIO = io.StringIO()
#twill.set_output(SIO)

b = get_browser()
#redirect_output("twill_out")
go("https://piazza.com")
#print(SIO.getvalue())

b.showforms()

fv("1", "email", 'nehe8v10@gmail.com')
fv("1", "password", "test123")

#save_html("twill1")
b.submit("0")
#save_html("twill2")
