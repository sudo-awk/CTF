Just another random CTF room created by me. Well, the main objective of the room is to test your CTF skills. For your information, vol.1 consists of 20 tasks and all the challenges are extremely easy. Stay calm and Capture the flag. :)

Note: All the challenges flag are formatted as THM{flag}, unless stated otherwise

Answer the questions below
High five!

### Task 2  What does the base said?
Can you decode the following?
```
VEhNe2p1NTdfZDNjMGQzXzdoM19iNDUzfQ==

--> echo -n "VEhNe2p1NTdfZDNjMGQzXzdoM19iNDUzfQ==" | base64 -d
THM{ju57_d3c0d3_7h3_b453}%    >>> flag
```

### Task 3  Meta meta
Meta! meta! meta! meta...................................

### Task 4 Answer the questions below
I'm hungry, I need the flag.
```
After downloading the task files, i used exiftool to check for metadata and got the flag

exiftool Findme.jpg 
Owner Name                      : THM{3x1f_0r_3x17}
```

### Task 5  Erm......Magick
Huh, where is the flag? THM{wh173_fl46}

Answer the questions below
Did you find the flag?

```
steghide extract -sf Extinction.jpg
Enter passphrase: 
the file "Final_message.txt" does already exist. overwrite ? (y/n) y
wrote extracted data to "Final_message.txt".

It going to be over soon. Sleep my child.

THM{500n3r_0r_l473r_17_15_0ur_7urn}
```
### Task 6  QRrrrr
Such technology is quite reliable.

Answer the questions below
More flag please!
```
Just download the file and I used google lens to get the flag

THM{qr_m4k3_l1f3_345y}
```
### Task 7  Reverse it or read it?
Both works, it's all up to you.

Answer the questions below
Found the flag?
```
I run the strings command and got the flag
 strings hello.hello        
THM{345y_f1nd_345y_60}

````
### Task 8  Another decoding stuff
Can you decode it?

3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L

Answer the questions below
Oh, Oh, Did you get it?

```
This one, I had to look the write ups because I cant figure out which encoding was used in this, and I want to thank mr shamsker khan for his write up, I found out it was base58. so pasting it to cyberchef I was able to get the flag

THM{17_h45_l3553r_l3773r5}

```
### Task 9  Left or right
Left, right, left, right... Rot 13 is too mainstream. Solve this

MAF{atbe_max_vtxltk}

Answer the questions below
What did you get?

```
this seems like a ceasar cipher since the format is for THM flag but that letters are not correct, so I pasted it to a ceasar cipher decoder and got the flag

THM{hail_the_caesar}
```
### Task 10  Make a comment
No downloadable file, no ciphered or encoded text. Huh .......

Answer the questions below
I'm hungry now... I need the flag
```
Hint says check the html

THM{4lw4y5_ch3ck_7h3_c0m3mn7}
```
### Task 11
I accidentally messed up with this PNG file. Can you help me fix it? Thanks, ^^

Answer the questions below
What is the content?

```
This task took me a few hours to solve since this is my first encounter with editing a hex byte
I look for multiple write ups so I could really understand the task. This is awesome since I got to learn about the magic numbers(first hex bytes of a file), this file is a PNG so the magic number should be \x89\x50\x4e\x47 , the current PNG file first hex are incorrect so we should just need to replace those numbers


```
### Task 12  Read it
Some hidden flag inside Tryhackme social account.
Answer the questions below
Did you found the hidden flag?
```
this task is more of osint
Upon checking the reddit google I got the flag

THM{50c14l_4cc0un7_15_p4r7_0f_051n7}


```

### Task 13  Spin my head
What is this?

++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++++++++.------------.+++++.>+++++++++++++++++++++++.<<++++++++++++++++++.>>-------------------.---------.++++++++++++++.++++++++++++.<++++++++++++++++++.+++++++++.<+++.+.>----.>++++.

Answer the questions below
Can you decode it?
```
I've encountered this language before, it is called Brainfuck so I used brainfuck website decoder and got the flag
THM{0h_my_h34d}
```
### Task 14  An exclusive!
Exclusive strings for everyone!

S1: 44585d6b2368737c65252166234f20626d
S2: 1010101010101010101010101010101010

Answer the questions below
Did you crack it? Feed me now!
```
I spent a few hours also for this task, I've been trying to xor it in python but I am getting an error, but this time I am happy I learned about a new website that can process xor and output it to a different encoding

