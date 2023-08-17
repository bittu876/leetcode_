#Search Insert Position
#https://leetcode.com/problems/search-insert-position/description/
def searchInsert( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    res=0
    for i in range(len(nums)):
        if i+1==len(nums):
            res=i+1
        if nums[i]==target :
            res=i
            break
        if nums[i]>target:
            res=i
            break
    return res
if __name__=="__main__":
    nums=[1,4,6,8,9,10]
    target=7
    result=searchInsert( nums, target)
    print(f"the index of {target} may be {result}".format(target,result))
