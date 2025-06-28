class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Kadanes Algorithm
        res=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                res.append(sum(nums[i:j+1]))
        return max(res)

## brute force
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                res.append(total)
        return max(res)