I copied the variables to and gained the flag
[xor-calculataor](https://toolslick.com/math/bitwise/xor-calculator)
THM{3xclu51v3_0r}
```
### Task 15  Binary walk
Please exfiltrate my file :)
```
I had experiencec with binwalk before, so I just read again the man page and looked for the extract tag
 binwalk -e hell.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
265845        0x40E75         Zip archive data, at least v2.0 to extract, uncompressed size: 69, name: hello_there.txt
266099        0x40F73         End of Zip archive, footer length: 22

Now we can see that a folder was created under _hell, I went into the folder and got the flag
ls | grep -i 'hell'   
_hell.jpg-0.extracted

Thank you for extracting me, you are the best!

THM{y0u_w4lk_m3_0u7}

```

### Task 16  Darkness
There is something lurking in the dark.

Answer the questions below
What does the flag said?
```
first I was stucked again, because this is my first encounter with .jar file , but upon googling for sometime, I understood that I need to download it and create a directory and move it. with that knowledge I was able to get the flag 

THM{7h3r3_15_h0p3_1n_7h3_d4rkn355}
```


### Task 16  Darkness
There is something lurking in the dark.

Answer the questions below
What does the flag said?
```
This task allowed to learn another steganograpy tool called stegsolve. The tool have different mode to see the actual pic by changing the colorization of the picture.
and by that I was able to get the flag

THM{7h3r3_15_h0p3_1n_7h3_d4rkn355} 
```
### Task 17  A sounding QR
How good is your listening skill?

P/S: The flag formatted as THM{Listened Flag}, the flag should be in All CAPS

Answer the questions below
What does the bot said?
```
This task is usually OSINT, after playing the sound I checked for the comments to get the flag
THM{soundingqr}
```

### Task 18  Dig up the past
Sometimes we need a 'machine' to dig the past

Targetted website: https://www.embeddedhacker.com/
Targetted time: 2 January 2020

Answer the questions below
Did you found my past?
```
This task used wayback machine, and by walking through the web I am able to get the flag
THM{ch3ck_th3_h4ckb4ck}
```
### Task19? Can you solve the following? By the way, I lost the key. Sorry >.<

MYKAHODTQ{RVG_YVGGK_FAL_WXF}

Flag format: TRYHACKME{FLAG IN ALL CAP}

Answer the questions below
The deciphered text


First, I thought it was a cesar cipher again, after spending some time, I checked the hint and fount out it was a vigenere cipher, and by that I go to a website [vigenere-cipher-decoder](https://www.dcode.fr/vigenere-cipher) that can decode and it I got the flag
```
TRYHACKME{YOU_FOUND_THE_KEY}
```
### Task 20  Small bases
Decode the following text.

581695969015253365094191591547859387620042736036246486373595515576333693

Answer the questions below
What is the flag?


In this task, the hint said to decode it from dec to hex to ascii, with that in mind I create a python program that will decode the give numbers to me 
```
#!/usr/local/bin/python3

dec = int("581695969015253365094191591547859387620042736036246486373595515576333693")
print(hex(dec)[0:])
n = hex(dec)[2:]
print(bytearray.fromhex((n)).decode())
THM{17_ju57_4n_0rd1n4ry_b4535}
```
### Task 21  Read the packet
I just hacked my neighbor's WiFi and try to capture some packet. He must be up to no good. Help me find it.
Answer the questions below
Did you captured my neighbor's flag?
```
After downloading the file, I opened it in wireshark, I filtered the packet using HTTP and found a /FLAG requests, upon checking the request the flag is encoded in plain text

THM{d0_n07_574lk_m3}
```
