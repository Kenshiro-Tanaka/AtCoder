import re

N = int(input())
S = input()

result = re.sub(r"(.)\1{1,}", "\g<1>", S) # 任意の1文字の1回以上の繰り返しをその(gはグループ要素を表す)1文字にする

print(len(result))


# ランレングス符号化で解く
# from itertools import groupby

# def runLengthEncode(S: str) -> "List[tuple(str, int)]":
#     grouped = groupby(S)
#     res = []
#     for k, v in grouped:
#         res.append((k, int(len(list(v)))))
#     return res

# def main():
#     N = int(input())
#     S = input()
#     print(len(runLengthEncode(S)))
#     return
