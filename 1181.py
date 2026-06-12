import sys
input = sys.stdin.read

def solve():
    lines = input().splitlines()
    if not lines:
        return
    
    n = int(lines[0])
    words = list(set(lines[1:n+1]))
    words.sort(key=lambda x: (len(x), x))
    for word in words:
        print(word)

if __name__ == "__main__":
    solve()