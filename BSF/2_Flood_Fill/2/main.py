# Flood_Fill problem
# Simulates ms paint, once you pick a color, and click on a cell, 
# any cell that matches, will get the color
# if the color as same as it is, then no need to do it


## Only spread through cells that are connected and same color

from typing import List
from collections import deque

def Flood_full(image: List[List[int]], r:int, c:int, replacement: int) -> List[List[int]]:

    rows, cols = len(image), len(image[0])
    original_color = image[r][c]
    
    if image[r][c] == replacement:
        return image

    image[r][c] = replacement
    
    q = deque([(r, c)])

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while (q):
        row, col = q.popleft()

        for dr, dc in directions:
            nr, nc = dr+row, dc+col

            if 0 <= nr < rows and 0 <= nc < cols:
                if image[nr][nc] == original_color:
                    image[nr][nc] = replacement
                    q.append((nr, nc))

    return image
