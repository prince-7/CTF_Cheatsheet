'''
import os
os.mkdir('./coordinates')
os.mkdir('./images')  
file = open('stripped.txt','r')
arr = [l for l in file.read().split('\n')]
coord = []
flag = 0
for l in arr:
	if (l[2:4]=='01'):
		if(flag ==0):
			x = []
		x.append((l[6:8],l[8:10]))
		flag = 1
	elif (l[2:4] == '00' and flag ==1):
		coord.append(x)
		flag=0


for c in range(len(coord)):
	x = 0
	y=0

	newcord = []
	for i in range(len(coord[c])):
		v1 = int(coord[c][i][0],16)
		if(v1>127):
			v1 = v1 -256
		x = x + v1
		v2 = int(coord[c][i][1],16)
		if(v2>127):
			v2 = v2 -256
		y= y + v2
		newcord.append((x,y))


	cords = open("./coordinates/coordinates"+str(c)+".txt" , 'w')
	for i in range(len(newcord)):
		cords.write(str(newcord[i][0])+" "+str(newcord[i][1])+'\n')
'''

file = open('stripped.txt','r')
arr = [l for l in file.read().split('\n')]
x = 0
y=0

newcord = []
for i in range(len(arr)):
	try:
		v1 = int(arr[i][6:8],16)
		if(v1>127):
			v1 = v1 -256
		x = x + v1
		v2 = int(arr[i][8:10],16)
		if(v2>127):
			v2 = v2 -256
		y= y + v2
		if(arr[i][2:4]=='01'):
			newcord.append((x,y))
	except:
		continue
cords = open("coordinates.txt" , 'w')
for i in range(len(newcord)):
	cords.write(str(newcord[i][0])+" "+str(newcord[i][1])+'\n')