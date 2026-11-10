class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        firstrow = 0 
        lastrowindex = R - 1
        
        while firstrow <= lastrowindex:
            mrow = (firstrow + lastrowindex) // 2
            if target > matrix[mrow][0] and target > matrix[mrow][C-1]:
                firstrow = mrow + 1
            elif target < matrix[mrow][0]:
                lastrowindex = mrow - 1
            else:
                for i in range(C):
                    if matrix[mrow][i] == target:
                        return True
                return False 
        return False
        
       


