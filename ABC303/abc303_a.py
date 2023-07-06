N = int(input())
S = input()
T = input()

# replaceを使ってlとoに寄せる方法
print("NYoe s"[(S.replace('1', 'l').replace('0', 'o') 
                == T.replace('1', 'l').replace('0', 'o'))::2])
