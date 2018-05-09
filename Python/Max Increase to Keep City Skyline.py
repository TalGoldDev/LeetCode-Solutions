"""
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there.
We are allowed to increase the height of any number of buildings, by any amount
(the amounts can be different for different buildings).
Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right,
must be the same as the skyline of the original grid.
A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance.

What is the maximum total sum that the height of the buildings can be increased?

"""
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # defining paramters.
        gridRows = len(grid)
        gridCols = len(grid[0])
        maxSum = 0;
        frontView = [0] * gridCols
        sideView = [0] * gridRows

        current_max_value = 0
        
        # going over the grid and searching for the highest number for each row.
        for i in range(gridRows):
            current_max_value = 0
            for j in range(gridCols):
                if current_max_value < grid[i][j]:
                    current_max_value = grid[i][j]

            sideView[i] = current_max_value

        # going over the grid and searching for the highest number for each column.
        for i in range(gridCols):
            current_max_value = 0
            for j in range(gridRows):
                if current_max_value < grid[j][i]:
                    current_max_value = grid[j][i]

            frontView[i] = current_max_value

        # calculating the maximum total sum that the height of the buildings can be increased.
        for i in range(gridRows):
            for j in range(gridCols):
                if frontView[j] <= sideView[i]:
                    maxSum += frontView[j] - grid[i][j]
                    continue
                maxSum += sideView[i] - grid[i][j]

        return maxSum
