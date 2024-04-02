# Incheon Science High School CAFE
# Black Coffee 1500, Latte 2500

beverage = ["Black Coffee", "Latte"]
prices = [1500, 2500]
total_price = 0

while True:
    menu = (input("1) Black Coffee  2) Cafe Latte  3) End Order : "))
    if menu == '3':
        print("Your order has been accepted.")
        break
    elif menu == '1':
        print("You ordered Black Coffee. The price is 1500 won.")
        total_price = total_price + prices[0]
    elif menu == '2':
        print("You ordered Cafe Latte. The price is 2500 won.")
        total_price = total_price + prices[1]
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu")

print(f"Your order has been accepted. The total amount is {total_price} won.")