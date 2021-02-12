def check(allowed, words):
    ans = 0
    for word in words:
        count = 0
        for item in list(word):
            if item not in list(allowed):
                ans += 1
                break
    return ans

allowed = input()
words = [item for item in input().split()]

print(len(words) - check(allowed, words))