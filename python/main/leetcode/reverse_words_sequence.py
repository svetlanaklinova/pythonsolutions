
class Solution:
    def reverseWords(self, s):
        if not s or len(s) == 0:
            return s
        sList = s.strip().split()
        rev = sList[::-1]
        return " ".join(rev)


sol =  Solution()
assert (sol.reverseWords("raz dva tri") == 'tri dva raz')
assert (sol.reverseWords("123") == '123')
assert (sol.reverseWords("") == '')