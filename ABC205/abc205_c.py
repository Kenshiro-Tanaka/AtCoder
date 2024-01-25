A, B, C = map(int, input().split())

if C%2 == 0: # A^C と B^C だから C の偶奇で底の扱いが変わる
    print("<" if abs(A) < abs(B) else ">" if abs(A) > abs(B) else "=")
else:
    print("<" if A < B else ">" if A > B else "=")
