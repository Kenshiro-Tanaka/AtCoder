S = input()

a = int(S[:2])
b = int(S[2:])

# 年の範囲は考慮しなくていい
print("AMBIGUOUS" if 1 <= a <= 12 and 1 <= b <= 12 else "YYMM" if 1 <= b <= 12 else "MMYY" if 1 <= a <= 12 else "NA")
