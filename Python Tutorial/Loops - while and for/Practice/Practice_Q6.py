#WAP to find the sum of first n natural numbers - using while

num = int(input("Enter the number: "))

sum = 0
iterator = 0

while(iterator <= num):
    sum = sum + iterator
    iterator += 1
else:
    print("Sum of the first ", num , " numbers is: ", sum)
