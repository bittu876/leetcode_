class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack=[]
        curMin=nums[0]
        for num in nums:
            while stack and num>=stack[-1][0]:
                stack.pop()

            if stack and num>stack[-1][1]:
                return True

            stack.append([num,curMin])
            curMin=min(curMin,num)
        return False        