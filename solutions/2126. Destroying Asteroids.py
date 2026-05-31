# O(NlogN) time, O(1) space

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a_mass in asteroids:
            if a_mass > mass:
                return False
            mass += a_mass
        return True
