from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []

        while matrix:
            # 1) add first list of matrix to the ret list
            ret += matrix.pop(0)

            # 2) add last element of all lists
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            # 3) add last list in reverse
            if matrix:
                ret += matrix.pop()[::-1]
            
            # 4) add first element in reverse of all lists
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))

        return ret


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

solution = Solution()
res = solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
res = solution.spiralOrder([[3],[2]])

print(res)
