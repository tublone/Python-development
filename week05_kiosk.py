# Incheon Science High School CAFE
# Black Coffee 1500, Latte 2500

beverage = ["Black Coffee", "Latte"]
prices = [1500, 2500]

while True:
    menu = int(input("1) Black Coffee  2) Cafe Latte  3) End Order : "))
    if menu == 3:
        print("Exit Program")
        break
    elif menu == 1:
        print("You ordered Black Coffee. The price is 1500 won.")
    elif menu == 2:
        print("You ordered Cafe Latte. The price is 2500 won.")