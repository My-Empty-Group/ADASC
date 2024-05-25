import urllib3
urllib3.disable_warnings()
import requests
from lxml import etree
username = input('Enter the username to grab...')
url = f'https://crawl.akrasiac.org/rawdata/{username}/'
req = requests.get(url = url)
while req.status_code == 404:
    print(f'The username {username} does not exist.')
    username = input('Enter the username to grab...')
    url = f'https://crawl.akrasiac.org/rawdata/{username}/'
    req = requests.get(url = url)
files = etree.HTML(req.text).xpath("//tr/td/a/@href")
tlist = []
for file in files:
    if file[-3:] == 'txt':
        tlist.append(f'{file}')
while True:
    path = input('Enter path to store...')
    if path[-1] != '/' and path[-1] != '\\':
        path += '/'
    try:
        for file in tlist:
            with open(file = f'{path}{file}', mode = 'w+', encoding = 'utf-8') as f:
                f.write(requests.get(url = f'{url}{file}').text)
        break
    except Exception as e:
        print(e)
