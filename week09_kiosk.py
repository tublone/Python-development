# Incheon Science High School CAFE
# Black Coffee 1500, Latte 2500

# beverage = ["black coffee", "latte", "iced tea"]
# prices = [1500, 2500, 2300]
beverage_prices_quantity = {'black coffee': [1500, 0],
                   'latte': [2500, 0],
                   'iced tea': [2300, 0]
                   }
total_price = 0

def select_menu(index):
    """
    display, calculate total price and count quantity
    :param index: index of list
    :return: None
    """

    global total_price
    print(f"You ordered {beverage[index]}. The price is {prices[index]} won.")
    total_price += prices[index]
    quantity[index] += 1


menu_lists = ""
# for m in range(len(beverage)):
i = 1
for k, v in beverage_prices_quantity.items():
    menu_lists = menu_lists + f"{i}) {k} {v[0]} won  "
    i += 1
menu_lists = menu_lists + f"{i}) End order : "


while True:
    menu = input(menu_lists)
    if menu == '4':
        print("Your order has been accepted.")
        break
    elif menu == '1':
        select_menu(0)
    elif menu == '2':
        select_menu(1)
    elif menu == '3':
        select_menu(2)
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu")

for i in range(len(beverage)):
    if quantity[i] != 0:
        print(f"{beverage[i]}\n\t{prices[i]}\tX{quantity[i]}\t{prices[i] * quantity[i]}")

print(f"The total amount is {total_price} won.")