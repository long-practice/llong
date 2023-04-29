class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        answer = 0
        dist = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        def get_dist(r, c):
            if not dist[r][c]:
                dist[r][c] = 1
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] > matrix[r][c]:
                        dist[r][c] = max(dist[r][c], get_dist(nr, nc) + 1)
            return dist[r][c]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if not dist[row][col]:
                    dist[row][col] = get_dist(row, col)
                answer = max(answer, dist[row][col])
        return answer