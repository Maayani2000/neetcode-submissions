class Solution:
    def str2int(self, s: str) -> int:
        """
        Converts a string of digits to an integer character-by-character:
        1. `ord(char) - ord('0')` converts a single char (e.g., '3') into its integer digit (3) via ASCII distance.
        2. `n * 10` shifts previous digits left (units -> tens -> hundreds), making space to add the new digit.

        Example for "123":
        - '1': 0 * 10 + 1 = 1
        - '2': 1 * 10 + 2 = 12
        - '3': 12 * 10 + 3 = 123
        """
        n = 0
        for char in s:
            # Shift existing number left (x10) and add the new digit (via ASCII offset)
            n = n * 10 + (ord(char) - ord('0'))
        return n

    def multiply(self, num1: str, num2: str) -> str:
        """
            num1: String, represents Non-Negative INTEGERS
            num2: String, represents Non-Negative INTEGERS

            You can not use any built-in library to convert the inputs directly into integers.
            Meaning - cant' do int(num1) * int(num2)
        """
        return str(self.str2int(num1) * self.str2int(num2))
    
