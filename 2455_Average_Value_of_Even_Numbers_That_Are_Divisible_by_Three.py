class Solution:
    def averageValue(self, nums: List[int]) -> int:
        d = []
        for i in nums:
            if i % 2 == 0 and  i % 3 == 0:
                d.append(i)
        if len(d)>0:
            return  (int( sum(d) / len(d) ))
        else:
            return 0
