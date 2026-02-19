class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        movement = 0
        i = 0
        while (i < len(points)):
            curr = points[i]
            next = points[i]
            
            if i + 1 < len(points):
                next = points[i + 1]
            
            currX = curr[0]
            currY = curr[1]

            nextX = next[0]
            nextY = next[1]

            while (currX != nextX or currY != nextY):

                if (currX < nextX):
                    currX += 1
                elif (currX > nextX):
                    currX -= 1
                

                if (currY < nextY):
                    currY += 1
                elif (currY > nextY):
                    currY -= 1
                
                movement += 1

            i += 1
        
        return movement

