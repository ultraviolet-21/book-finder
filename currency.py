#currency.py

import requests

API_KEY = "a2874301fff94256b170f50eb0bf228a"
url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"


def exchange(from_currency: str, amount: float, to_currency: str = "USD") ->float:
    '''Uses Open Exchange API to convert between currencies at current exchange rates'''
    
    if from_currency == to_currency:
        return amount

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        exchange_rate = float(data["rates"].get(from_currency))

        if exchange_rate:
            converted_amount = amount / exchange_rate

            #Open Exchange uses default currency USD, but this program does not assume that
            if to_currency == "USD":
                return converted_amount

            else:
                rate = float(data["rates"].get(to_currency))
                return converted_amount * rate

        else:
            print(f"Currency {from_currency} not found in exchange rates.")
    else:
        print("Error: ", response.status_code)

