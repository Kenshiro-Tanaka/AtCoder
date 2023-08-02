def f(x):
    return 1 if x == 0 else x * f(x-1)

N = int(input())

print(f(N))
