class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for idx_row, row in enumerate(grid):
            for idx_tile, tile in enumerate(row):
                if tile == 1:
                    print(idx_tile, idx_row)
                    # Up
                    if idx_row == 0 or grid[idx_row - 1][idx_tile] == 0:
                        perimeter += 1
                    # Down
                    if idx_row + 1 == len(grid) or grid[idx_row + 1][idx_tile] == 0:
                        perimeter += 1
                    # Right
                    if idx_tile + 1 == len(row) or row[idx_tile + 1] == 0:
                        perimeter += 1
                    # Left
                    if idx_tile == 0 or row[idx_tile - 1] == 0:
                        perimeter += 1
        return perimeter