#!/usr/bin/python3

from pwn import *
from decimal import Decimal as D

r = connect('challenge.ctf.games', 30310)

print(r.recv().decode('utf-8'))
r.send('Y'.encode())
print(r.recv().decode('utf-8'))

while(True) :
	try:
		print(r.recvuntil('What is '.encode()).decode())

		a = r.recvuntil(' ', drop=True).decode()
		print(a)
		stat = False
		if (len(a.split('.')) == 2):
			stat = True
		s = r.recvuntil(' ', drop=True).decode()
		print(s)
		b = r.recvuntil('?', drop=True).decode()
		print(b)
		if (len(b.split('.')) == 2):
			stat = True
		if (s == '/'):
			a = D(D(a)/D(b))
			if(stat == False):
				a = int(a)
		elif (s == '*'):
			a = D(D(a)*D(b))
		elif (s == '+'):
			a = D(D(a)+D(b))
		elif (s == '-'):
			a = D(D(a)-D(b))
		print(str(round(a,1)))
		r.send(str(round(a,1)).encode())

		# if(len(a)>1) :
		# 	a=int(a.decode('utf-8'))
		# else:
		# 	a=int(a.decode('utf-8'))

		# o = r.recvuntil(' ', drop=True).decode('utf-8')
		# if(len(o)>1) :
		# 	o=map[o[0:]]
		# 	o=o.decode('utf-8')
		# else:
		# 	o= o.decode('utf-8')
		# print(o)


		# b = (r.recvuntil(' ', drop=True).decode('utf-8'))
		# if(len(b)>2) :
		# 	b=map[b[0:]]

		# b=b.decode('utf-8')
		# b=int(b.decode('utf-8'))
		# print(b)

						
		# if(o == '*') :
		# 	r.send(str(int(a*b))+'\n')
		# 	print(str(int(a*b))+'\n')
		# elif(o == '//') :
		# 	r.send(str(int(a/b))+'\n')
		# 	print(str(int(a/b))+'\n')
		# elif(o == '+') :
		# 	r.send(str(int(a+b))+'\n')
		# 	print(str(int(a+b))+'\n')
		# elif(o == '-') :
		# 	r.send(str(int(a-b))+'\n')
		# 	print(str(int(a-b))+'\n')
		
	except EOFError :
		print(r.recv(1024))
		break
