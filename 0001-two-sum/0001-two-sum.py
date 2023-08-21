class Solution:
    def twoSum(self,nums,target):
        b=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                  
                    b.append(i)
                    b.append(j)
        return b 
               