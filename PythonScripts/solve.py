from pwn import *

r=connect('chals20.cybercastors.com',  14429)


map ={
        "zero" : '0', "one" :'1' , "two" :'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8',
        "nine":'9', "plus":'+', "minus" : '-', "//" : '//' , "multiplied-by" : '*' , "divided-by" : '//'
}


print(r.recv())
r.send('\n')
i=0
while(True) :
	i=i+1
	print(i)
	try:
		r.recvuntil("What is ")

		a = (r.recvuntil(' ', drop=True))
		if(len(a)>1) :
			a=map[a]
			a=int(a.decode('utf-8'))
		else:
			a=int(a.decode('utf-8'))
		print(a)

		o = r.recvuntil(' ', drop=True).decode('utf-8')
		if(len(o)>1) :
			o=map[o[0:]]
			o=o.decode('utf-8')
		else:
			o= o.decode('utf-8')
		print(o)


		b = (r.recvuntil(' ', drop=True).decode('utf-8'))
		if(len(b)>2) :
			b=map[b[0:]]

		b=b.decode('utf-8')
		b=int(b.decode('utf-8'))
		print(b)

						
		if(o == '*') :
			r.send(str(int(a*b))+'\n')
			print(str(int(a*b))+'\n')
		elif(o == '//') :
			r.send(str(int(a/b))+'\n')
			print(str(int(a/b))+'\n')
		elif(o == '+') :
			r.send(str(int(a+b))+'\n')
			print(str(int(a+b))+'\n')
		elif(o == '-') :
			r.send(str(int(a-b))+'\n')
			print(str(int(a-b))+'\n')
		
	except EOFError :
		print(r.recv(1024))
		break