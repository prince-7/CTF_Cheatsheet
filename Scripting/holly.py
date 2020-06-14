from pwn import *

r=connect('algo.hsctf.com',  4002)


while (True):
	try:
		print(r.recvuntil('\n',drop=True))
		n = (r.recvuntil(' ', drop=True))
		n=int(n.decode('utf-8'))
		x = (r.recvuntil('\n', drop=True))
		x=int(x.decode('utf-8'))
		colpref = []
		stupref = []
		stdname = []
		print(n)
		for i in range(0,n):
			cp = []
			for j in range (0,n-1):
				a=r.recvuntil(' ', drop=True)
				a=int(a.decode('utf-8'))
				cp.append(a)
			a = r.recvuntil('\n',drop=True)
			a=int(a.decode('utf-8'))
			cp.append(a)
			colpref.append(cp)
			print(cp)
		print('\n')
		print('stdpref')
		for i in range(0,n):
			sp = []
			for j in range (0,n-1):
				a=r.recvuntil(' ', drop=True)
				a=int(a.decode('utf-8'))
				sp.append(a)
			a = r.recvuntil('\n',drop=True)
			a=int(a.decode('utf-8'))
			sp.append(a)
			stupref.append(sp)
			print(sp)
		print('\n')
		print('stdname')
		for i in range(0,n):
			a=r.recvuntil('\n', drop=True)
			stdname.append(a)
			print(a)

		print('\n')
		ans= 1000
		for i in range(0,n):
			for j in range(0,n):
				if(stupref[colpref[x][i]][j] == x):
					mini=i+j
					if(mini<ans):
						ans=mini

		print(stdname[ans])
		r.send(str(stdname[ans])+'\n')

	except EOFError :
		print(r.recv(1024))
		break

