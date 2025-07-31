# Web Application Vulnerability Report – DVWA

**Project**: Ultimate 12-Week Pentester Internship  
**Date**: July 31, 2025  
**Author**: Ahmed Adeyemi (@Yemi-spice)  
**Target**: DVWA (Damn Vulnerable Web Application)  
**Security Level**: Low  
**Environment**: Local Lab (`192.168.56.101`)

---

## 🔎 Summary

This report documents three confirmed vulnerabilities discovered and exploited in DVWA: **Cross-Site Scripting (XSS)**, **SQL Injection (SQLi)**, and **Cross-Site Request Forgery (CSRF)**. Manual and automated techniques were used to validate these findings.

---

## 1. 📍 Reflected Cross-Site Scripting (XSS)

**Module**: `xss_r`  
**URL**: `http://192.168.56.101/dvwa/vulnerabilities/xss_r/`  
**Method**: GET

### 🔬 Description
The application fails to sanitize user input in the `name` parameter, allowing for execution of malicious JavaScript code in the browser.

### 💥 Payloads Tested
```html
<script>alert(1)</script>
"><svg/onload=alert(1)>
<img src=x onerror=alert(1)>

✅ Result
JavaScript was executed in the victim browser, confirming XSS.

📎 Evidence
Screenshot: screenshots/xss_manual_success.png

Logs: logs/xss_auto_output.txt

Script: scripts/xss_scanner.py

2. 📍 SQL Injection (SQLi)
Module: sqli
URL: http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit
Method: GET
Parameter: id

🔬 Description
User input is concatenated directly into SQL queries without proper sanitization, allowing for unauthorized data access.

🧪 Manual Payloads
sql
Copy code
' OR '1'='1
1' AND '1'='2
1' UNION SELECT null, version() --
⚙️ Automation Tool
sqlmap

✅ Results
Database banner: 11.8.2-MariaDB-1 from Debian

Databases enumerated: dvwa, mysql, information_schema

Dumped Table: dvwa.users

📎 Evidence
Output: sql_automated.md

Screenshot: screenshots/sqli_manual_success.png

Logs: logs/log, logs/target.txt

3. 📍 Cross-Site Request Forgery (CSRF)
Module: csrf
URL: http://192.168.56.101/dvwa/vulnerabilities/csrf/
Method: GET
Parameters: password_new, password_conf, Change

🔬 Description
Password change is triggered by a GET request with no anti-CSRF token, making it vulnerable to CSRF.

🧪 Test Case
http
Copy code
GET /dvwa/vulnerabilities/csrf/?password_new=hacked&password_conf=hacked&Change=Change
✅ Result
Password was successfully changed without authentication re-validation.

📎 Evidence
Screenshot: screenshots/csrf_success_message.png

Logs: Burp captured request

Notes: csrf_manual.md

🔐 Recommendations
Vulnerability	Recommendation
XSS	Sanitize input, encode output, implement CSP
SQLi	Use parameterized queries / prepared statements
CSRF	Implement anti-CSRF tokens and verify Referer headers

✅ Conclusion
This assessment confirms that DVWA's low-security configuration is vulnerable to several common web attacks. These findings reinforce the importance of secure coding practices, proper input validation, and strong session controls.


