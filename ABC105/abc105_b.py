N = int(input())

for i in range(100//4+1):
    for j in range(100//7+1):
        if 4*i+7*j == N:
            print("Yes")
            exit()

print("No")
