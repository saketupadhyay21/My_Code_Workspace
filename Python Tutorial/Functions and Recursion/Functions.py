def calc_sum(num1, num2):
    return num1 + num2

#print(calc_sum(15, 6))


def list_len(cities):
    return len(cities)

cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Banglore"]
#print(list_len(cities))

def calc_factorial(num):
    factorial = 1
    for i in range(num, 1, -1):
        factorial = factorial * i
    return factorial
    
print(calc_factorial(5))

def dollar_to_INR(value):
    return value * 90.5

print(dollar_to_INR(100))

print(dollar_to_INR(56))