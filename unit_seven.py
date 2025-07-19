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


def count_suits_iterative(suits):
    count = 0
    for suit in suits: 
        count+=1 
    return count
def count_suits_recursive(suits ):
    # base case 
    count = 0 
    if len(suits) == count:
        return count
    count += 1
    return 1 + count_suits_recursive(suits)

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))



def sum_stones(stones):
    
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))