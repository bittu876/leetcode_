class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def check(lst):
            if len(lst) == 1:
                return [lst]
            result = []
            for i in range(len(lst)):
                cur_ele = lst[i]
                cur_lst = lst[:i] + lst[i+1:]
                x = check(cur_lst)
                
                for j in x:
                    result .append([cur_ele]+j)
            return result   
        x = check(nums)
        return x
            


        