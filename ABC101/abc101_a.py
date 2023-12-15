S = list(input())

num = 0
for i in S:
    num += 1 if i == "+" else -1
    
print(num)
