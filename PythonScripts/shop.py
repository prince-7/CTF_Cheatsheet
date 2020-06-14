from pwn import *

r=connect('jh2i.com',  50034)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while(True): 
    a=(r.recvuntil('\n'))
    r.send(str(a)+'\n')
