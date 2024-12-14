def count(num):
    counts = {i: 0 for i in range(1, 10)}
    for n in num:
        for i in range(1, 10):
            if n % i == 0:
                counts[i] += 1

    return counts
num = []
num = list(map(int, input("Enter numbers : ").split()))
res = count(num)
print(res)
