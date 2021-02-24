class Solution:
    def climbStairs(self, n: int) -> int:   
        if n<=3: return n
        x,y=2,3
        for i in range (4,n):
            t=y
            y+=x
            x=t
        return x+y