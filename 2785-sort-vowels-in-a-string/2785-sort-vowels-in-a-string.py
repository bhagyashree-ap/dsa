class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        sorted_vowels = sorted(c for c in chars if c in vowels)  #sorting vowels
        j = 0

        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = sorted_vowels[j]    #replacing vowels
                j += 1

        return "".join(chars)