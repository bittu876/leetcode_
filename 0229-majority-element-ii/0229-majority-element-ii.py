class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = len(nums)//3
        if x == 0:
            return list(set(nums))
        ref = {}
        res=[]
        for i in nums:
            if i in ref.keys():
                ref[i] += 1
                if ref[i] > x and i not in res:
                    res.append(i)
            else:
                ref[i] = 1
            print(ref)
        return res

                    

        