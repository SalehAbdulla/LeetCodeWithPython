
points = [[1,1],[3,4],[-1,0]]

movement = 0

currX, currY = points.pop()
while (len(points) != 0):
    nextX, nextY = points.pop()
    movement += max(abs(nextX - currX), abs(nextY - currX))

print(movement)