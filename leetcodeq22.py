import collections


def criticalConnections(n, connections):
    def makeGraph(connections):
        graph = collections.defaultdict(list)
        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])
        return graph

    graph = makeGraph(connections)
    print(graph)
    connections = set(map(tuple, connections))
    print("connections = ", connections)
    rank = [-2] * n
    print("\nrank = ", rank)

    def dfs(node, depth):
        print("DFS FUNCTION BEGIN ========")
        print("\nnode = ", node)
        print("depth = ", depth)

        print(f"\nrank[{node}] = {rank[node]}")
        print(f"\nif rank[{node}] >= 0: {rank[node] >= 0}")
        if rank[node] >= 0:
            # visiting (0<=rank<n), or visited (rank=n)
            print("RETURN ", rank[node])
            return rank[node]

        rank[node] = depth
        print(f"\nset rank[{node}] = {depth}")
        print("Updated rank = ", rank)

        min_back_depth = n
        print(f"\nset min_back_depth = {n}")

        print("\nFOR LOOP BEGIN")
        for n1 in graph[node]:
            print("\n===================\n")
            print("n1 = ", n1)
            print(f"graph for node {node} : graph[{node}] = {graph[node]}\n")

            print(f"If rank[{n1}] == {depth - 1} : {rank[n1] == depth - 1}")
            if rank[n1] == depth - 1:
                print("CONTINUE\n")
                continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
            
            print("Again call FUNCTION DFS\n")
            print(f"\nback_depth = dfs({n1}, {depth + 1})\n")
            back_depth = dfs(n1, depth + 1)
            print(f"\nback_depth = dfs({n1}, {depth + 1})")
            print("back_depth = ", back_depth)
            
            print(f"if {back_depth} <= {depth} : {back_depth <= depth}")
            if back_depth <= depth:
                connections.discard(tuple(sorted((node, n1))))
                print("connections = ", connections)
            min_back_depth = min(min_back_depth, back_depth)
            print(f"\nset min_back_depth = min({min_back_depth}, {back_depth})")
            print("min_back_depth = ", min_back_depth)
        print("\nEND FOR LOOP")
        rank[node] = n  # this line is not necessary. see the "brain teaser" section below
        print(f"set rank[{node}] = {n}")
        print("rank = ", rank)
        print("\nRETURN ", min_back_depth)
        return min_back_depth

    dfs(0, 0)  # since this is a connected graph, we don't have to loop over all nodes.
    return list(connections)


connections = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3], [2, 6]]
n = 7
print("\n\n", criticalConnections(n, connections))
