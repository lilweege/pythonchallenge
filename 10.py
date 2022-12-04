def desc(x):
    a = ""
    s = str(x)
    n = len(s)
    i = 0
    while i < n:
        c = s[i]
        m = 0
        while i < n and s[i] == c:
            i += 1
            m += 1
        a += str(m) + c
    return int(a)

x = 1
for _ in range(30):
    x = desc(x)
print(len(str(x)))
