class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0 for _ in temperatures]
        stack = []

        for idx, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < t:
                popped_idx, _ = stack.pop()
                answer[popped_idx] = idx - popped_idx
            stack.append((idx, t))

        return answer
    

if __name__ == "__main__":
    solution = Solution()

    temperatures = [73,74,75,71,69,72,76,73]
    assert solution.dailyTemperatures(temperatures) == [1,1,4,2,1,1,0,0]

    temperatures = [30,40,50,60]
    assert solution.dailyTemperatures(temperatures) == [1,1,1,0]

    temperatures = [30,60,90]
    assert solution.dailyTemperatures(temperatures) == [1,1,0]
