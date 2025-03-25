import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def divide(x, y, size):
    global white, blue
    current = paper[x][y]
    all_same = True
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != current:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        if current == 0:
            white += 1
        else:
            blue += 1
    else:
        half = size // 2
        divide(x, y, half)                   
        divide(x, y + half, half)            
        divide(x + half, y, half)            
        divide(x + half, y + half, half)     

divide(0, 0, n)
print(white)
print(blue)
