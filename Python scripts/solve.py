
#This Script reads the file and replace HEX Places having E2 80 83(representing "...") by 0 and 20 (representing " ") by 1 and thus creates a binary string which when decoded to ascii gives the flag.

from pwn import *

with open("whitepages.txt", "rb") as bin_file:
    data = bytearray(bin_file.read()) 
    data = data.replace(b'\xe2\x80\x83', b'0')
    data = data.replace(b'\x20', b'1')
    data = data.decode("ascii")
    print unbits(data)
