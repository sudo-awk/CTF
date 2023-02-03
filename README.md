# OWASP Juice Shop

# Task 1: Let's go on an adventure! 

```Question #1: What's the Administrator's email address?
Doing an application walkthrough I got the information
--> admin@juice-sh.op
```
```Question #2: What parameter is used for searching? 
--> Q
```
```Question #3: What show does Jim reference in his review? 
--> star trek
```
# Task 2 : Inject the juice 
```Question #1: Log into the administrator account!
--> 32a5e0f21372bcc1000a6088b93b458e41f0e02a
```
```Question #2: Log into the Bender account!
---> fb364762a3c102b2db932069c0e6b78e738d4066
```

# Task 4 Who broke my lock?! 
```Question #1: Bruteforce the Administrator account's password!

I used hydra for this to get the password

aaron@aaron-VirtualBox:~/thm/owasp_juice_shop$ sudo hydra -l admin@juice-sh.op -P /home/aaron/SecLists/Passwords/Common-Credentials/best1050.txt 10.10.249.34 http-post-form "/rest/user/login:email=^USER^&password=^PASS^:Invalid Email or password." -V

----> [80][http-post-form] host: 10.10.249.34   login: admin@juice-sh.op   password: admin123


upon logging in to the admin account i get the flag, yey
--- > c2110d06dc6f81c67cd8099ff0ba601241f1ac0e
```
```Question #2: Reset Jim's password!
 jim@juice-sh.op
---> 094fbc9b48e525150ba97d05b942bbf114987257
```
# Task 5 AH! Don't look! 

```Question #1: Access the Confidential Document!
 go to http://10.10.249.34/ftp/legal.md
 --> edf9281222395a1c5fee9b89e32175f1ccf50c5b
```
```Question #2: Log into MC SafeSearch's account!

He notes that his password is "Mr. Noodles" but he has replaced some "vowels into zeros", meaning that he just replaced the o's into 0's.

We now know the password to the mc.safesearch@juice-sh.op account is "Mr. N00dles"
---> 66bdcffad9e698fd534003fbb3cc7e2b7b55d7f0

Question #3: Download the Backup file!

To get around this, we will use a character bypass called "Poison Null Byte". A Poison Null Byte looks like this: %00. 

Note: as we can download it using the url, we will need to encode this into a url encoded format.

The Poison Null Byte will now look like this: %2500. Adding this and then a .md to the end will bypass the 403 error!

Why does this work? 

A Poison Null Byte is actually a NULL terminator. By placing a NULL character in the string at a certain byte, the string will tell the server to terminate at that point, nulling the rest of the string. 

---> b0fc1e6b4a16579e85e06fee4c36ff8c02fb13795
```
# Task 6 Who's flying this thing? 
```Question #1: Access the administration page!
--> 946a799363226a24822008503f5d1324536629a0
```

```Question #2: View another user's shopping basket!
using burpsuite I change the headers to basket2
--> 41b997a36cc33fbe4f0ba018474e19ae5ce52121
```
```Question #3: Remove all 5-star reviews!
--> 50c97bcce0b895e446d61c83a21df371ac2266ef
```
# Task 7 Where did that come from? 

```Question #1: Perform a DOM XSS!
<iframe src="javascript:alert(`xss`)"> 
	9aaf4bbea5c30d00a1f5bbcfce4db6d4b0efe0bf
````

```Question #2: Perform a persistent XSS!
using burpsuite i added this header in the http request
True-Client-IP	<iframe src="javascript:alert(`xss`)">
--> 149aa8ce13d7a4a8a931472308e269c94dc5f156
```
```Question #3: Perform a reflected XSS!

i used this command to get the flag
<iframe src="javascript:alert(`xss`)"> 
in the place of the 5267-f73dcd000abcc353
---> 23cefee1527bde039295b2616eeb29e1edc660a0
````