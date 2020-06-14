import enchant
from pwn import *

r=connect('jh2i.com',  50012)

while(True):
	try:
		inst = (r.recvuntil('\n' , drop=True))
		inst = str(inst)
		d = enchant.Dict("en_US") 
		print(inst)
		para =(r.recvuntil('\n' , drop=True))
		para = str(para)
		print(para)
		words = []
		a = []
		for i in range (0 , len(para)-1):	
			if(para[i]== ' '):
				a = "".join(a)
				words.append(a)
				a = []
			else:
				a.append(para[i])

		a = "".join(a)
		print(a)
		words.append(a)

		words[0] = words[0][2:]
		print(words[0])
		count = 0 
		alpha = []
		beta = []
		for i in range(0 ,len(words)):
			if(d.check(words[i])):
				alpha.append(words[i])
				count = count + 1
			else:
				beta.append(words[i])

		print(alpha)

		if 'NOT' in inst:
			if 'CHRONOLOGICAL' in inst:
				r.send(" ".join(beta) +'\n')
				print(" ".join(beta) +'\n')
			elif 'ALPHABETICAL' in inst:
				r.send(" ".join(sorted(beta))+ '\n')
				print(" ".join(sorted(beta))+ '\n')
			else :
				r.send (str(len(words)- count)+'\n')
				print(str(len(words)- count)+'\n')

		elif 'ARE' in inst:
			if 'CHRONOLOGICAL' in inst:
				r.send(" ".join(alpha) +'\n')
				print(" ".join(alpha) +'\n')
			elif 'ALPHABETICAL' in inst:
				r.send(" ".join(sorted(alpha))+ '\n')
				print(" ".join(sorted(alpha))+ '\n')
			else :
				r.send (str(count)+'\n')
				print(str(count)+'\n')

		print(r.recvuntil('\n' , drop=True))

	except EOFError :
		print(r.recv(1024))
		break

# flag : flag{you_know_the_dictionary_so_you_are_hired}