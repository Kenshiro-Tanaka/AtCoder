N, M = map(int, input().split())

# その食べ物を好きだと言った人数をカウントして N に一致すればいい
food = [0]*M
for i in range(N):
    A = list(map(int, input().split()))
    A = A[1:] # Kは使わないので削る
    for i in A:
        food[i-1] += 1
    
print(food.count(N))
