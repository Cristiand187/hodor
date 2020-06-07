#!/usr/bin/python3
"""module requests hodor"""
import requests


url = 'http://158.69.76.135/level0.php'
params = {'id': '1729', 'holdthedoor': 'submit'}
votos = 0
while votos <= 350:
    response = requests.post(url, data=params)
    votos += 1
    print("voto number: {}".format(votos))

print("Voting complete!")
