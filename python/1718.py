class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        if n == 1:
            return [1]

        cur_sequence = [1] * ((2 * n) - 1)
        cur_sequence[0] = n
        cur_sequence[n] = n
        return self._search(1, (1 << (n - 1)), cur_sequence)
    
    def _search(self, idx: int, visited: int, cur_sequence: list[int]) -> list[int]:
        n = (len(cur_sequence) + 1) // 2

        if visited & ((2 ** n) - 1 - 1) == ((2 ** n) - 1 - 1):
            return cur_sequence
        elif idx == len(cur_sequence):
            return []
        else:
            for i in range(n, 1, -1):
                if (visited >> (i - 1)) & 1 == 0 and cur_sequence[idx] == 1 and idx + i < len(cur_sequence) and cur_sequence[idx + i] == 1:
                    visited |= 1 << (i - 1)
                    cur_sequence[idx] = i
                    cur_sequence[idx + i] = i
                
                    candidate = self._search(idx + 1, visited, cur_sequence)
                
                    if candidate:
                        return candidate

                    cur_sequence[idx] = 1
                    cur_sequence[idx + i] = 1
                    visited ^= 1 << (i - 1)
            
            return self._search(idx + 1, visited, cur_sequence)


if __name__ == "__main__":
    solution = Solution()

    n = 3
    assert solution.constructDistancedSequence(n) == [3,1,2,3,2]

    n = 5
    assert solution.constructDistancedSequence(n) == [5,3,1,4,3,5,2,4,2]
