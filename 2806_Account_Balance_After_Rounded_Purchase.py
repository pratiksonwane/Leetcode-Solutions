class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 == 0:
            return 100 - purchaseAmount
        else:
            if purchaseAmount % 10 >= 5:
                for i in range(purchaseAmount, 101):
                    purchaseAmount+=1
                    if (purchaseAmount) % 10 == 0:
                        return 100 - purchaseAmount
            else:
                if (purchaseAmount % 5) < 5:
                    purchaseAmount = purchaseAmount - purchaseAmount % 5
                    return 100 - purchaseAmount
