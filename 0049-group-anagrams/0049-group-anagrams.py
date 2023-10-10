class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ref = {}
        for i in strs:
            x = str(sorted(i))
            if x in ref.keys():
                ref[x].append(i)
            else:
                ref[x] = [i]
        return ref.values() 
                



        