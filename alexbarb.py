stack = input()
lis = stack.split(" ")
maximum = int(lis[0])
alex = int(lis[1])
barb = int(lis[2])


if (maximum % (alex+barb))< alex:
    print("Barb")
else:
    print("Alex")

