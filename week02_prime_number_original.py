# 실행: alt + shift + f10
#1번
#name = input("name input : ")
#print(f"welcome {name}")

number = int(input("Input number : "))

is_prime_number = True
if number < 2:
   is_prime_number = False
else:
     #for i in range(2, number):
     i = 2
     while i*i < number: # reduce loop operation
        if number % i == 0:
            is_prime_number = False # Remove addition operation
            break  # Escape from the loop when the first divisor is found, improving performance when the input value is not a prime number
        print(i, end=" ")
        i = i + 1


if is_prime_number: #Remove comparison operators
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")