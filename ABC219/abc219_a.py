X = int(input())

if 0<=X<40:
    print(40-X)
elif 40<=X<70:
    print(70-X)
else:
    print(90-X if 70<=X<90 else "expert")
  
