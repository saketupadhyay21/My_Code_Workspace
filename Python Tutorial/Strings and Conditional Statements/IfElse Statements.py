age = 5

if(age >= 18):
    print("Eligible")
elif(age>12 and age <18):
    print("Under parental guidence")
else:
    print("Not eligible")

marks = int(input("Enter your marks: "))

if(marks >= 90):
   print(" Your grade is A")
elif((marks <90) and (marks >= 80)):
    print("Your grade is B")
elif((marks <80) and (marks >= 70)):
    print("Your grade is C")
else:
    print("Your grade is D")