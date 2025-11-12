class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            zeros_count = s.count("0")
            ones_count = s.count("1")
        
            for i in range(m, zeros_count - 1, -1):
                for j in range(n, ones_count - 1, -1):
                    dp[i][j] = max(dp[i - zeros_count][j - ones_count] + 1, dp[i][j])

        return dp[m][n]


if __name__ == "__main__":
    solution = Solution()

    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    assert solution.findMaxForm(strs, m, n) == 4

    strs = ["10","0","1"]
    m = 1
    n = 1
    assert solution.findMaxForm(strs, m, n) == 2
