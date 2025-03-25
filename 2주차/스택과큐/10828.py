import sys
input = sys.stdin.readline 

n = int(input())
stack = []                     
n = int(input())               

for i in range(n):              
    qry = input().split()       

    if qry[0] == 'push': 
        stack.append(int(qry[1]))   
    elif qry[0] == 'pop': 
        print(stack.pop() if stack else -1)
    elif qry[0] == 'size':
        print(len(stack))
    elif qry[0] == 'empty':
        print(0 if stack else 1)
    else:  
        print(stack[-1] if stack else -1)