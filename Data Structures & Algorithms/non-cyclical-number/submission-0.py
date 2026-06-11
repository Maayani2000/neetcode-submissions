class Solution:
    def sum_square_digits(self, n: int) -> int:
        sum_square = 0
    
        while n > 0:
            sum_square += (n % 10) ** 2
            n = n // 10
            
        return sum_square

    def isHappy(self, n: int) -> bool:
        # A set to keep track of numbers we have already seen
        seen = set()
        
        while n != 1:
            # If we see a number again, it means we are in an infinite loop!
            if n in seen:
                return False
                
            # Add the current number to our history
            seen.add(n)
            
            # Update n to be the sum of squares of its digits
            n = self.sum_square_digits(n)
            
        return True