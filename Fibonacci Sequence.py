n = int(input())
num1 = 1
num2 = 0
sum= 0
for i in range (n):
    sum = num1 + num2
    num1 = num2
    num2 = sum
    print(f"{num2}")    

