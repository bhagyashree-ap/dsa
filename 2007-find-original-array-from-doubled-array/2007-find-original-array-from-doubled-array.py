class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if len(changed) % 2:
            return []

        count = Counter(changed)
        original = []

        for num in sorted(changed):
            if count[num] == 0: continue
            if count[2 * num] == 0: return []

            original.append(num)    #adding original number
            count[num] -= 1
            count[2 * num] -= 1

        return original