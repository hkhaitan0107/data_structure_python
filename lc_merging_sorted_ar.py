class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        k = 0
        while j < m and k<n:
            if nums1[j+k] <= nums2[k]:
                j += 1
            else:
                nums1.insert(j+k, nums2[k])
                k += 1
                nums1.pop()
                
        while k < n:
            nums1[j+k] = nums2[k]
            k += 1
            
            