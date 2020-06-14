from pwn import *

r=connect('jh2i.com',  50035)

map = {'AAA' : 'a' , 'AAC' : 'b' , 'AAG' : 'c' ,'AAT' : 'd' , 'ACA' : 'e' , 'ACC' : 'f' , 'ACG' : 'g' , 'ACT' : 'h' , 'AGA' : 'i' , 'AGC' : 'j' , 'AGG' : 'k' , 'AGT' : 'l' , 'ATA' : 'm' , 'ATC' : 'n' , 'ATG' : 'o' , 'ATT' : 'p' , 'CAA' : 'q' , 'CAC' : 'r' , 'CAG' : 's' , 'CAT' : 't' , 'CCA' : 'u' , 'CCC' : 'v' , 'CCG' : 'w' , 'CCT' : 'x' , 'CGA' : 'y' , 'CGC' : 'z' , 'CGG' : 'A' , 'CGT' : 'B' , 'CTA' : 'C' , 'CTC' : 'D' , 'CTG' : 'E' , 'CTT' : 'F' , 'GAA' : 'G' , 'GAC' : 'H' , 'GAG' : 'I' , 'GAT' : 'J' , 'GCA' : 'K' , 'GCC' : 'L' , 'GCG' : 'M' , 'GCT' : 'N' , 'GGA' : 'O' , 'GGC' : 'P' , 'GGG' : 'Q' , 'GGT' : 'R' , 'GTA' : 'S' , 'GTC' : 'T' , 'GTG' : 'U' , 'GTT' : 'V' , 'TAA' : 'W' , 'TAC' : 'X' , 'TAG' : 'Y' , 'TAT' : 'Z' , 'TCA' : '1' , 'TCC' : '2' , 'TCG' : '3' , 'TCT' : '4' , 'TGA' : '5' , 'TGC' : '6' , 'TGG' : '7' , 'TGT' : '8' , 'TTA' : '9' ,
'TTC' : '0' , 'TTG' : ' ' , 'TTT': '.'}  

seq = (r.recvuntil('\n> ', drop=True))
print(seq)
codons = []
a = []
for i in range (0,len(seq)):
	if(i%3==2):
		a.append(seq[i])
		a = "".join(a)
		codons.append(a)
		a = []
	else:
		a.append(seq[i])

reply = []

for i in range (0 , len(codons)):
	reply.append(map[codons[i]])

reply = "".join(reply)
r.send(reply+ '\n')
print(reply)

while(True):
	try:
		seq = (r.recvuntil('\n', drop=True))
		print(seq)
		codons = []
		a = []
		for i in range (0,len(seq)):
			if(i%3==2):
				a.append(seq[i])
				a = "".join(a)
				codons.append(a)
				a = []
			else:
				a.append(seq[i])

		reply = []

		for i in range (0 , len(codons)):
			reply.append(map[codons[i]])

		reply = "".join(reply)
		r.send(reply+ '\n')
		print(reply)

	except EOFError :
		break
