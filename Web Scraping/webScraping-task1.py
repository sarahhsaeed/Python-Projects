import webbrowser, sys, pyperclip
if len(sys.argv)>1:
    #get the address from the command line
    address=''.join(sys.argv[1:])
else :
    address=pyperclip.paste()
webbrowser.open(f'http://maps.google.com/?q={address}')
