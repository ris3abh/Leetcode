class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        t = [[1]*i for i in range(1,numRows+1)]
        for i in range(1,numRows):
            for j in range(1,len(t[i-1])):
                t[i][j] = t[i-1][j] + t[i-1][j-1]
        return(t)