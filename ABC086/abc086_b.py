a, b = input().split()

N = int(a+b)
i = 1
while i*i <= N:
    if N/i == i:
        print("Yes")
        exit()
    i += 1

print("No")
