from pwn import *

r=connect('jh2i.com',  50031)

print(r.recvuntil('>' , drop=True))
r.send('6'+'\n')
r.recvuntil(':' , drop=True)
r.send('1' + '\n')

while(True):
	try:
		r.recvuntil('>' , drop=True)
		r.send('5' + '\n')
		r.recvuntil(': ' , drop=True)
		gold = (r.recvuntil('\n' , drop=True))
		print(gold)

		if(int(gold) > 100000):
			print(r.recvuntil('>' , drop=True))
			r.send('6'+'\n')
			r.recvuntil(':' , drop=True)
			r.send('5' + '\n')
			print(r.recvuntil('> ' , drop=True))
			r.send('1' + '\n')
			print(r.recvuntil(':' , drop=True))
			r.send('y' + '\n')
			print(r.recvuntil('>' , drop=True))
			print(r.recvuntil(':' , drop=True))

	except EOFError :
		print(r.recv(1024))
		break

	# flag : - flag{it_was_in_fact_you_that_was_really_powerful}