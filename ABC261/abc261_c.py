N = int(input())
d = {}
for i in range(N):
    s = input()
    if s in d:
        d[s] += 1
        print(s+"("+str(d[s]-1)+")")
    else:
        d[s] = 1
        print(s)
