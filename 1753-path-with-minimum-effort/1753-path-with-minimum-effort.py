import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m=len(heights)
        n=len(heights[0])
        ref = [[False for i in range(n)] for j in range(m)]
        q=[]
        heapq.heappush(q,(0,0,0))
        while len(q) > 0:
            cur = heapq.heappop(q)
            if ref[cur[1]][cur[2]]:
                continue
            if cur[1] == m-1 and cur[2] == n-1:
                return cur[0]
            ref[cur[1]][cur[2]] = True
            for x1 , y1 in [(-1,0),(1,0),(0,-1),(0,1)]:
                x,y = cur[1]+x1,cur[2]+y1
                if 0<=x<m and 0<=y<n and not ref[x][y]:
                    heapq.heappush(q,(max(cur[0], abs(heights[x][y]-heights[cur[1]][cur[2]])), x, y))
        return -1
