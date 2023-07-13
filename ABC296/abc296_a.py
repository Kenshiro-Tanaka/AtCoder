N = int(input())
S = input()

S1 = "MF"*50
S2 = "FM"*50

if (S in S1) or (S in S2):
    print("Yes")
else:
    print("No")

# Sの中にMM, FFが存在しないことを使った方が早い
