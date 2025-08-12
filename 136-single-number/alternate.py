class Solution(object):
    def singleNumber(self, nums):
        dict = {}
        for num in nums:
            dict[num] = dict.get(num,0)+1

        for key, value in dict.items():
            if value == 1:
                return key
