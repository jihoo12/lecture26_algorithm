import sys
input = sys.stdin.read

def solve():
    lines = input().splitlines()
    n = int(lines[0])
    
    students = []
    for i in range(1, n + 1):
        name, kor, eng, math = lines[i].split()
        students.append((name, int(kor), int(eng), int(math)))
        
    students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    
    for student in students:
        print(student[0])

if __name__ == "__main__":
    solve()