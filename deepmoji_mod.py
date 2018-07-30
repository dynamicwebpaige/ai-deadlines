import time
import sys

fp = open('outputs.txt', 'r')

counter = 0

for line in fp:

	if len(line) / 8 == 0 or counter == 0:
		sys.stdout.write(line)
		time.sleep(0.5)
		counter = 1
	elif line[0] == "/" or counter == 1:
		sys.stdout.write(line)
		counter = 0
	elif len(line) / 3 == 0 or counter == 0:
		sys.stdout.write(line)
		time.sleep(0.7)
	elif len(line) / 2 == 0 or line[0] == "B":
		sys.stdout.write(line)
		time.sleep(0.05)
	else:
		sys.stdout.write(line)
		time.sleep(0.15)
