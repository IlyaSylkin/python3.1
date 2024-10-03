b = []
while (i := input()) != "":
    b.append(i)
for j in range(len(b)):
    if b[j].find("#") > 0:
        print(b[j][: b[j].find("#")])
    elif b[j].find("#") == -1:
        print(b[j])
