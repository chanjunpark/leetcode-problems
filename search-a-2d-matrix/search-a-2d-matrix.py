class Solution: 
            
    def binary_search(self, pool: List[int], left: int, right: int, target: int) -> bool:
        middle = (left+right)//2
        try:
            if left > right:
                return False
            if target == pool[middle]:
                return True
            else:
                if target > pool[middle]:
                    key = self.binary_search(pool, middle+1, right, target)
                    return key
                else:
                    key = self.binary_search(pool, left, middle-1, target)
                    return key
        except:
            return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        if len(matrix) == 1:
            result = self.binary_search(matrix[0], 0, len(matrix[0]), target)
            return result
        else :
            for i in range(1,len(matrix)):
                if target >= matrix[i-1][0] and target<matrix[i][0]:
                    row = i-1
                    break
                row = len(matrix) - 1
            if row == -1:
                return False
            else:
                result = self.binary_search(matrix[row], 0, len(matrix[row]), target)
                return result