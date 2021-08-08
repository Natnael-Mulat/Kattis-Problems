import math

info = input().split(" ")
area = float(info[0])
n = float(info[1])
circle_area = math.pi*(n/(math.pi*2))**2

if circle_area >= area:
    print('Diablo is happy!')
else:
    print('Need more materials!')