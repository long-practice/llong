class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bisect_2D(left_r, right_r, left_c, right_c):
            if left_r <= right_r and left_c <= right_c:
                mid_r, mid_c = (left_r + right_r) >> 1, (left_c + right_c) >> 1
                if matrix[mid_r][mid_c] == target:
                    return True
                elif matrix[mid_r][mid_c] < target:
                    return bisect_2D(mid_r + 1, right_r, left_c, right_c) or bisect_2D(left_r, mid_r, mid_c + 1, right_c)
                else:
                    return bisect_2D(left_r, right_r, left_c, mid_c - 1) or bisect_2D(left_r, mid_r - 1, left_c, right_c)
            return False

        return bisect_2D(0, len(matrix) - 1, 0, len(matrix[0]) - 1)