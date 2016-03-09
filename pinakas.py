#program to create a random matrix filled with spaces and zeros
import random

choices = [" ", 0]
matrix = [[0 for x in xrange(8)] for x in xrange(8)]
for i in range(8):
	for j in range(8):
		matrix[i][j] = random.choice(choices)
	print matrix[i]
file_out = open("input.txt", "w")
for i in xrange(8):
	file_out.write ('%s' % matrix[i])
file_out.close()
