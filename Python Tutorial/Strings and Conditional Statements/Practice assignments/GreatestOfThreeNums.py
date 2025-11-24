num1 = int(input("Enter the first number num1: "))
num2 = int(input("Enter the second number num2: "))
num3 = int(input("Enter the third number num3: "))

if((num1 == num2) and (num1 == num3)):
    print("All three numbers are equal")
elif((num1 > num2) and (num1 > num3)):
    print("num1 is greatest")
elif(num2 > num3):
    print("num2 is greatest")
elif(num2 == num3):
    print("num2 and num3 are eqal but greater than num1")
else:
    print("num3 is greatest")