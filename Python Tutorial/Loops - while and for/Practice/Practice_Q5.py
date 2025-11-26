find_num = 49
count = 0
my_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

while count < len(my_tuple):
    if (my_tuple[count] == find_num):
        print("Position =", count)
    count += 1