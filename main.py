import urllib3
urllib3.disable_warnings()
import requests
from lxml import etree
username = input('Enter the username to grab...')
req = requests.get(url = f'https://crawl.akrasiac.org/scoring/players/{username}.html')
while req.status_code == 404:
    print(f'The username {username} does not exist.')
    username = input('Enter the username to grab...')
    req = requests.get(url = f'https://crawl.akrasiac.org/scoring/players/{username}.html')
path = input('Enter path to store...')
path = path.replace('\\', '/') + ('/' if path[-1] != '/' else '')
# akrasiac
url = f'https://crawl.akrasiac.org/rawdata/{username}/'
req = requests.get(url = url)
files = etree.HTML(req.text).xpath("//tr/td/a/@href")
tlist = []
for file in files:
    if file[-4:] == '.txt' and file[:7] == 'morgue-':
        tlist.append(f'CAO-{file}')
try:
    for file in tlist:
        with open(file = f'{path}{file}', mode = 'w+', encoding = 'utf-8') as f:
            f.write(requests.get(url = f'{file.replace("CAO-",url)}').text)
except Exception as e:
    print(e)