N = int(input())
S = [input() for i in range(N)]
S1 = [0 for i in range(N)]

dic = dict(zip(S, S1))
ans = 0

for i in S:
    dic[i]+=1

for k, v in dic.items():
    if ans < v:
        ans = v
        result = k
    
print(result)
