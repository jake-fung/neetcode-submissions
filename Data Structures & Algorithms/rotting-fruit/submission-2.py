class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1,0), (1,0), (0,-1), (0,1)]
        fresh = 0
        time = 0

        # find all rotten cell first
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 2):
                    q.append((r,c))
                elif (grid[r][c] == 1):
                    fresh += 1
                    
        
        # run bfs from each rot orange simultaneously, add one to each layer
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        q.append((r+dr, c+dc))
                        grid[r+dr][c+dc] = 2
                        fresh -= 1
            time += 1
        
        # if there are fresh oranges left, return -1
        if fresh > 0: return -1
        
        return time
