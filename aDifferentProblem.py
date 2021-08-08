# https://open.kattis.com/problems/different

import sys

for line in sys.stdin:
    data = [int(x) for x in line.split()]
    total = abs(data[1] - data[0])
    print(total)