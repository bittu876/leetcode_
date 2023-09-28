class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        res=[]
        for i in matrix:
            res += i
        low = 0
        high = len(res)
        print(res)
        while low < high:
            mid = (low + high)//2
            print(mid)
            if res[mid] == target:
                return True
            elif res[mid] < target:
                low = mid+1
            else:
                high = mid
        else:
            return False

        