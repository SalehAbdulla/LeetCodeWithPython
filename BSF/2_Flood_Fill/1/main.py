from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], r: int, c: int, replacement: int) -> List[List[int]]:    
        num_rows, num_cols = len(image), len(image[0])
        original_color = image[r][c]

        if original_color == replacement:
            return image

        queue = deque([(r, c)])
        image[r][c] = replacement 

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    if image[nr][nc] == original_color:
                        image[nr][nc] = replacement
                        queue.append((nr, nc))

        return image
