series = []
series.append(1)
series.append(1)

# def end_of_loop():
#     raise StopIteration

# [next(iter(())) if series[k-1] > 4000000 else series.append(series[k-1]+series[k-2]) for k in range(2, 50)]
# series.pop()


def Fibonacci():
    f0, f1 = 1, 1
    while True:
        yield f0
        f0, f1 = f1, f0+f1

fibs = []
for f in Fibonacci():
    if f > 4000000:
        break
    else:
        fibs.append(f)

print(sum(num for num in fibs if not num % 2))
