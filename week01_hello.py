# 실행: alt + shift + f10
#1번
#name = input("name input : ")
#print(f"welcome {name}")

number = int(input("Input number"))

if number < 2:
   count = 1
else:
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
           count = count + 1


if count == 2:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")