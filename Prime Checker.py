n = int(input())
ip = 1
for i in range(2, n):  
    if n % i == 0:  
        ip = 0  
        break 
if ip == 1:
    print("Prime")
else:
    print("Not Prime")