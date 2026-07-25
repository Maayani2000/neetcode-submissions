class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        prev = 0 
        curr = 1 
        
        # we already know the calculation for 0 and 1, hence starting with 2
        for _ in range(2, n + 1): 
            next_num = prev + curr 
            prev = curr            
            curr = next_num        
            
        return curr
