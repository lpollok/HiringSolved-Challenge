import re
import requests
import urllib


def crumb(crumb_url):
    
    for x in urllib.request.urlopen(crumb_url):
        next_crumb = re.findall(r'[0-9]{5}', str(x))
        return next_crumb[0]

base_url = 'https://challenge.hiringsolved.com/breadcrumbs/'
seed = '19196'
while seed != '54321':
    crumb_url = ''.join([base_url, seed])
    seed = crumb(crumb_url)
    res = requests.get(crumb_url)
    for cookie in res.cookies:
        print(cookie.value)

