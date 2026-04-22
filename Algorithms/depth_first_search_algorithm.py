def dfs(adj_matrix, start_node):
    n = len(adj_matrix)
    result = []
    visited = [False] * n
    stack = [start_node]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            for neighbor in range(n):
                if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
    return result
