from binance.client import Client
import xlsxwriter
import click
import os

currency = ""   # Currency you need all pairs for eg. USDT, BUSD
api_key = ""    #Binance API key (read-only)
api_secret = "" #Binance API Secret (read-only)

if not currency:
    currency = input("What currency are you looking for? ")
if not api_key:
    api_key = input("Binance API Key? ")
if not api_secret:
    api_secret = input("Binance API Secret? ")

pairs = ""
client = Client(api_key, api_secret)
exchange_info = client.get_exchange_info()
for s in exchange_info['symbols']:
    if currency in s['symbol']:
        pairs = pairs + s['symbol'] + "\n"


print(pairs)

if click.confirm('Write to Output.xtt file?', default=True):
    text_file = open("Output.txt", "w")
    text_file.write(pairs)
    text_file.close()
    print("Wrote file: " + os.path.realpath(text_file.name))

if click.confirm('Write to Output.xlsx file?', default=True):
    workbook = xlsxwriter.Workbook('Output.xlsx')
    worksheet = workbook.add_worksheet()
      
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 0
    column = 0
    content = pairs.splitlines()
      
    # iterating through content list
    for item in content :
      
        # write operation perform
        worksheet.write(row, column, item)
      
        # incrementing the value of row by one
        # with each iteratons.
        row += 1
          
    workbook.close()