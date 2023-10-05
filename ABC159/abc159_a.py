N, M = map(int, input().split())

NC2 = N*(N-1)//2 if N > 0 else 0
MC2 = M*(M-1)//2 if M > 0 else 0
print(NC2+MC2) # 奇数は M*N 個
