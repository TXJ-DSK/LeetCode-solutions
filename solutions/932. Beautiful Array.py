class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        """
        Constructs a beautiful array of size n.
        A beautiful array is an array where for every i < j < k,
        nums[j] * 2 != nums[i] + nums[k].
      
        The approach uses divide and conquer:
        - Split the problem into odd and even parts
        - Recursively build beautiful arrays for each half
        - Transform left half to odd numbers (2x - 1)
        - Transform right half to even numbers (2x)
        - Concatenate them (odd + even guarantees no arithmetic progression)
      
        Args:
            n: The size of the beautiful array to generate
          
        Returns:
            A list containing a beautiful permutation of numbers 1 to n
        """
        # Base case: array of size 1 is always beautiful
        if n == 1:
            return [1]
      
        # Recursively build beautiful array for left half (ceiling division)
        # (n + 1) // 2 handles both odd and even n correctly
        left_half = self.beautifulArray((n + 1) // 2)
      
        # Recursively build beautiful array for right half (floor division)
        right_half = self.beautifulArray(n // 2)
      
        # Transform left half elements to odd numbers: 1, 3, 5, 7, ...
        odd_numbers = [x * 2 - 1 for x in left_half]
      
        # Transform right half elements to even numbers: 2, 4, 6, 8, ...
        even_numbers = [x * 2 for x in right_half]
      
        # Combine odd and even parts to form the final beautiful array
        # This works because odd + even can never equal 2 * another_number
        return odd_numbers + even_numbers
