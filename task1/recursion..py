def calculate(n, x, ans=0):
    if n == 1:
        return (1 / x) + ans
    ans += 1 / (x ** n)
    n -= 1
    return calculate(n, x, ans)


print(calculate(2, 3))
