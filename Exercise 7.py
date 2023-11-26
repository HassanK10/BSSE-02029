
def check_pal(n) :
    n = str(n)
    return n == n [ : : -1 ]
check_num = input(print("Enter a number :")) 
res = check_pal(check_num)  
if res :
    print(f"{check_num} is a palindrome") 
else :
    print(f"{check_num} is not a palindrome")     