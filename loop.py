dollar_price = [1.50,9.60,5.60,10.00,25.52]

# cents_prices = []

# for price in dollar_price:
#     cents =int(price * 100)
#     cents_prices.append(cents)
    
# print(cents_prices)

cents_price = [int(price * 100) for price in dollar_price if price > 2]

print(cents_price)