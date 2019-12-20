# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        numsdx = {}
        for idx, i in enumerate(nums):          
            n = target - i
            if n not in numsdx:                
                numsdx[i]=idx
            else:
                return [idx, numsdx[n]]
