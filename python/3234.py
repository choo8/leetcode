class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # last_zero[i] is the position of "0" closest to s[i]
        last_zero = [-1] * (n + 1)
        for i in range(n):
            # See "0"
            if i == 0 or s[i - 1] == "0":
                last_zero[i + 1] = i
            # See "1"
            else:
                last_zero[i + 1] = last_zero[i]

        num_substrings = 0
        # Loop over all possible ending index of substring
        for i in range(1, n + 1):
            num_zeros = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and num_zeros * num_zeros <= n:
                num_ones = (i - last_zero[j]) - num_zeros
                if num_zeros * num_zeros <= num_ones:
                    num_substrings += min(j - last_zero[j], num_ones - (num_zeros * num_zeros) + 1)
                # Go to the next last seen "0"
                j = last_zero[j]
                num_zeros += 1

        return num_substrings
    

if __name__ == "__main__":
    solution = Solution()

    s = "00011"
    assert solution.numberOfSubstrings(s) == 5

    s = "101101"
    assert solution.numberOfSubstrings(s) == 16
