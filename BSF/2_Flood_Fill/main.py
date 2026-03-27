from collections import deque
from typing import List

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    num_rows, num_cols = len(image), len(image[0])

    def get_neighbors(row: int, col: int, color: int):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < num_rows and 0 <= nc < num_cols:
                if image[nr][nc] == color:
                    yield nr, nc

    def bfs(start_row: int, start_col: int):
        original_color = image[start_row][start_col]
        
        # If the color is already the replacement, no need to proceed
        if original_color == replacement:
            return

        queue = deque([(start_row, start_col)])
        visited = [[False] * num_cols for _ in range(num_rows)]

        image[start_row][start_col] = replacement
        visited[start_row][start_col] = True

        while queue:
            row, col = queue.popleft()

            for nr, nc in get_neighbors(row, col, original_color):
                if not visited[nr][nc]:
                    image[nr][nc] = replacement
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    bfs(r, c)
    return image