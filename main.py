import urllib3
urllib3.disable_warnings()
import requests
from lxml import etree
yes = ['yes', 'y', 'Y', '1', 'Yes', 'YES']
no = ['no', 'n', 'N', '0', 'No', 'NO']
username = input('Enter the username to grab...')
req = requests.get(url = f'https://crawl.akrasiac.org/scoring/players/{username.lower()}.html')
while req.status_code == 404:
    print(f'The username {username} does not exist.')
    username = input('Enter the username to grab...')
    req = requests.get(url = f'https://crawl.akrasiac.org/scoring/players/{username.lower()}.html')
username = str(etree.HTML(req.text).xpath("//h2/text()")[0])[8:]
path = input('Enter path to store...')
path = path.replace('\\', '/') + ('/' if path[-1] != '/' else '')
# akrasiac
if input('Request CAO?') in yes:
    url = f'https://crawl.akrasiac.org/rawdata/{username}/'
    print('Requesting CAO...')
    req = requests.get(url = url)
    if req.status_code != 404:
        files = etree.HTML(req.text).xpath("//tr/td/a/@href")
        tlist = []
        for file in files:
            if file[-4:] == '.txt' and file[:7] == 'morgue-':
                tlist.append(file)
        for file in tlist:
            with open(file = f'{path}CAO-{file}', mode = 'w+', encoding = 'utf-8') as f:
                print(f'Downloading CAO-{file}...')
                f.write(requests.get(url = url + file).text)
# underhound
if input('Request CUE?') in yes:
    url = f'https://underhound.eu/crawl/morgue/{username}/'
    print('Requesting CUE...')
    req = requests.get(url = url)
    if req.status_code != 404:
        files = etree.HTML(req.text).xpath("//pre/a/@href")
        tlist = []
        for file in files:
            if file[-4:] == '.txt' and file[:7] == 'morgue-':
                tlist.append(file)
        for file in tlist:
            with open(file = f'{path}CUE-{file}', mode = 'w+', encoding = 'utf-8') as f:
                print(f'Downloading CUE-{file}...')
                f.write(requests.get(url = url + file).text)
# kelbi
if input('Request CKO?') in yes:
    url = f'https://crawl.kelbi.org/crawl/morgue/{username}/'
    print('Requesting CKO...')
    req = requests.get(url = url)
    if req.status_code != 404:
        files = etree.HTML(req.text).xpath("//tr/td/a/@href")
        tlist = []
        for file in files:
            if file[-7:] == '.txt.gz' and file[:7] == 'morgue-':
                tlist.append(file.strip('.gz'))
        for file in tlist:
            with open(file = f'{path}CKO-{file}', mode = 'w+', encoding = 'utf-8') as f:
                print(f'Downloading CKO-{file}...')
                f.write(requests.get(url = url + file).text)
# xtahua
if input('Request CXC?') in yes:
    url = f'https://crawl.xtahua.com/crawl/morgue/{username}/'
    print('Requesting CXC...')
    req = requests.get(url = url)
    if req.status_code != 404:
        files = etree.HTML(req.text).xpath("//tr/td/a/@href")
        tlist = []
        for file in files:
            if file[-4:] == '.txt' and file[:7] == 'morgue-':
                tlist.append(file)
        for file in tlist:
            with open(file = f'{path}CXC-{file}', mode = 'w+', encoding = 'utf-8') as f:
                print(f'Downloading CXC-{file}...')
                f.write(requests.get(url = url + file).text)
# berotato
if input('Request CBR2?') in yes:
    url = f'https://cbro.berotato.org/morgue/{username}/'
    print('Requesting CBR2...')
    req = requests.get(url = url)
    if req.status_code != 404:
        files = etree.HTML(req.text).xpath("//tr/td/a/@href")
        tlist = []
        for file in files:
            if file[-4:] == '.txt' and file[:7] == 'morgue-':
                tlist.append(file)
        for file in tlist:
            with open(file = f'{path}CBR2-{file}', mode = 'w+', encoding = 'utf-8') as f:
                print(f'Downloading CBR2-{file}...')
                f.write(requests.get(url = url + file).text)
# project357
if input('Request CPO?') in yes:
    url = f'https://crawl.project357.org/morgue/{username}/'
    print('Requesting CPO...')
    req = requests.get(url = url)
    if req.status_code != 404:
        files = etree.HTML(req.text).xpath("//pre/a/@href")
        tlist = []
        for file in files:
            if file[-4:] == '.txt' and file[:7] == 'morgue-':
                tlist.append(file)
        for file in tlist:
            with open(file = f'{path}CPO-{file}', mode = 'w+', encoding = 'utf-8') as f:
                print(f'Downloading CPO-{file}...')
                f.write(requests.get(url = url + file).text)
# webzook
# currently unavailable
# develz
if input('Request CDO?') in yes:
    url = 'https://crawl.develz.org/morgues/'
    files = []
    vers = [f'0.{i}/' for i in range(4,27)] + ['ancient/', 'git/', 'trunk/']
    print('Requesting CDO...')
    for ver in vers:
        req = requests.get(url = url + ver + username + '/')
        if req.status_code != 404:
            files += [ver] + etree.HTML(req.text).xpath("//pre/a/@href")
    for file in files:
        if file[:2] == '0.':
            ver = file
        elif file[-4:] == '.txt' and file[:7] == 'morgue-':
            with open(file = f'{path}CDO-{file}', mode = 'w+', encoding = 'utf-8') as f:
                print(f'Downloading CDO-{file}...')
                f.write(requests.get(url = url + ver + username + '/' + file).text)
# lazylife
# currently unavailable
# dcss.io
# currently unavailable
print('Finished downloading files.')