class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        maxx = max(nums)
        d = []
        for i in range(1, maxx+1):
            d.append(i)
        d.append(max(nums))
        if nums == d:
            return True
        
