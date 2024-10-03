n = int(input())
c = 0
for i in range(n):
    if input()[0] in "абв":
        c += 1
if c == n:
    print("YES")
else:
    print("NO")
