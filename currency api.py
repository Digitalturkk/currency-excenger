import freecurrencyapi as curapi
import csv

def exchange_rate(from_cur, to_cur, api_key):

    client = curapi.Client(api_key)

    result = client.latest(currencies=[from_cur, to_cur])
    return result["data"][to_cur]

from_cur = "USD"
to_cur = "TRY"
api_key = "" # your api key from freecurrencyapi.com (It is fully free!)

rate = exchange_rate(from_cur, to_cur, api_key)
rate = round(rate, 2)

with open("exchange_rate.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow([from_cur, to_cur, rate])
print("Data written to exchange_rate.csv")
