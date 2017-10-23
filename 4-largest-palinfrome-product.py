largest_palindrome = 0
lx, ly = 0, 0

for x in range(999, 100, -1):
    for y in range(x, 100, -1):
        product = x*y
        check = str(x*y)
        if check == check[::-1]:
            if product > largest_palindrome:
                largest_palindrome = product
                lx, ly = x, y

print("The largest palindrome is {} and is made from {} and {}"
      .format(largest_palindrome, lx, ly))
