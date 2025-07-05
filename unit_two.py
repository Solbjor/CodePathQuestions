def is_valid_post_format(posts):
    stack = []
    for char in posts:
        if char in "([{":
            stack.append(char)
            continue
        if not stack:
            return False
        top = stack[-1]
        if char == ')':
            if (top == '('):
                stack.pop()
            else:
                return False
        if char == ']':
            if (top == '['):
                stack.pop()
            else:
                return False
        if char == '}':
            if (top == '{'):
                stack.pop()
            else:
                return False
    if stack == []:
        return True
    else:
        return False    
            
print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

##WRITE TESTS FIRST USING INPUT EXAMPLES THEY GIVE YOU. EXAMPLE:

def is_balanced(s):
    if s[0] == ')':
        return False
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

testOne = is_balanced("((()))")
print(f"test 1 passed: {testOne == True}")

testTwo = is_balanced("(()())")
print(f"test 2 passed: {testTwo == True}")

testThree = is_balanced("(()(")
print(f"test 3 passed: {testThree == False}")

testFour = is_balanced(")()")
print(f"test 4 passed: {testFour == False}")

testFive = is_balanced("((((((((()")
print(f"test 5 passed: {testFive == False}")

#EXAMPLE OUTPUT
# TRUE
# TRUE
# FALSE


#EXAMPLE OUTPUT
# TRUE
# TRUE
# FALSE

###############################################

def reverse_comments_queue(comments):
    stack = []
    for comment in comments:
        stack.append(comments.pop())
    stack.append(comments.pop())
    return stack
        
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

###############################################

def is_symmetrical_title(title):
    right_pointer = len(title) - 1
    left_pointer = 0
    title = title.lower()
    print(title)
    while (left_pointer < right_pointer):
        if (title[left_pointer] == title[right_pointer]):
            left_pointer += 1
            right_pointer -= 1
        elif title[left_pointer] == ' ' and title[right_pointer] == ' ':
            left_pointer += 1
            right_pointer -= 1
        elif title[left_pointer] == ' ' or title[right_pointer] == ' ':
            if title[left_pointer] == ' ':
                left_pointer += 1
            else:
                right_pointer -= 1
        else:
            return False
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

###################################################

def engagement_boost(engagements):
    engagement = []
    right = len(engagements) - 1
    left = 0
    
    while left < right:
        engagement.append(engagements[left] * engagements[left])
        engagement.append(engagements[right] * engagements[right])
        left += 1
        right -= 1
    engagement.append(engagements[left] * engagements[left])
    engagement.sort()
    return engagement

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))

###################################################

def clean_post(post):
    stack = []
    for char in post:
        if not stack:
            stack.append(char)
            top = stack[-1]
            continue
        if char.lower() == top.lower() and (char != top):
            stack.pop()
            if stack:
                top = stack[-1]
        else:
            stack.append(char)
            top = stack[-1]
        
    word = ''
    for char in stack:
        word += char
        
    return word
            
        
print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s"))





