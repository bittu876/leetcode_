class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        low = 0 
        high = len(nums)-1
        while low <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                j = mid
                i = mid 
                if len(nums) == 1:
                    return [i,j]
                while i>=0:
                    if nums[i] == target:
                        i -= 1
                    else:break
                while j<=len(nums)-1 :
                    if nums[j] == target:
                        j += 1
                    else:break
                res.append(i+1)
                res.append(j-1)
                return res
            elif target < nums[mid] :
                high = mid-1
            else:
                low = mid+1
        else:
            return ([-1,-1])