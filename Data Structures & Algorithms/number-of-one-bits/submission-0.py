from collections import Counter

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        For counting 0's - 
            # Total bits minus the 1s equals the 0s
            zeros = number.bit_length() - number.bit_count()
        """
        return n.bit_count()