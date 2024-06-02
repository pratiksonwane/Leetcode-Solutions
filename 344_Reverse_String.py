class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        c = len(s)-1
        e = 0 
        for i in range(0, len(s)):
            if e == len(s)//2:
                break
            e+=1
            d = ""
            d = s[i]
            s[i] = s[c]
            s[c] = d
            c-=1
            
        print(s) 
