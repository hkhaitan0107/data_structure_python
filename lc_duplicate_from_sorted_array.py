class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        while k < len(nums)-1:
            if nums[k] == nums[k+1]:
                nums.pop(k)
                continue
            else:
                k += 1
            
        return len(nums)
    