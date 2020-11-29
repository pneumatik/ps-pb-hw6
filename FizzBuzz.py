s = 0
for x in range(1000, 20001):
    if x % 3 == 0 and x % 5 == 0:
        s = s + x
print(s)
