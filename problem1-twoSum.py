class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            j = i + 1
            
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return i,j
                j += 1
        
