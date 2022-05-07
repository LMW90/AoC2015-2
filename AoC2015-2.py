filename = 'inputDay-2.txt'
try:
    fhand = open(filename)
except:
    print(f'Could not open file {filename}')
    exit()
total_area = 0
# turn individual lines into lists of dimensions
for line in fhand:
    line = line.rstrip()
    dims = line.split('x')
# convert dimensions into integers
    for i in range(0, len(dims)):
        dims[i] = int(dims[i])
    # print(dims)
    # calculate side areas
    A = dims[0] * dims[1]
    B = dims[0] * dims[2]
    C = dims[1] * dims[2]
    # calculate total area of a box
    area = 2 * (A + B + C) + min(A, B, C)
    # print(area)
    # increment rolling sum
    total_area += area
print(total_area)
