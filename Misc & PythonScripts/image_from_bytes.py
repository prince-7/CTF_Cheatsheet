from pwn import *

r=connect('jh2i.com',  50001)

r.recvuntil('.', drop=True)
r.send('\n')

(r.recvuntil('\n', drop=True))
noise = (r.recvuntil('That', drop=True))


with open('image.png', 'wb') as file:
    file.write(noise[:-2])
