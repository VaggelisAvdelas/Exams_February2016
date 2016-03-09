#creating empty matrix
table2 = [[0 for x in xrange(8)] for x in xrange(8)]

#reading txt file and removing unnecessary punctuation
file_in = open ("input.txt")
for line in file_in:
    line = line.replace("'" , "")
    line = line.replace("][" , ", ")
    line = line.replace("]" , "")
    line = line.replace("[" , "")
file_in.close()
table = line.split(", ")
y = 0

#filling the matrix with elements from 1-d list
for i in range(8):
    for j in range(8):
        table2[i][j]= table[y]
        y +=1

#rotating the matrix
rotated90 = zip(*table2[::-1])
for i in range(8):
    print rotated90[i]
print "\n"
rotated180 = zip(*rotated90[::-1])
for i in range(8):
    print rotated180[i]
print "\n"
rotated270 = zip(*rotated180[::-1])
for i in range(8):
    print rotated270[i]
