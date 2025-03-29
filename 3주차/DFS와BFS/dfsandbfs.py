def dfs(visit):
    visited[visit] = True
    print(visit, end=' ')
    for i in graph[visit]:
        if not visited[i]:
            dfs(i)



def bfs(visit):
    queue = deque([visit])
    visited[visit] = True
    while queue:
        visit = queue.popleft()
        print(visit, end=' ')
        for i in graph[visit]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
