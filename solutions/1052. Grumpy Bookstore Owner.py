class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_customers = 0
        total_unsatisfied = 0
        for i in range(len(customers)):
            total_customers += customers[i]
            if grumpy[i] == 1:
                total_unsatisfied += customers[i]
        # Use a sliding window to find the maximum number of unsatisfied customers that can be PREVENTED
        window_sum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                window_sum += customers[i]
        max_window = window_sum
        for i in range(minutes, len(customers)):
            if grumpy[i - minutes] == 1:
                window_sum -= customers[i - minutes]
            if grumpy[i] == 1:
                window_sum += customers[i]
            max_window = max(max_window, window_sum)
        return total_customers - total_unsatisfied + max_window
