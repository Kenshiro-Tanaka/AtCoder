P = list(map(int, input().split()))

ans = ''
for i in P:
    ans += chr(i + 97 - 1) # 97が'a'を表すのでiが1のときにchr(97)になってほしい

print(ans)
