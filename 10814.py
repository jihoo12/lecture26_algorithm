import sys


input = sys.stdin.read

def solve():
    lines = input().splitlines()
    n = int(lines[0])
    members = []
    for i in range(1, n + 1):
        age, name = lines[i].split()
        members.append((int(age), name))
    
    members.sort(key=lambda x: x[0])
    
    for age, name in members:
        print(f"{age} {name}")

if __name__ == "__main__":
    solve() 