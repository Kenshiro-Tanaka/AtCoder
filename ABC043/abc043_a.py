def f(N):
    return N+f(N-1) if N != 0 else 0

N = int(input())

print(f(N))
