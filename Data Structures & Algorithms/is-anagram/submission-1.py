from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if 's' and 't' are anagrams in O(n) time and O(1) space.

        How it works:
        1. Length Check (Early Exit): If lengths differ, they can't be anagrams.
        2. Frequency Counting: Counter(s) creates a map of character frequencies.
           Example: "anagram" -> {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        3. Comparison: Compares frequency maps. Returns True if identical.
        """
        # Quick check: Anagrams must have the exact same length
        if len(s) != len(t):
            return False
            
        # Compare character frequency distributions
        return Counter(s) == Counter(t)