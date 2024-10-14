class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))  # 각 노드는 자기 자신을 부모로 가짐
        self.rank = [0] * (n + 1)  # 각 노드의 깊이(rank)를 기록

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # 랭크를 기준으로 더 낮은 트리를 더 높은 트리 밑에 붙임
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1  # 랭크가 같을 때는 rootX를 root로 하고 랭크 증가


def solution(n, lighthouse):
    uf = UnionFind(n)

    # 등대 연결 관계를 기반으로 Union 연산
    for u, v in lighthouse:
        uf.union(u, v)

    # 각 그룹별로 최소한의 노드만 불을 켜기 위해 대표 노드를 찾아야 함
    group_count = {}

    # 각 노드의 루트(대표 노드)를 확인하여 그룹별 카운트
    for i in range(1, n + 1):
        root = uf.find(i)
        if root not in group_count:
            group_count[root] = 0
        group_count[root] += 1

    # 그룹별로 최소한의 노드를 선택해 불을 켬
    answer = 0
    for count in group_count.values():
        answer += (count + 1) // 2  # 최소한의 노드를 켜기 위한 그리디 계산

    return answer


solution(10,[[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]])