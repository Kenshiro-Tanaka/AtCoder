S = input()

# 集合にして文字の種類数で分類，数学的に出力は1 or 3 or 6
print('1' if len(set(S)) == 1 else '3' if len(set(S)) == 2 else '6')
