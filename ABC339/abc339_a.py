S = input()

tmp = ""
for i in S:
    if i == ".": # .が出たら文字列リセット
        tmp = ""
    else: 
        tmp += i

print(tmp)
