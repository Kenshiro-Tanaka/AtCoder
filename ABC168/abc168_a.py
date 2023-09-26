N = input()

print("bon" if N[-1] in ["3"] else "pon" if N[-1] in ["0", "1", "6", "8"] else "hon")
