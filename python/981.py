from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        if len(self.keys[key]) == 0 or timestamp < self.keys[key][0][0]:
            return ""

        left, right = 0, len(self.keys[key]) - 1

        while left < right:
            mid = left + (right - left + 1) // 2

            if self.keys[key][mid][0] == timestamp:
                return self.keys[key][mid][1]
            elif self.keys[key][mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid

        return self.keys[key][left][1]
    

if __name__ == "__main__":
    timeMap = TimeMap()

    timeMap.set("foo", "bar", 1)
    assert timeMap.get("foo", 1) == "bar"
    assert timeMap.get("foo", 3) == "bar"
    timeMap.set("foo", "bar2", 4)
    assert timeMap.get("foo", 4) == "bar2"
    assert timeMap.get("foo", 5) == "bar2"
