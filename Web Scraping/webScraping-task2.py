import requests,os
try:
    res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
    print(res.text)
    playFile=open('RomeoAndJulit','wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    #raises exception if http error exists
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

