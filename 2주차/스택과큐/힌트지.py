a=int(input())
# a_list=[input().split() for i in range(a)]

stack=[]
for ii in range(a):
    i=input().split()
    if i[0]=='push':
        stack.append(int(i[1]))
        
    elif i[0]=='pop':
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif i[0]=='size':
        print(len(stack))
    elif i[0]=='empty':
        if stack:
            print(1)
        else:
            print(0)

    elif i[0]=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        continue