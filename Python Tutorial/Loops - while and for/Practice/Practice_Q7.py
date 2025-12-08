#WAP to find the fatorial of the given number - use for loop

num = int(input("Enter the number: "))

factorial = 1

for num in range(1, num + 1):
    factorial = factorial * num

print("Factorail is: ", factorial)