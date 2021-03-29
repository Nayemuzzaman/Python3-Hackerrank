import array as arr

print("--------Array------------")
# array just store one type of data
# index based used the data


a = arr.array("i", [1, 2, 3, 4, 5])
while True:
    print("1. print Array")
    print("2. Add Elements")
    print("3. Delete Elements")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The array elements are: ")
        for numbers in a:
            print(numbers)
    elif choice == 2:
        val = int(input('please enter the integer number:'))
        if isinstance(val, int):
            a.append(val)
    elif choice == 3:
        value = a.pop()
        print("Delete value enter: ", value)
    elif choice == 4:
        break
    else:
        print('Enter valid choice.')
