N = int(input())

for i in range(22):
    for j in range(22):
        for k in range(22):
            if i+j+k <= N:
                print(i, j, k)
