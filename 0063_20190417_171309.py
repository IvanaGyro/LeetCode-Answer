class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        obstacleGrid[0][0] = 1

        for x in range(len(obstacleGrid)):
            for y in range(len(obstacleGrid[0])):
                if x == 0 and y == 0:
                    continue
                if obstacleGrid[x][y] == 1:
                    obstacleGrid[x][y] = 0
                else:
                    obstacleGrid[x][y] = 0
                    if x > 0:
                        obstacleGrid[x][y] += obstacleGrid[x - 1][y]
                    if y > 0:
                        obstacleGrid[x][y] += obstacleGrid[x][y - 1]

        return obstacleGrid[-1][-1]  