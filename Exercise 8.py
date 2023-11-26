
List1 = [3 , 14 , 7 ,80 , 18 , 13]
List2 = [11 , 76 , 16 , 18 , 1 , 12]
List_res = []
for n in List1 :
    if n % 2 != 0 :
        List_res.append(n)
for n in List2 :
    if n % 2 == 0 :
        List_res.append(n)        
print("New list is : ", List_res)