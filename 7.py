#Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        upperLimit = (2 ** 31) - 1
        lowerLimit = (-2 ** 31)

        if x >= 0:
            x = str(x)
            res = 0 if (int(x[::-1]) > upperLimit) else (int(x[::-1]))
            return res
        
        x = str(abs(x))
        res = 0 if (-int(x[::-1]) < lowerLimit) else -int(x[::-1])
        return res