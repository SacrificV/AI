from collections import deque

def solve_labyrinth():
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]

    directions = [(-1,0,'U'), (1,0,'D'), (0,-1,'L'), (0,1,'R')]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            if grid[i][j] == 'B':
                end = (i, j)

    queue = deque([start])
    visited = [[False]*m for _ in range(n)]
    parent = [[None]*m for _ in range(n)]

    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            break

        for dx, dy, move in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y, move)
                    queue.append((nx, ny))

    if not visited[end[0]][end[1]]:
        print("NO")
        return

    path = []
    cur = end

    while cur != start:
        px, py, move = parent[cur[0]][cur[1]]
        path.append(move)
        cur = (px, py)

    path.reverse()

    print("YES")
    print(len(path))
    print("".join(path))

solve_labyrinth()

#To run code use this ( delete # before 5 )
#5 8
########
#A..#..#
#.##.#B#
#......#
########
