class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        if (grid is None):
            return 0

        rows = len(grid)
        cols = len(grid[0])

        def get_neighbor(coord):
            res = []
            r, c = coord
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    res.append((nr, nc))
            
            return res
        
        def dfs(coord):
            r, c = coord
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"

            for neighbor in get_neighbor(coord):
                dfs(neighbor)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs((r, c))
                    count += 1
        
        return count