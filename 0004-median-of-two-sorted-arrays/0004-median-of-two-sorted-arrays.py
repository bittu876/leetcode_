class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        import math
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=nums1+nums2
        nums3.sort()
        print(1.0/2.0)
        if  len(nums3)%2==0:
            return ((float(nums3[len(nums3)//2])+float(nums3[(len(nums3)/2)-1]))/2)
        else:
            return nums3[len(nums3)//2]
