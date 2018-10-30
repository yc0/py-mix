"""
Given a 2D matrix M X N, support two operations:
Query(row1, col1, row2, col2) such that I get the sum of all numbers in the rectangle ((row1, col1), (row1, col2), (row2, col1), (row2, col2)) and
Update(row, col) to a new number
"""
class Solution(object):
    def __init__(self,V):
        self.input = V
        if V:
            M,N = len(V), len(V[0])
            self.sum = [[0]*N for _ in range(M)]
            self.sum[0][0] = V[0][0]
            self._update()
    def query(self,r1,c1,r2,c2):
        upper, left, joint = 0,0,0
        if r1 > 0:
            upper = self.sum[r1-1][c2]
        if c1 > 0:
            left = self.sum[r2][c1-1]
        if r1 > 0 and c1 > 0:
            joint = self.sum[r1-1][c1-1]
        return self.sum[r2][c2]-upper-left+joint

    def update(self,row,col, val):
        if self.input:
            m,n = len(self.input),len(self.input[0])
            if 0<= row < m and 0 <= col < n:
                self.input[row][col] = val
                self._update(row,col)
    def _update(self,s_r=0,s_c=0):
        V = self.input
        M,N = len(V), len(V[0])
        for r in range(s_r,M):
            for c in range(s_c,N):
                if r == 0 or c == 0:
                    if r == 0:
                        self.sum[0][c] = self.sum[0][c-1]+V[0][c]
                    else:
                        self.sum[r][0] = self.sum[r-1][0]+V[r][0]
                else:       
                    self.sum[r][c] = self.sum[r-1][c]+self.sum[r][c-1]-self.sum[r-1][c-1]+V[r][c]
if __name__ == '__main__':
    s = Solution([
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]
    ])
    print(s.query(1,1,2,2))
    s.update(1,2,7)
    s.update(2,1,0)
    print(s.query(1,1,2,2))