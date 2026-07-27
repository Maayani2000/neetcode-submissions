class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # go through every single asteroid in the input
        for a in asteroids:
            """
            collisions handling:
                must check that:
                    1. the stack is not empty
                    2. the current asteroid we're visiting is negative -> we're moving left
                    3. the asteroid on the top of the stack is positive -> we're moving right

                    if all these are true - we're definitely getting a collision
            """ 
            while stack and a < 0 and stack[-1] > 0:
                # the result of the collision
                diff = a + stack[-1]

                # asteroid a is going to win - pop the top of the stack
                if diff < 0: 
                    stack.pop()

                # the top of the stack is going to win -> a is going to be destroyed
                elif diff > 0:
                    a = 0

                # a is equal to the top of the stack -> both will be destroyed
                else:
                    a = 0
                    stack.pop()
            
            # if a is still positive or negative - we'll add it to the stack.
            # if this is 0 we won't add it
            if a:
                stack.append(a)

        # return whatever is left in the stack - the remaining asteroids
        return stack