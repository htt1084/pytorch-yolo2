import os
from random import shuffle


txt_file = open("person_train.txt", "r")
lines = txt_file.readlines()
txt_file.close()
#shuffle(lines)

COCO = []
WW = []

for line in lines:
	if 'COCO' in line:
		COCO.append(line)
	else:
		WW.append(line)

shuffle(COCO)
n = len(COCO)

print(len(COCO))
print(len(WW))
print(len(lines))

with open("person_train.txt", "w") as out_file:
	for line in COCO[:n//5]:
		out_file.write(line)
	for line in WW:
		out_file.write(line)
	for line in COCO[n//5:(2*n)//5]:
		out_file.write(line)
	for line in WW:
		out_file.write(line)
	for line in COCO[(2*n)//5:(3*n)//5]:
		out_file.write(line)
	for line in WW:
		out_file.write(line)
	for line in COCO[(3*n)//5:(4*n)//5]:
		out_file.write(line)
	for line in WW:
		out_file.write(line)
	for line in COCO[(4*n)//5:]:
		out_file.write(line)
	for line in WW:
		out_file.write(line)


