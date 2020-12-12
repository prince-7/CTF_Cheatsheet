#Writeup for PCAP Tracing Challenge
This is a Challenge created by me for b00t2root CTF event organized by my college team NULLKrypt3rs.
In this Challenge a PCAP file was given which had USB Mouse Capture Data in the leftover Packates.
The leftover data has can be used to trace the path of the mouse and also the clicks.(can be used to differntiate between left-click and right click).
So first of all we can extract the leftover data from the pcap file by using tshark.
`tshark -r tracer.pcap -Y "(usb.transfer_type == 0x01) && (frame.len == 35)" -e usb.capdata -Tfields > stripped.txt`

Now we have the the all the data stored in stripped.txt
After this wrote a python script [ exploit.py ].
The basic concept is that the leftover data ` 02 : 01 : 00 : fe : 0f : 00 : 00 : 00 ` contains of 8 bytes
the second bytes tells us `01` meaning right click was made and 3rd and 4th byte tells us about x and y coordinates respectively.

