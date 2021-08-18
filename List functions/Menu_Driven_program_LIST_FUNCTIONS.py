# Menu driven program to do various list operations
num = int(input("Enter the no. of elements you want in your list: "))
my_list = []
for i in range(num):
    element = int(input("Enter numeric element no.{}: ".format(i+1)))
    my_list.insert(i,element)
while True:
    def change():
        if choice in range(1,9):
            print("\nThe modified list:",my_list)
    print("\nLIST OPERATIONS")
    print('-'*16)
    print(" 1) Append an element")
    print(" 2) Insert an element")
    print(" 3) Append a list to the given list")
    print(" 4) Modify an existing element")
    print(" 5) Delete an existing element from its position")
    print(" 6) Delete an existing element with a given value")
    print(" 7) Sort the list in ascending order")
    print(" 8) Sort the list in descending order")
    print(" 9) Exit")
    choice = int(input("ENTER YOUR CHOICE (1-9) : "))
    # APPEND ELEMENT
    if choice == 1:
        element = int(input("Enter the number to be appended: "))
        my_list.append(element)
        print("The element has been appended.\n")
        change()
    # INSERT ELEMENT AT DESIRED POSITION
    elif choice == 2:
        element = int(input("Enter the number to be inserted: "))
        index = int(input("Enter its index: "))
        my_list.insert(index, element)
        print("The element has been inserted.\n")
        change()
    # APPEND A LIST TO THE GIVEN LIST
    elif choice == 3:
        new = input("Enter the list to be appended (element1 element2...separated by space): ")
        new1 = new.split()
        for i in new1:
            a = int(i)
            new_list = []
            new_list.append(a)
            my_list.extend(new_list)
        print("The new list has been appended.\n")
        change()
    # MODIFY AN EXISTING ELEMENT
    elif choice == 4:
        index = int(input("Enter its index: "))
        if index < len(my_list):
            new_element = int(input("Enter the new element: "))
            old_element = my_list[index]
            my_list[index] = new_element
            print("The element {} has been modified.\n".format(old_element))
        else:
            print("\nIndex of element is greater than the length of the list.")
        change()
    # DELETE AN EXISTING ELEMENT FROM ITS POSITION
    elif choice == 5:
        index = int(input("Enter its index: "))
        if index < len(my_list):
            element = my_list.pop(index)
            print("The element {} has been deleted\n".format(element))
        else:
            print("\nIndex of element is greater than the length of the list.")
        change()
    # DELETE AN EXISTING ELEMENT WITH A VALUE
    elif choice == 6:
        element = int(input("Enter the element to be deleted: "))
        if element in my_list:
            my_list.remove(element)
            print("\nThe element {} has been deleted\n".format(element))
        else:
            print("\nElement {} is not present in the list".format(element))
        change()
    # LIST IN ASCENDING ORDER
    elif choice == 7:
        my_list = sorted(my_list, reverse = False)
        print("\nThe list has been sorted in ascending order.")
        change()
    # LIST IN DESCENDING ORDER
    elif choice == 8:
        my_list = sorted(my_list, reverse = True)
        print("\nThe list has been sorted in descending order.")
        change()
    # EXIT FROM THE MENU
    elif choice == 9:
        break
    else:
        print("Choice isn't valid.") 