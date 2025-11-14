from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.freqs = defaultdict(int)
        self.freq_counts = defaultdict(int)

    def add(self, number: int) -> None:
        if self.freqs[number] != 0:
            self.freq_counts[self.freqs[number]] -= 1

        self.freqs[number] += 1
        self.freq_counts[self.freqs[number]] += 1

    def deleteOne(self, number: int) -> None:
        # Does not contain number
        if self.freqs[number] == 0:
            return
        
        # Contains number
        self.freq_counts[self.freqs[number]] -= 1

        self.freqs[number] -= 1
        if self.freqs[number] != 0:
            self.freq_counts[self.freqs[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return True if self.freq_counts[frequency] > 0 else False


if __name__ == "__main__":
    frequency_tracker = FrequencyTracker()
    frequency_tracker.add(3)
    frequency_tracker.add(3)
    assert frequency_tracker.hasFrequency(2)

    frequency_tracker = FrequencyTracker()
    frequency_tracker.add(1)
    frequency_tracker.deleteOne(1)
    assert not frequency_tracker.hasFrequency(1)

    frequency_tracker = FrequencyTracker()
    assert not frequency_tracker.hasFrequency(2)
    frequency_tracker.add(3)
    assert frequency_tracker.hasFrequency(1)
