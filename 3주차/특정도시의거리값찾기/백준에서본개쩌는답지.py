import sys
from collections import deque
import heapq

n, m, k, x = map(int, sys.stdin.readline().split())
city_dic = {}

for i in range(m):
  start, end = map(int, sys.stdin.readline().split())
  if start in city_dic:
    city_dic[start].append(end)
  else:
    city_dic[start] = [end]