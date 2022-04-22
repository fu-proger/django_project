n = int(input())
i = 2
m = []
while i <= int(n ** 0.5) + 2:
    if n % i == 0:
        m.append(i)
        n = n // i
    else:
        i = i + 1
if n > 1:
    print(n)
else:
    m.sort()
    print("*".join(str(i) for i in m))
