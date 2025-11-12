class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        num_strs = len(strs)
        dp = [[[0 for _ in range(num_strs + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

        for k, s in enumerate(strs, 1):
            zeros_count = s.count("0")
            ones_count = s.count("1")
        
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[i][j][k] = dp[i][j][k - 1]

                    if i >= zeros_count and j >= ones_count:
                        dp[i][j][k] = max(dp[i - zeros_count][j - ones_count][k - 1] + 1, dp[i][j][k])

        return dp[m][n][num_strs]


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
