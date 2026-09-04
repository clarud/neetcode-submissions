class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 0, 0 - > 0, 1
        # 0, 1 -> 1, 1
        # 1, 1 -> 1, 0
        # 1, 0 -> 0, 0
        n = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = (matrix[j][i], matrix[i][j])
        
        for row in range(n):
            matrix[row].reverse()