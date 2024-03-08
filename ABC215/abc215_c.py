import itertools

S, K = input().split()

words = ["".join(i) for i in itertools.permutations(S)] # 文字列の全組み合わせ
sort_words = sorted(list(set(words))) # 重複を消してソート

print(sort_words[int(K)-1])
