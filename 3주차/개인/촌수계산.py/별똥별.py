import time
import sys
import random
import os

try:
    cols, rows = os.get_terminal_size()
except:
    cols, rows = 80, 24  

stars = ['*', '+', '.', '✦', '✧']
frame_count = 100

star_positions = []

for i in range(20):
    x = random.randint(0, cols - 1)
    y = random.randint(0, rows - 2)
    star = random.choice(stars)
    star_positions.append([x, y, star])

for _ in range(frame_count):
    screen = [[' ' for i in range(cols)] for j in range(rows)]

    for star in star_positions:
        x, y, shape = star
        if 0 <= y < rows:
            screen[y][x] = shape
        star[1] += 1 

    if random.random() < 0.3:
        x = random.randint(0, cols - 1)
        star = random.choice(stars)
        star_positions.append([x, 0, star])

    sys.stdout.write('\x1b[2J\x1b[H')
    for row in screen:
        print(''.join(row))
    time.sleep(0.05)

print("\n✨ 애니메이션 종료 ✨")