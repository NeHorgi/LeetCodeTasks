'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
'''

def isValid(s: str) -> bool:
    openers = '([{'
    closers = ')]}'
    result = []
    if s[0] in closers or s[-1] in openers:
        return False
    for letter in s:
        if letter in openers:
            result.append(letter)
        else:
            if result == []:
                return False
            else:
                if closers.index(letter) == openers.index(result[-1]):
                    result.pop()
                else:
                    return False
    if result == []:
        return True
    else:
        return False


if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
