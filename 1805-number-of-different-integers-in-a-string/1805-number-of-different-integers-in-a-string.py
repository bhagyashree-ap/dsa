class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        curr = ""

        for ch in word:
            if ch.isdigit():
                curr += ch   #adding digit

            else:
                if curr:
                    nums.add(str(int(curr)))   #removing leading zeros
                    curr = ""

        if curr:
            nums.add(str(int(curr)))   #adding last number

        return len(nums)
        