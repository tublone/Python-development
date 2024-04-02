# Incheon Science High School CAFE
# Black Coffee 1500, Latte 2500

beverage = ["Black Coffee", "Latte", "Iced Tea"]
prices = [1500, 2500, 2300]
quantity = [0, 0, 0]
total_price = 0

while True:
    menu = (input("1) Black Coffee  2) Cafe Latte  3) Iced Tea  4) End Order : "))
    if menu == '4':
        print("Your order has been accepted.")
        break
    elif menu == '1':
        print("You ordered Black Coffee. The price is 1500 won.")
        total_price = total_price + prices[0]
        quantity[0] += 1
    elif menu == '2':
        print("You ordered Cafe Latte. The price is 2500 won.")
        total_price += prices[1]
        quantity[1] += 1
    elif menu == '3':
        print("You ordered Iced Tea. The price is 2300 won.")
        total_price += prices[2]
        quantity[2] += 1
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu")
print(f"{beverage[0]} X{quantity[0]}")
print(f"{beverage[1]} X{quantity[1]}")
print(f"{beverage[2]} X{quantity[2]}")
print(f"Your order has been accepted. The total amount is {total_price} won.")