ln = int(input())
n = int(input())
b = [input() for i in range(n)]
for i in b:
    if len(i) > ln:
        print(i[: ln - 3] + "...")
    else:
        print(i, "fasdfasdfasfaf")
