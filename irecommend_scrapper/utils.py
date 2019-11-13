from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_proxies():
    ua = UserAgent()
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')
    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    proxies = []
    for row in proxies_table.tbody.find_all('tr'):
        ip, port = row.find_all('td')[0].string, row.find_all('td')[1].string
        proxies.append('http://' + ip + ':' + port)

    return proxies
