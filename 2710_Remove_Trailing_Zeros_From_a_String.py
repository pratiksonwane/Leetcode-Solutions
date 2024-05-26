class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = (num[:: -1])
        return str(int(num))[:: -1] 
