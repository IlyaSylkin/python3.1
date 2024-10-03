a = input()
print("YES" * (a == a[::-1]), "NO" * (a != a[::-1]), sep="")
