n = int(input())
factsum = 0

for i in range(1, n // 2 + 1): 
    if n % i == 0:
        factsum += i

if factsum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")