import base64
ciphertext = base64.b64decode('1a2xasBR1Wh24wdZYo5XsqDvpryJr3+vM8wv3HSHe8Yro0IAyfSGJ459pU3QbfyNR0Ip9DYZ1zw5h7PuAmXI/g==')
result=ciphertext[0:10]+chr(ord(ciphertext[10])^0x1)+ciphertext[11:]
result = base64.b64encode(result)
print(result)

