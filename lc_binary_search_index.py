class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(0,len(nums)-1, nums, target)
    
    def binary_search(self, start, end, nums, target):
        if start >= end:
            if nums[start] == target:
                return start
            else:
                if nums[start] < target:
                    return start + 1
                else:
                    return start
                
        m = int((end-start)/2) + start
        if target == nums[m]:
            return m
        elif target > nums[m]:
            index = self.binary_search(m+1, end, nums, target)
            return index
        else:
            index = self.binary_search(0, m-1, nums, target)
            return index
        