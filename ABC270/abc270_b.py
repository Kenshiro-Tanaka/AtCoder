X, Y, Z = map(int, input().split())

if X >= 0:
    if Y <= 0:
        print(X)
    else:
        if X < Y: # 間に壁がない
            print(X)
        else:
            if Z < Y:
                if Z <= 0:
                    print(2*abs(Z)+X) # ハンマー取りに負の方向へ行くから往復する
                else: # 0 <= Z < Y < X                    
                    print(X)
            else:
                print(-1)
else:
    if Y >= 0:
        print(abs(X))
    else:
        if Y < X: # 間に壁がない
            print(abs(X))
        else:
            if Y < Z:
                if Z >= 0:
                    print(2*Z+abs(X)) # ハンマー取りに負の方向へ行くから往復する
                else: # X < Y < Z <= 0              
                    print(abs(X))
            else:
                print(-1)

# 単純に場合分けはもっと減らせる
# さらに Y に対して考えると場合分けが半分に
