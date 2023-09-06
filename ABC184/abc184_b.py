N, X = map(int, input().split())
S = list(input())

score = X
for i in S:
    if i == "x" and score > 0:
        score -= 1
    if i == "o":
        score += 1

print(score)
