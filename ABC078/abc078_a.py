X, Y = input().split()

print("<" if ord(X) < ord(Y) else ">"  if ord(X) > ord(Y) else "=")
