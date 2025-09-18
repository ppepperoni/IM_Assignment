mydict = {}

print("Matrix size: ")
size = int(input())

for i in range(size):
    print(f"Shopping items {i+1}:")
    items = input()
    mydict[i] = items

print(f"You have {len(mydict)} items in the cart")

while True:
    print("What would you like to do [C]hange items [R]emove [D]isplay  [S]earch [*] Exit?: ")
    choice = input().lower()

    if choice == "*":
        print("Bye")
        break
    
    if choice == "c":
        print("Enter key to change:")
        key_change = int(input())
        if mydict.get(key_change) is not None:
            print(f"Found {mydict[key_change]} item")
            print("Enter value:")
            new_value = input()
            mydict[key_change] = new_value
            print(f"Key {key_change} has been updated to {new_value}")
        else:
            print("Key not found")
            
    elif choice == "r":
        print("Enter key to remove:")
        key_remove = int(input())
        if mydict.get(key_remove) is not None:
            removed = mydict.pop(key_remove)
            print(f"The key {key_remove} with value {removed} has been deleted")
        else: 
            print("Key not found")
    
    elif choice == "d":
        print("Displaying Values")
        print("Key", "Value")
        for key, values in mydict.items():
            print(f"{key:<5}{values}")
            
    elif choice == "s":
        print("Enter item to search:")
        search = input().lower()
        found = False
        for keys, values in mydict.items():
            if search == values.lower():
                print(f"Found {search} item with item id: {keys}")
                found = True
                break
        
        if not found:
            print("I'm sorry, not in the cart")
    
    else:
        print("Invalid choice. Please try again.")