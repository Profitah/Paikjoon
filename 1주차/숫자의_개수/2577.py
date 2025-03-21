A = int(input())
B = int(input())
C = int(input())
D = A * B * C 

integer_str = [int(integer_str) for integer_str in str(D)]

count0 = integer_str.count(0)
count1 = integer_str.count(1)
count2 = integer_str.count(2)
count3 = integer_str.count(3)
count4 = integer_str.count(4)
count5 = integer_str.count(5)
count6 = integer_str.count(6)
count7 = integer_str.count(7)
count8 = integer_str.count(8)
count9 = integer_str.count(9)


print(count0)
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
print(count6)
print(count7)
print(count8)
print(count9)