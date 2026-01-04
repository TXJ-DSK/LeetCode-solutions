class Solution:
    def getFactor(self, num: int) -> Set[int]:
        if num <= 1:
            return set()
        elif num < 4:
            return set([num])
        else:
            result = []
            sqroot = math.floor(math.sqrt(num))
            for i in range(2, sqroot + 1):
                if num % i == 0:
                    result.append(i)
                    result.append(num//i)
            if num == sqroot ** 2:
                result.pop(-1)
            result.append(num)
            return set(result)

    def largestComponentSize(self, nums: List[int]) -> int:
        class Component:
            self.factors = set()
            self.count = 0

            def __init__(self, factors, count=1):
                self.factors = factors
                self.count = count
            def __repr__(self):
                return f"count={self.count},factors={self.factors}"
            def __str__(self):
                return self.__repr__()
        components = [Component(self.getFactor(nums[0]))]
        for num in nums[1:]:
            factors = self.getFactor(num)
            connectables = []
            for c in components:
                cfactors = c.factors
                common = factors & cfactors
                if len(common) > 0:
                    connectables.append(c)
            if len(connectables) == 1:
                connectables[0].count += 1
                connectables[0].factors.update(factors)
            else:
                components = [c for c in components if c not in connectables]
                new_count = 1
                for c in connectables:
                    new_count += c.count
                    factors.update(c.factors)
                components.append(Component(factors, new_count))
        max_count = 1
        for c in components:
            max_count = max(max_count, c.count)
        return max_count
