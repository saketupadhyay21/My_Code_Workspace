age = int(input("Enter your age: "))

#nesting

if(age < 80):
    if(age >= 18):
        print("you can drive")
    else:
        print("you cannot drive")
else:
    print("It's not safe to drive")