class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1]*n
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a,b):
            rootX = find(a)
            rootY = find(b)

            if rootX==rootY:
                return False

            if size[rootX]>=size[rootY]:
                parent[rootY]=parent[rootX]
                size[rootX]+=size[rootY]
            else:
                parent[rootX]=parent[rootY]
                size[rootY]+=size[rootX]
            return True
            
        components = n
        for u, v in edges:
            if union(u, v):
                components -= 1
        return components