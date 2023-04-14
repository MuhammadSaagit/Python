L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
even_sum = 0
for num in L:
    if num % 2 == 0:
        even_sum += num
print("Sum of even numbers in the list is:", even_sum)