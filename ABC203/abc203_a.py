a, b, c = map(int, input().split())

if a == b: # a=b=cはここに含まれる 
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)
else:
    print(0)
