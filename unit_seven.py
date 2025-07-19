# Fibonnacci with Memoization, memo servers as a cache and stores the numbers we've already encountered

def fibonacci(num, memo={}):
    if num in memo:
        return memo[num]
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    
    return memo[num]


print(fibonacci(600))