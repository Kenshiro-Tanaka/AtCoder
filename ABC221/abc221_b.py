S = list(input())
T = list(input())

flag = True
for i in range(len(S)-1):
    if(S[i] != T[i]): # 一致しなかった時に
        S[i], S[i+1] = S[i+1], S[i] # 入れ替えてみて
        if S != T: # それでも一致しなかったら
            flag = False
            break
    
print("NYoe s" [flag::2])
