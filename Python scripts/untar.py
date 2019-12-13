from os import system

system('unar ./1000.tar')
for i in range(999, -1, -1):
  system('unar ./{}/{}.tar'.format(i+1, i))