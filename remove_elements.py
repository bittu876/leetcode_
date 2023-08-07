#Remove Element
#https://leetcode.com/problems/remove-element/submissions/
def removeElement(nums,val):
    """
    :type nums: List[int]
    :rtype: int
    """
    i=0
    while i< len(nums):
        if nums[i]==val:
            nums.remove(val)
            i-=1
        i+=1
    return nums
if __name__=="__main__":
    val=0
    nums=[0,0,5,6,7,3,8,9,3,0,0,7,0]
    result=removeElement(nums,val)
    print(f"after removing {val} list is {nums}".format(val,result))
