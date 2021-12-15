def calculate(x, n):
    try:
        ans = 0
        for i in range(1, n + 1):
            ans += 1 / (x**i)
        return ans
    except Exception as e:
        print(e)


print(calculate(5, 2))
