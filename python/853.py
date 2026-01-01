class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time = [(target - p) / s for p, s in zip(position, speed)]

        fleets = []
        for p, t in sorted(zip(position, time), key=lambda x: x[0], reverse=True):
            if len(fleets) == 0 or t > fleets[-1][-1]:
                fleets.append((p, t))

        return len(fleets)
    

if __name__ == "__main__":
    solution = Solution()

    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    assert solution.carFleet(target, position, speed) == 3

    target = 10
    position = [3]
    speed = [3]
    assert solution.carFleet(target, position, speed) == 1

    target = 100
    position = [0,2,4]
    speed = [4,2,1]
    assert solution.carFleet(target, position, speed) == 1
