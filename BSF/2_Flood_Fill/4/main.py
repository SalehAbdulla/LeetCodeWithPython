class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # Simulates the ms paint, color picker, user will click on pixel, and matches colors and share the same color.
        if (len(image) == 0):
            return image

        # if the color picker has the same color as the pixels does, then nothing happens
        if (image[sr][sc] == color):
            return image
        
        orginal_color = image[sr][sc] 
        rows, cols = len(image), len(image[0])
        image[sr][sc] = color

        q = deque([(sr, sc)])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while (q):
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == orginal_color:
                    q.append((nr, nc))
                    image[nr][nc] = color
                
        return image


        