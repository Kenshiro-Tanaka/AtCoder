# Pypyで提出するとTLEになるからPythonで

S = input()
T = input()

flag = False
for K in range(26):
    ans = ''
    for c in S:
        ans += chr(ord('a') + (ord(c)-ord('a') + K) % 26) # ord(c)がord('a')から見ていくつ離れているか
    
    if ans == T:
        flag = True
        break

print("NYoe s" [flag::2])
