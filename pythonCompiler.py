from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []

        while matrix:
            if matrix and matrix[0]:
                ret += matrix.pop(0)
            
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            if matrix:
                ret += (matrix.pop()[::-1])

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
 
        return ret


solution = Solution()
res = solution.spiralOrder([[3],[2]])
print(res)

