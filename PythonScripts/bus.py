from pwn import *

r=connect('chals20.cybercastors.com',  14421)

string = 'SNESYT3AYN1CTISL7SRS31RAFSKV3C4I0SOCNTGER0COM5'


while(True):
	print(r.recvuntil("choice:"))
	r.send('1\n')
	print(r.recvuntil("bus?:"))
	r.send(str(string)+'\n')
	print(r.recvuntil("seating:"))
	string = r.recvuntil('\n')
	print(string)
