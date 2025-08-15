class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        k = 0
        if len(s) == 0:
            return True
        for i in range(len(s) - 1, -1, -1):
            if s[k] != s[i]:
                return False
            k += 1
        return True
