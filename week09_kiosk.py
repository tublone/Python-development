# Incheon Science High School CAFE
# Black Coffee 1500, Latte 2500

# beverage = ["black coffee", "latte", "iced tea"]
# prices = [1500, 2500, 2300]
beverage_prices_quantity = {'black coffee': [1500, 0],
                   'latte': [2500, 0],
                   'iced tea': [2300, 0]
                   }
total_price = 0

def select_menu(key):
    """
    display, calculate total price and count quantity
    :param key: key of dictionary
    :return: None
    """

    global total_price
    print(f"You ordered {key}. The price is {beverage_prices_quantity[key][0]} won.")
    total_price += beverage_prices_quantity[key][0]
    beverage_prices_quantity[key][1] += 1


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
        select_menu('black coffee')
    elif menu == '2':
        select_menu('latte')
    elif menu == '3':
        select_menu('iced tea')
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu")

for key, value in beverage_prices_quantity.items():
    if value[1] != 0:
        print(f"{key}\n\t{value[0]}\tX{value[1]}\t{value[0] * value[1]}")

print(f"The total amount is {total_price} won.")