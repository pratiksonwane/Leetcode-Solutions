class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        d  = []
        while len(nums) > 0:
            d.append( ( min(nums) + max(nums) ) / 2 )
            nums.remove(max(nums))
            nums.remove(min(nums))
        return ( len(set(d)))
        
