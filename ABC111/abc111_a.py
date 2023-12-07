n = input()

n = n.replace("1", "a").replace("9", "b") # 一回間に挟めばreplace()使える
n = n.replace("a", "9").replace("b", "1")

print(n)
