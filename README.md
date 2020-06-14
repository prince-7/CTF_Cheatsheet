# CTF tools
This Repo Contains Write-UPs for all Tasks 
HERE ARE SOME EXTREMELY USEFUL TOOLS AND COMMANDS


SOME Useful Tools, links and commands


1)binwalk -e <filenam> : //Extracts hidden files

2)steghide extract -sf <filename> : //Extracts hidden text in the image

3)xxd <file name> : //Prints the Hex version of file

4)grep "element" //finds the element

5)strings <filename> // gives the strings hidden in the file

6)hexedit <filename>

7)java -jar stegsolve.jar

8)pngcheck <filename>

9)tar -xvf <filename>

10)cat temp.txt | cut -d'(' -f2 | sort -n | cut -d"'" -f2 | tr -d "\n" ; echo      // used this command to obtain the flag from the java file having flag characters written in an scrambled order 

11)fcrackzip -u -l 10-11 -c a1 -p IEC2019000 findME.zip     
// this command helps us to find the password to a zip. -u : unzip -l: range of length -c: type of elements a1 means alphabets and numbers -p:sample password 

12)ltrace ./file     is a helphul command to see the functioning of a program
also use strace

13)Esoteric languages(pikalang, 2dfuck, brainfuck) use tio.run website, Malboge an esoteric language that looks like base 85.

14)curl "https://2019shell1.picoctf.com/problem/4162/login.php" --data "username=admin&password='+or+1=1--" && echo 
   this command will find the password to username admin stored in database.

15)Robots -->>> url/robots.txt (shows hidden info)

16)cat /proc/(process id)/             
    we can see all files running in the process with given process id.

17)use tcpflow -r file  for pcap

18)exiftool for meta data

19) git show -1 filename.txt > to compare against the last revision of file
    git show -2 filename.txt > to compare against the 2nd last revision of file

20)Basic Injection  if there is a hidden info in the data base then to leak the data type 'OR''=' in the info bar.

21) 1 union select 1,TABLE_NAME, 3,4 from INFORMATION_SCHEMA.TABLES     input this code in the info bar of a website for sql attack using injection.



22) Use this site for substitution https://quipqiup.com/

23) Detect the DMFT Tools http://dialabc.com/sound/detect/index.html

24) Online Stegnographic Decoder :- https://futureboy.us/stegano/decinput.html

25) zsteg :- another great stego tool

26) john the ripper :- tool for password cracking

27) Postman great tool for web challs
