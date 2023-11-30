def factorial(num):
	return num * factorial(num-1) if num != 0 else 1

l = [] # 硬貨リスト [10!, 9!, ..., 1!]にしたい
for i in range(10):
	l.append(factorial(i+1))

l = list(reversed(l)) # 大きい方から扱いたい

P = int(input())

cnt = 0
while P > 0: # Pは0で終わることが保証されている
	for i in l:
		if P >= i: # 大きい方から比べてもP以上なら
			cnt += 1
			P -= i
			break # lの最初から比較し直すから

print(cnt)
