def adjacency_list_to_matrix(adj_list):
    nodes = list(adj_list.keys())
    n = len(nodes)

    adj_matrix = [[0] * n for _ in range(n)]

    for i, node in enumerate(nodes):
        for neighbor in adj_list[node]:
            j = node.index(neighbor)
            adj_matrix[i][j] = 1
    for row in adj_matrix:
        print(row)

    return adj_matrix

