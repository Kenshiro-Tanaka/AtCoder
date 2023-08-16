A, B, C = map(int, input().split())

if C == 0:
    for _ in range(100):
        A -= 1
        if A <= 0: # A == 0としてしまうと最初のAが0のときifに入らない
            print("Aoki")
            break
        B -= 1
        if B <= 0:
            print("Takahashi")
            break
else:
    for _ in range(100):
        B -= 1
        if B <= 0:
            print("Takahashi")
            break
        A -= 1
        if A <= 0:
            print("Aoki")
            break

# forを使わずにifと数学で考えようとすると複雑になりそう
