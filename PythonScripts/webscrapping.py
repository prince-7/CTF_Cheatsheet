import requests

url = 'https://twitter.com/BigBird01558595'

s = requests.Session()

r = s.get(url)

print r.text