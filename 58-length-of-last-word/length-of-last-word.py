class Solution(object):
    def lengthOfLastWord(self, s):
        lw = s.strip().split()
        return len(lw[-1])