import sys

fast_print = sys.stdout.write
goal = 2
road = 1
water = 0

n, m = map(int, input().split())

graph_input = list()
distance = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
queue = list()


def init(n, m_list):
    for i in range(m):
        if m_list[i] != road:
            distance[n][i] = 0
            visited[n][i] = True

            if m_list[i] == goal:
                queue.append((n, i))


def is_reachable(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False
    return not visited[i][j]


def explore(i, j):
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_i = i + di
        new_j = j + dj
        if is_reachable(new_i, new_j):
            distance[new_i][new_j] = distance[i][j] + 1
            visited[new_i][new_j] = True
            queue.append((new_i, new_j))

    return


for i in range(n):
    graph_input.append(list(map(int, input().split())))
    init(i, graph_input[i])

while queue:
    i, j = queue.pop(0)
    explore(i, j)


fast_print('\n'.join([' '.join(map(str, row)) for row in distance]))