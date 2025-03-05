# book-finder

# Overview:

Book Finder is a command-line tool that helps students find the best deals on textbooks. The program searches multiple online stores using an ISBN and displays the prices, all converted to the user's preferred currency.

# Key Features:

1. Search for books using ISBN numbers
2. Fetch real-time prices from various stores using Barcode Lookup API
3. Convert prices to the preferred currency
4. Open links directly from terminal
5. Calculate total price of books

# Tools Used:

1. Python 3.11, including the third-party library requests
2. Barcode Lookup API for price data. Please note that the free version, which I used, has limited access.
3. Open Exchange Rates API for currency conversions. Again, the free version has limitations; specifically it doesn't allow a base currency other than USD. As a workaround, the program will perform an additional conversion from USD to the preferred currency.

# Example Workflow:
1. The user will be asked how many books they want, as well as the currency.
2. For each book, the user will be asked to enter an ISBN number.
3. The program fetches store and price data for the ISBN number and displays it. Prices will be converted to the preferred currency.
4. The user can select a store, which will open the link. The user can also add the book to a cart.
5. The program will display the total price of all the books in the cart.

# Future Improvements:
1. Allow search by title instead of limiting it to ISBN
2. Develop a GUI version
