from binance.client import Client

currency = ""   # Currency you need all pairs for eg. USDT, BUSD
api_key = ""    #Binance API key (read-only)
api_secret = "" #Binance API Secret (read-only)

if not currency:
    currency = input("What currency are you looking for? ")
if not api_key:
    api_key = input("Binance API Key? ")
if not api_secret:
    api_secret = input("Binance API Secret? ")


client = Client(api_key, api_secret)
exchange_info = client.get_exchange_info()
for s in exchange_info['symbols']:
    if currency in s['symbol']:
        print(s['symbol'])