stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "SPRAY": 1000,
    "MOBILE": 4000,
    "PARFUME": 3000,
    "LAPTOP": 500
}

total = 0

# overwrite file every run (IMPORTANT)
file = open("portfolio.txt", "w")

file.write("Stock Portfolio Report\n")
file.write("----------------------\n")

num = int(input("How many items? "))

for i in range(num):

    name = input("Enter stock name: ").strip().upper()
    qty = int(input("Enter quantity: "))

    if name in stocks:
        price = stocks[name]
        investment = price * qty
        total += investment

        file.write(f"{name} | Qty: {qty} | Price: {price} | Investment: {investment}\n")

    else:
        # still save invalid entries
        file.write(f"{name} | Qty: {qty} | NOT FOUND\n")

file.write("----------------------\n")
file.write(f"TOTAL INVESTMENT = {total}\n")

file.close()

print("DONE - check portfolio.txt")