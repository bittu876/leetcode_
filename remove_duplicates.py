#Remove Duplicates from Sorted Array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
def removeDuplicates(nums):
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
                    
        
    return nums
if __name__=="__main__":
    
    nums=[0,0,0,1,2,4,6,6,6,7,8,9,9,]
    result=removeDuplicates(nums)
    print("array , after removing duplicates",result)
