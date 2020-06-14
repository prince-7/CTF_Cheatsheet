found = []
with open('main.c') as f:
    for e in f:
            e = e.replace(' ', '0')
            e = e.replace('\t','1')
            try:
                found.append(e)
            except Exception:
                pass

flag = []
for i in range(0,len(found)):
    for j in range(0,len(found[i])):
        if(found[i][j]=='1' or found[i][j]=='0'):
            flag.append(found[i][j])

print(''.join(flag))