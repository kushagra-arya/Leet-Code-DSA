class Solution(object):
    def maximum69Number (self, num):
        lst = list(str(num))
        a = ""
        for i in range(len(lst)):
            if lst[i] == "6":
                lst[i] = "9"
                break
        for j in range(len(lst)):
            a += lst[j]
        return int(a)