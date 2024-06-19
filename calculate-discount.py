def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

if __name__ == "__main__":
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)
        if final_price == price:
            print(f"No discount applied. The original price is: {price}")
        else:
            print(f"The final price after applying the discount is: {final_price}")
    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")
