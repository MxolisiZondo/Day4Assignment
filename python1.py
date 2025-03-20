price = input("Enter the price: ")
price = float(price)
discount = input("Enter the discount: ")
discount = float(discount)
discounted_price = price - price * discount / 100
print("The discounted price is: ", discounted_price)