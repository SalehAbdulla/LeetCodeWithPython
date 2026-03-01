from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        visited = set()
        

        rows = len(grid)
        cols = len(grid[0])


        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visited.add((r, c))

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1' and (nr, nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr, nc))


        count = 0
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == '1' and (r, c) not in visited):
                    bfs(r, c)
                    count += 1



        return count


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

s = Solution()

print(s.numIslands(grid)) #1


