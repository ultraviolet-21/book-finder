#display.py

from barcode_lookup import *
import webbrowser

def sort_by_price(stores: list[dict], to_currency: str) -> list[dict]:
    '''Converts prices to the desired currency, then sorts low to high'''
    
    for store in stores:
        converted_amount = exchange(store["currency"], float(store["price"]), to_currency)
        store.update({"adjusted price": converted_amount})
    new_list = sorted(stores, key=lambda x: float(x["adjusted price"]), reverse=False)
    return new_list


def display(stores: list[dict], to_currency) -> None:
    '''Displays the store name, price, and link for each online store selling the book'''

    for i in range(len(stores)):
        store = stores[i]
        print(f'{i+1}. Name: {store["name"]}')
        print(f'Price: {store["price"]} {store["currency"]}')
        if store["currency"] != to_currency:
            print(f'Price in {to_currency}: {store["adjusted price"]:.2f} {to_currency}')
        print(f'Link: {store["link"]}\n')
        

def add_books(stores):
    '''Allows the user to explore the various links and add books to cart'''

    answer = 'n'

    while answer != 'y':
        item = int(input("Which store do you want to check? "))
        webbrowser.open(stores[item - 1]["link"])
        answer = input("Is this the book you want? y/n ")

    return stores[item - 1]


if __name__ == "__main__":
    number = int(input("How many books do you need? "))
    to_currency = input("Enter a base currency: ")
    cart = []
    for i in range(number):
        barcode = input("Enter an ISBN number: ")
        stores = lookup(barcode)
        sorted_stores = sort_by_price(stores, to_currency)
        display(sorted_stores, to_currency)
        cart.append(add_books(sorted_stores))
    
    total_price = 0
    for item in cart:
        total_price += item["adjusted price"]

    print(f"Your total is {total_price:.2f} {to_currency}")

