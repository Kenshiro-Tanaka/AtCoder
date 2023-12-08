a, b = map(int, input().split())

x = a+b
print((x+2-1)//2) # 切り上げたいときは (a+b)/c ではなく (a+b+c-1)/c


# 切り上げはmath.ceil()
