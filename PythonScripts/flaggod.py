from pwn import *
import os
import binascii

r=connect('chals20.cybercastors.com',  14431)


print(r.recv())
r.send('\n')

l=0

while(True):
    try:
        print(r.recvuntil("Transmitted message: " , drop=True))
        a= r.recvuntil('\n',drop=True)
        print(a)
        r.recvuntil("Received message: " , drop=True)
        b= r.recvuntil('\n',drop=True)
        print(b)

        s1 = str(bin(int(binascii.hexlify(a), 16)))

        s2 = str(bin(int(b, 16)))
        print(len(s1)-len(s2))
        k=len(s1)-len(s2)
        for i in range(k):
           s2='1'+s2
        dist=0

        for i in range(0, len(s1)):
            if(s1[i]!=s2[i]):
                dist=dist+1

        #dist=hamming(s1,s2)
        print(dist)
        l=l+1
        r.recvuntil("distance: " , drop=True)
        r.send(str(dist) + '\n')

    except EOFError :
        print(r.recv())
        break
