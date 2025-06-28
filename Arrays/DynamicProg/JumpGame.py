class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        r=0
        for i in range(0,len(nums)):
            if i>r:
                return False
            r=max(r,i+nums[i])
        return True
        
