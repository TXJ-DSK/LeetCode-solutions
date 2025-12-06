class Solution:
    def magicalString(self, n: int) -> int:
        # Base case: if n is 0, return 0
        if n == 0:
            return 0
      
        # Initialize the magical string with the first three elements
        # The magical string starts as: 1, 2, 2, ...
        magical_string = [1, 2, 2]
      
        # Index pointer to track which element determines the next group's count
        # Starting from index 2 (third element)
        group_count_index = 2
      
        # Generate the magical string until we have at least n elements
        while len(magical_string) < n:
            # Get the previous element to determine what the next element should be
            previous_element = magical_string[-1]
          
            # The next element alternates between 1 and 2
            # If previous was 1, current is 2; if previous was 2, current is 1
            current_element = 3 - previous_element
          
            # The number of times to append the current element is determined by
            # the value at the current group_count_index position
            repeat_count = magical_string[group_count_index]
          
            # Append the current element 'repeat_count' times to the magical string
            magical_string.extend([current_element] * repeat_count)
          
            # Move to the next position for determining group counts
            group_count_index += 1
      
        # Count the number of 1s in the first n elements of the magical string
        return magical_string[:n].count(1)
