N = int(input())
S = input()

for n in range(N-2):
    if S[n:n+3] == "ABC":
        print(n+1)
        exit()
    
print(-1)
