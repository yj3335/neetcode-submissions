class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left, right = 0,1
        collisions = 0
        while right < len(asteroids) or collisions != 0:
            if right >= len(asteroids):
                left = 0
                right = 1
                collisions = 0
                continue
            if (asteroids[left] < 0 and asteroids[right] < 0) or (asteroids[left] > 0 and asteroids[right] > 0) or (asteroids[left] < 0 and asteroids[right] > 0):
                left += 1
                right += 1                
            elif abs(asteroids[left]) == abs(asteroids[right]):
                asteroids.pop(right)
                asteroids.pop(left)
                collisions += 1
            else:
                if abs(asteroids[left]) > abs(asteroids[right]):
                    asteroids.pop(right)
                    collisions += 1
                else:
                    asteroids.pop(left)
                    collisions += 1
        return asteroids        
