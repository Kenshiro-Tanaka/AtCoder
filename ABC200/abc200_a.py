N = input()

if 1 <= int(N) <= 99:
    print(1)
elif N[-2:] == "00":
    print(N[:-2])
else:
    print(int(N[:-2])+1)
    
