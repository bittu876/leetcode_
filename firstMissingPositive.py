def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        x=0
        for i in range(len(nums)):
            if nums[i]>0:
                x=i
                break
        if nums[x]!=1:
            return 1   
        for i in range(x+1,len(nums)+1) :
            if i<len(nums):
               if nums[x]+1!=nums[i] and nums[i]>nums[x]+1 :
                  return (nums[x]+1)
            x+=1  
        return nums[len(nums)-1]+1
nums=[0,2,2,1,1]
n=firstMissingPositive(nums)
print(n)
