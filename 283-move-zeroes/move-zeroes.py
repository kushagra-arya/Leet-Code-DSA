class Solution(object):
    def moveZeroes(self, nums):
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                a = nums.pop(i)
                nums.append(a)
        return nums