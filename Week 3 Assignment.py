def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

# user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# final price
final_price = calculate_discount(original_price, discount_percentage)

#  result
if discount_percentage >= 20:
    print(f"After applying a {discount_percentage}% discount, the final price is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${original_price:.2f}")