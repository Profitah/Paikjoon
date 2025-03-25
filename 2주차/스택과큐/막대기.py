n = int(input())

stack = []
for i in range(n):
    stack.append(int(input()))

막대기 = 0  
막대기_최대높이 = 0     

for 높이 in reversed(stack):
    if 높이 > 막대기_최대높이:
        보이는_막대기 += 1        
        막대기_최대높이 = 높이      

print(보이는_막대기)
