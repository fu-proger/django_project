def f(n):
    c4 = 0
    n4 = n
    while n4:
        c4 += n4 % 4
        n4 //= 4
    c8 = 0
    n8 = n
    while n8:
        c8 += n8 % 8
        n8 //= 8
    return c8 == c4


ans = 0
n = 52
for i in range(2 ** n):
    if f(i):
        ans += 1
print(ans)