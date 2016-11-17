#! /usr/bin/python3
#map_it.py :- Launches a map in the broswer using an address from the command line or clipboard


import webbrowser,sys
if len(sys.argv) > 1:
    #Get address from a command line.
    address = ' '.join(sys.argv[1:])
    webbrowser.open(address)




