class Solution:
    def __init__(self):
        self._max = 0
        self._res = None
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        rst, n =[], len(nums)
        self._max, self._rest = 0, None
        dp = [[0]*n for _ in range(n)]
        
        for r in range(n):
            for c in range(r,n):
                if r == c:
                    dp[r][c] = nums[c]
                if c > r:
                    dp[r][c] = dp[r][c-1]/nums[c]
                    
        self.backtrack(nums, dp, rst, 0)
        return self._res
    def backtrack(self, nums, dp, rst, start):
        if start == len(nums):
            print(rst)
            l = rst[0]
            v = dp[l[0]][l[1]]
            for i in range(1, len(rst)):
                l = rst[i]
                v /= dp[l[0]][l[1]]
            if v > self._max:
                self._max = v
                self._res = "/".join([self.expr(nums,x) for x in rst])
        else:
            for i in range(start, len(nums)):
                if rst and self.length(rst[-1]) == 0 and start==i:
                    continue
                self.backtrack(nums,dp, rst+[[start,i]], i+1)
                
    def length(self, l):
        return l[1]-l[0]
    def expr(self, nums, l):
        print(l)
        if self.length(l) == 0:
            return str(nums[l[0]])
        else:
            if l[0] == 0 and l[1] == len(nums)-1:
                return "/".join([str(nums[i]) for i in range(l[0],l[1]+1)])
            else:
                return "({})".format("/".join([str(nums[i]) for i in range(l[0],l[1]+1)]))
            
if __name__ == "__main__":
    s = Solution()
    print(s.optimalDivision([1000,100,10,2]))
    print(s.optimalDivision([3,2]))
    print(s.optimalDivision([10,5,2]))
    print(s.optimalDivision([10000,1,2,5]))
    print(s.optimalDivision([2,5,10,100]))
