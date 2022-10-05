import sys

if len(sys.argv) < 2:
	exit(0)

with open(sys.argv[1], 'r') as f:
	file = f.read().splitlines()

file.pop(0)
file.pop(1)
file.pop(2)
file.pop(3)

vertex = []

for i,c in enumerate(file):
	if c[0] == 'v' and c[1] == ' ':
		vertex.append(c)
	else:
		file.pop(i)

for i,c in enumerate(vertex):
	vertex[i] = c.replace('v ', '').replace(' ', ',') + ','

print('\n'.join(vertex))

with open(sys.argv[1], 'w') as f:
	f.write(f'#pragma once\nfloat {sys.argv[1].replace(".obj", "_OBJ")} = ' + '{ ' + ''.join(vertex) + ' };')