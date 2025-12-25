with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("World", "Saket")

print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

print()