class Solution:
    def asteroidCollision(self, asteroids):
        finalAsteroids = []
        for asteroid in asteroids:
            if asteroid > 0:
                finalAsteroids.append(asteroid)
            else:
                result = asteroid
                while result < 0:
                    if len(finalAsteroids) == 0 or finalAsteroids[-1] < 0:
                        finalAsteroids.append(asteroid)
                        break

                    result = asteroid + finalAsteroids[-1]
                    if result <= 0:
                        finalAsteroids.pop()

        return finalAsteroids