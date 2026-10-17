class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
    
        nums.sort(key=lambda x: (freq[x], -x))  #freq ascending, value descending

        return nums