import math

# 事前に桁数を求めておく
# print(math.log10(15**15)) # log10(15**15) = 17.641より18桁
l = [1, 2**2, 3**3, 4**4, 5**5, 6**6, 7**7, 8**8, 9**9, 10**10, 11*11, 12**12, 13**13, 14**14, 15**15]

B = int(input())

print(l.index(B)+1 if B in l else -1)
