n = int(input())
b = [input() for i in range(n)]
for i in b:
    c = i.find("зайка")
    if c >= 0:
        print(c + 1)
    else:
        print("Заек нет =(")
