from sys import stdin
from collections import deque
N = int(stdin.readline())
T = {}
for _ in range(N):
    a, b, c = stdin.readline().rstrip().split()
    t = [b, c, '.']
    T[a] = t

R = [''] * 3
    
def traverse(a:str):
    if a == '.' : return
    for i in range(3):
        R[i]+=a
        traverse(T[a][i])

traverse('A')
for i in range(3): print(R[i])