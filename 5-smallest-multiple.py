optimized_check_list = [11, 13, 14, 16, 17, 18, 19, 20]


def solver(step):
    maximum = 99999999999
    for num in range(step, maximum, step):
        if all(num % n == 0 for n in optimized_check_list):
            return num
    return None

result = solver(2520)

if result is None:
    print("No solution within the range")
else:
    print("The answer is:", result)
