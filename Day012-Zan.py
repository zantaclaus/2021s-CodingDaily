lst = [int(item) for item in input().split()]
big = max(lst[0], lst[2])
lst[0] = big
lst[1] = big
lst[2] = big

print(lst)