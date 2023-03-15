'''
5. Longest Palindromic Substring
Given a string s, return the longest
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
'''


def longestPalindrome(s: str) -> str:
    palindrome = ''
    check = ''
    if s == s[::-1]:
        return s
    for i in range(len(s)):
        for j in range(len(s[i:]) - 1, -1, -1):
            if s[i:j + i + 1] == s[i:j + i + 1][::-1]:
                check = s[i:j + i + 1]
                if len(check) > len(palindrome):
                    palindrome = check
    return palindrome


if __name__ == '__main__':
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
