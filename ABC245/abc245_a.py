A, B, C, D = map(int, input().split())

Ta = "Takahashi"
Ao = "Aoki"
if A < C:
    print(Ta)
elif A > C:
    print(Ao)
else:
    print(Ta if B <= D else Ao)
    
