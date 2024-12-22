import sys
from PIL import Image, ImageOps

try:
    input = sys.argv[1]
    input = input.lower()
    if not (input.endswith('.png') or input.endswith('.jpg') or input.endswith('.jpeg')):
        sys.exit("Not an image file")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if input.endswith('.png'):
        extnsn = '.png'
    elif input.endswith('.jpg'):
        extnsn = 'jpg'
    elif input.endswith('.jpeg'):
        extnsn = 'jpeg'
    if not sys.argv[2].endswith(extnsn):
        sys.exit("Input and output have different extensions")

    shirt = Image.open('shirt.png')
    shirt = ImageOps.fit(shirt, size=[600,600])
    output = Image.open(input)
    output = ImageOps.fit(output, size=[600,600])
    output.paste(shirt, mask=shirt)
    output.save(sys.argv[2])

except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("Input does not exist")
