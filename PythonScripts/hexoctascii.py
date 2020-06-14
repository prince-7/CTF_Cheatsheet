import base64
pswd = [
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            '7' , 'e' , '0' , '3' , 'd' , '1' , '1' , '6' ]
for i in range(0,8):
	print(chr(pswd[i]),end="")
for i in range(8,16):
	print(chr(pswd[i]),end="")
print("bYt3s_26",end="")
for i in range(16,24):
	print(pswd[i],end="")