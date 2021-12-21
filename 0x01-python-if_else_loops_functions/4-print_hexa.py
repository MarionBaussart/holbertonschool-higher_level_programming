#!/usr/bin/python3
for number in range(0, 99):
	print("{0:d} = 0x{0:x}".format(number))
	#or we can use : print(number, " = ", hex(number).format(number))
