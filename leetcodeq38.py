from collections import deque


def longestValidParentheses(s):
    length = len(s)
    stack = deque([-1])
    longest = 0
    print(stack)
    for i in range(length):
        print("\n Check ", s[i])
        if s[i] == "(":
            print(f"append {i} in stack")
            stack.append(i)
            print("stack = ", stack, "\n")
        elif s[i] == ")":
            print("Pop from stack")
            stack.pop()
            print("stack = ", stack)
            print("if not stack:", not stack)
            if not stack:
                print(f"append {i} in stack")
                stack.append(i)
                print("stack = ", stack)
            else:
                print(f"i {i} - {stack[-1]} stack[-1] = ", i - stack[-1])
                longest = max(longest, i - stack[-1])
                print("longest = ", longest)

    return longest


s = "()()()(()"

print(longestValidParentheses(s))
