N, Q = map(int, input().split())
event = [list(map(int, input().split())) for _ in range(Q)]

player = [0]*N # 選手のカード数
for i in range(Q):
    if event[i][0] == 1:
        player[event[i][1]-1] += 1 # event[i][1]はxなので1からNまで
        if player[event[i][1]-1] == 2: # イエローカードが累計2枚
            player[event[i][1]-1] = -1 # 退場した選手は負の値にする
    elif event[i][0] == 2:  # レッドカード
        player[event[i][1]-1] = -1
    else:
        print("Yes" if player[event[i][1]-1] < 0 else "No")
