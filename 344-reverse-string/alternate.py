class Solution(object):
    def reverseString(self, s):
        l = []
        for i in range(len(s)-1, -1, -1):
            l.append(s[i])
        s[:] = l # s[:] = l will overwrite the contents of s while s=l will change 's' only inside the function
