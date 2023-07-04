S = [input() for i in range(2)]
# 行き来できないマス目はこの2通りだけ
flag = False if S == ['#.', '.#'] else False if S == ['.#', '#.'] else True
print("NYoe s"[flag::2])
