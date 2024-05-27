class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        d = []
        for i in range(1, len(nums)+1):
            if len(nums) % i == 0:
                d.append(nums[i-1]  *  (nums[i-1]))
        return (sum(d))
