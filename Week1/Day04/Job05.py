L = [1, 2, 3, 4, 5]

print(L[1])

def replace_with_sum(lst):
    lst[3] = lst[2] + lst[4]

replace_with_sum(L)

print(L[-1])
