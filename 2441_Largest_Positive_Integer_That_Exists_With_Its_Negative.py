class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        p = []
        n = []
        res = []
        for i in nums:
            if i > 0:
                p.append(i)
            else:
                n.append(abs(i))
        for i in p:
            if i in n:
                res.append(i)
        if len(res)>=1:
            return max(res)
        else:
            return -1
