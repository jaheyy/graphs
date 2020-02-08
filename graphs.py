def create_adjacency_matrix(vec_num, edges, directed=True):
    matrix = []
    if directed:
        for i in range(vec_num):
            matrix.append([])
            for j in range(vec_num):
                if [i, j] in edges:
                    matrix[i].append(1)
                else:
                    matrix[i].append(0)
    else:
        for i in range(vec_num):
            matrix.append([])
            for j in range(vec_num):
                matrix[i].append(0)
        for edge in edges:
            x = edge[0]
            y = edge[1]
            matrix[x][y] = 1
            matrix[y][x] = 1
    return matrix
    
def create_incidence_matrix(vec_num, edges, directed=True):
    matrix = []
    if directed:
        for i in range(vec_num):
            matrix.append([])
            for j in range(len(edges)):
                if i == edges[j][0]:
                    matrix[i].append(1)
                elif i == edges[j][1]:
                    matrix[i].append(-1)
                else:
                    matrix[i].append(0)
    else:
        for i in range(vec_num):
            matrix.append([])
            for j in range(len(edges)):
                if i == edges[j][0] or i == edges[j][1]:
                    matrix[i].append(1)
                else:
                    matrix[i].append(0)
    return matrix
        
def create_adjacency_list(vec_num, edges, directed=True):
    matrix = []
    if directed:
        print("directed")
        for i in range(vec_num):
            matrix.append([])
            for edge in edges:
                if i == edge[0]:
                    matrix[i].append(edge[1])
    else:
        print("undirected")
        for i in range(vec_num):
            matrix.append([])
            for edge in edges:
                if i == edge[0]:
                    matrix[i].append(edge[1])
                elif i == edge[1]:
                    matrix[i].append(edge[0])
    return matrix
