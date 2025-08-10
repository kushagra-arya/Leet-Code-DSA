class Solution(object):
    def isAnagram(self, s, t):
        # return sorted(s) == sorted(t)
        if sorted(s) != sorted(t):
            return False
        else: 
            return True