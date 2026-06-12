import sys
input = sys.stdin.read

def solve():
    data = input().split()
    n = int(data[0])
    points = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx+1])
        points.append((x, y))
        idx += 2
    points.sort(key=lambda p: (p[0], p[1]))
    for x, y in points:
        print(f"{x} {y}")

if __name__ == "__main__":
    solve()