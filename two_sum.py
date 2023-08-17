#Two Sum
#https://leetcode.com/problems/two-sum/description/
def twoSum(nums,target):
    b=[]
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
            
                b.append(i)
                b.append(j)
    return b 
if __name__=="__main__":
    nums=[2,4,6,7,1,8]
    target=13
    sum=twoSum(nums,target)
    print("array is ",nums)
    print(f"indexs of numbers who's sum is {target} are {sum}".format(target,sum))
 
