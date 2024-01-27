N = int(input())

l = []*N
for i in range(1, N+1, 1):
    cnt = 0 
    while i > 1:
        if i%2 == 0:
            i //= 2
            cnt += 1
        else:
            break
    l.append(cnt)

print(l.index(max(l))+1)
