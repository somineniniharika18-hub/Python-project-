stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 150,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker")

n = int(input("How many stocks do you want to add? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not available in price list.")

print("\nPortfolio Summary")
print("----------------------")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} : {quantity} shares × ${price} = ${investment}")

print("----------------------")