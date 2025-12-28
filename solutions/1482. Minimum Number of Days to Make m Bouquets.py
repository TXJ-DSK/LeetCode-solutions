class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        if k == 1:
            return sorted(bloomDay)[m-1]

        def feasible(days: int) -> bool:
            """
            Check if we can make m bouquets after waiting 'days' days.
            Returns True if we can make at least m bouquets.
            """
            bouquets_made = 0
            consecutive_bloomed = 0

            for bloom_day in bloomDay:
                if bloom_day <= days:
                    consecutive_bloomed += 1
                    if consecutive_bloomed == k:
                        bouquets_made += 1
                        consecutive_bloomed = 0
                else:
                    consecutive_bloomed = 0

            return bouquets_made >= m

        # Binary search using the template pattern
        left, right = min(bloomDay), max(bloomDay)
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2

            if feasible(mid):
                first_true_index = mid
                right = mid - 1  # Search for earlier day
            else:
                left = mid + 1

        return first_true_index
