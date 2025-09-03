while True:
    
    print("Enter row: ")
    num = int(input())
    if num == 0:
        print("You entered 0 in row. Exiting...")
        break
    
    print("Enter column: ")
    num2 = int(input())
    if num2 == 0:
        print("You entered 0 in column. Exiting...")
        break
    
    print("Search: ")
    num3 = int(input())

    for i in range(1, num+1):
        for j in range(1, num2+1):
            result = i * j
            if num3 == result:
                print(f"[{result}]", end=" ")   
            else:
                print(f"{result}", end=" ")    
        print()
