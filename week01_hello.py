# 실행: alt + shift + f10
#1번
#name = input("name input : ")
#print(f"welcome {name}")

number = int(input("Input number"))

if number < 2:
   count = 1
else:
    count = 0
    for i in range(2, number):
        if number % i == 0:
           count = count + 1
            break  # Escape from the loop when the first divisor is found, improving performance when the input value is not a prime number
        print(i, end=" ")


if count == 0:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")