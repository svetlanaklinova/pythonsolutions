'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
'''

def minRemoveToMakeValid(s):
    open_parens_stack, illegal_indexes = [], set()
    for i, c in enumerate(s):
        if c == '(':
            open_parens_stack.append(i)
        elif c == ')':
            if open_parens_stack:
                open_parens_stack.pop()
            else:
                illegal_indexes.add(i)

    for i in open_parens_stack:
        illegal_indexes.add(i)


    return ''.join(c for i, c in enumerate(s) if i not in illegal_indexes)

assert minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
assert minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
assert minRemoveToMakeValid("))((") == ""
assert minRemoveToMakeValid("(a(b(c)d)") == "a(b(c)d)"
