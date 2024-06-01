class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
            fuel=0
            while mainTank // 5 > 0:
                mainTank-=5
                fuel+=5
                if additionalTank>=1:
                    mainTank+=1
                    additionalTank-=1
        
            return fuel*10 + mainTank*10
