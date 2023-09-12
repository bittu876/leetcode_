class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ""
        if len(s) < len(t):
            nums1= list(s)
            nums2 =list(t)
        else:
            nums1 = list(t)
            nums2 = list(s)
        i = 0
        while i < len(nums1):
            if nums1[i]  in nums2:
                nums2.remove(nums1[i])
                nums1.remove(nums1[i])   
                i = i -1
            i = i + 1
        res = nums1 + nums2
        ref= "".join(res)
        return ref
            

        