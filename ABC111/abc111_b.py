N = int(input())

l = [111, 222, 333, 444, 555, 666, 777, 888, 999]
for i in l:
    if i - N >= 0:
        print(i)
        break
