import requests
import sys
import decimal

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    b = decimal.Decimal(sys.argv[1])
except decimal.InvalidOperation:
    sys.exit("Command-line argument is not a number")


try:
    api_key = "3d5bbe069ce9399906322c3fb921efc796bf7326c03b253d1ab2a4590c784fc6"
    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + api_key)
    r = r.json()
    p = decimal.Decimal(r["data"]["priceUsd"])
    # print(p)
except requests.exceptions:
    sys.exit("API Error")

print(f"${(b * p):,.4f}")
