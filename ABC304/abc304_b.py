N = input()

# 書いてみたら上位3桁だけ保持して0埋めでいいことが分かる
print(N[:3].ljust(len(N), '0'))
