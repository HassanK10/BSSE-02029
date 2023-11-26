 
rows = int(input("Enter num of rows : "))
for m in range(rows, 0, -1):
    for n in range(1, m + 1):
        print("*", end=" ")
    print() 