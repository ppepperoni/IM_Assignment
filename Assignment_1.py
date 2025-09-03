print("Enter row: ")
num = int(input())
    
print("Enter col: ")
num2 = int(input())

print("Search: ")
num3 = int(input())
for i in range(1, num+1):
    for j in range(1, num2+1):
        result = i * j
        if num3 == result:
            print(f"[{result:4}]", end=" ")   
        else:
            print(f"{result:4}", end=" ")    
    print()