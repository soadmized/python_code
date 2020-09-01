import os

""" 
a f j
b g k
c h l
d i
e
"""

with open('1.txt', 'r') as file_1:
	txt_1 = file_1.readlines()

with open('2.txt', 'r') as file_2:
	txt_2 = file_2.readlines()

with open('3.txt', 'r') as file_3:
	txt_3 = file_3.readlines()

#result = open('result.txt', 'w')

counter_1 = 0
counter_2 = 0
counter_3 = 0
id = -1

for i in range(100):
	line_1 = txt_1[counter_1]
	counter_1 += 1
	if counter_1 >= len(txt_1):
		counter_1 = 0

	line_2 = txt_2[counter_2]
	counter_2 += 1
	if counter_2 >= len(txt_2):
		counter_2 = 0

	line_3 = txt_3[counter_3]
	counter_3 += 1
	if counter_3 >= len(txt_3):
		counter_3 = 0

	res = line_1.rstrip('\n') + line_2.rstrip('\n') + line_3.rstrip('\n')
	id += 1
	print(id, res)

