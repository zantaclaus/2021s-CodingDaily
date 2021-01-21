def list_of_multiples(num, lst):
    ans = []
    for i in range(1, lst + 1):
        ans.append(num*i)
    return ans

# print(list_of_multiples(12, 10))