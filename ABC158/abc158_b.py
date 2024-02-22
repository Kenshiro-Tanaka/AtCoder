N, A, B = map(int, input().split())

ans = N//(A+B)*A # Nがあるブロックの1つ前のブロックまでの青いボールの数
ans += N%(A+B) if N%(A+B) < A else A  # Nがあるブロックの中で前から青いボールがいくつあるか

print(ans)


# 2行目はans += min(N%(A+B), A)でいい
