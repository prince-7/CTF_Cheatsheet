mapping= {
"04" : "a",
"05" : "b",
"06" : "c",
"07" : "d",
"08" : "e",
"09" : "f",
"0a" : "g",
"0b" : "h",
"0c" : "i",
"0d" : "j",
"0e" : "k",
"0f" : "l",
"10" : "m",
"11" : "n",
"12" : "o",
"13" : "p",
"14" : "q",
"15" : "r",
"16" : "s",
"17" : "t",
"18" : "u",  
"19" : "v",
"1a" : "w",
"1b" : "x",
"1c" : "y",
"1d" : "z",
"1e" : "1",
"1f" : "2",
"20" : "3",
"21" : "4",
"22" : "5",
"23" : "6",
"24" : "7",
"25" : "8",
"26" : "9",
"27" : "0",
"2c" : "",
"2f" : "{",
"30" : "}",
"38" : "/",
"39" : "caps"
}

nums = []
keys = open('data.txt')
for line in keys:
    nums.append((line[4:6]))


keys.close()

output = []

for f in nums:
    if f == '00':
        continue
    elif f == '':
        continue
    else:
        output.append(f)

flag =[]
for o in output:
    flag.append(mapping[o])

print("".join(flag))

