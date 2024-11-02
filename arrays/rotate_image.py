'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix[0])):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverse_rows(matrix):
            for r in range(len(matrix)):
                left, right = 0, len(matrix) - 1
                while left < right:
                    matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                    left += 1
                    right -= 1

        transpose(matrix)
        reverse_rows(matrix)
