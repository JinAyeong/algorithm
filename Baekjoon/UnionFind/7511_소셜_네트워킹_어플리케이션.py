import sys
input = sys.stdin.readline

class SNA:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.rank[rootY] += self.rank[rootX]
                self.parent[rootX] = rootY
            else:
                self.rank[rootX] += self.rank[rootY]
                self.parent[rootY] = rootX

def solve():
    n = int(input())
    k = int(input())
    sna = SNA(n)

    for _ in range(k):
        a, b = map(int, input().split())
        sna.union(a, b)

    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        print(1 if sna.find(u) == sna.find(v) else 0)

def main():
    T = int(input())
    for t in range(T):
        print(f'Scenario {t+1}:')
        solve()
        if t != T - 1:
            print()

main()