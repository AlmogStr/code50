import sys
from PIL import Image, ImageOps
import requests

response = requests.get('https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png')
with open("shirt.jpg", "wb") as f:
    f.write(response.content)

url = "https://cs50.harvard.edu/python/2022/psets/6/shirt/before3.jpg"
response1 = requests.get(url)

try:
    input = sys.argv[1]
    input = input.lower()
    if not (input.endswith('.png') or input.endswith('.jpg') or input.endswith('.jpeg')):
        sys.exit("Not an image file")
    with open(input, "wb") as f:
        f.write(response1.content)
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    shirt = Image.open('shirt.jpg')
    shirt = ImageOps.fit(shirt, size=[200,200])
    output = Image.open(input)
    output = ImageOps.fit(output, size=[200,200])
    output.paste(shirt, mask=shirt)
    output.save(sys.argv[2])

except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
