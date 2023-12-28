from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        layers = n // 2
        
        for layer in range(layers):
            first = layer
            last = n - layer - 1
            
            for i in range(first, last):
                offset = i - first
                top = matrix[first][i]  # Save top element
                
                # Left -> Top
                matrix[first][i] = matrix[last - offset][first]
                
                # Bottom -> Left
                matrix[last - offset][first] = matrix[last][last - offset]
                
                # Right -> Bottom
                matrix[last][last - offset] = matrix[i][last]
                
                # Top -> Right
                matrix[i][last] = top  # Assign the saved top element to the right