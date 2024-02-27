N = int(input())

st = set()
for a in range(2, 10**5+1, 1):
    b = 2
    while a**b <= N:
            st.add(a**b)
            b += 1

print(N-len(st)) # 2^4と4^2みたいな被りがある
