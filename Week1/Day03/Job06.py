x = "abcdefghijklmnopqrstuvwxyz" * 10
row_limit = 10

for i in range(1, row_limit+1):
    row_chars = x[sum(range(i)) : sum(range(i+1))]
    print(row_chars.center(26))