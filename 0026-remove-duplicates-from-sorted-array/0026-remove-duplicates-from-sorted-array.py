class Solution(object):
   def removeDuplicates(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        for i in range(len(nums)):
            if i+1 < len(nums):
                j=i+1
        
                while j<len(nums):
                    if nums[i]==nums[j]:
                        nums.remove(nums[j]) 
                        j-=1
                    j+=1
                      
        k=len(nums)     
        return k 