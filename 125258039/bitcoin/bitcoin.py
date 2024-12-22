import requests
import sys

try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    rate = (r["bpi"]["USD"]["rate_float"])
    price = rate * n
    print(f"${price:,.4f}")

except requests.RequestException:
    sys.exit("Error")