S = list(input())

ans, n = 0, len(S)-1
for i in S:
    ans += (ord(i)-64)*26**n # 26進数みたいな考え方で 係数 * 26^n
    n -= 1

print(ans)
