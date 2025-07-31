# Manual CSRF Testing – DVWA

## 🎯 Target
- URL: http://192.168.56.101/dvwa/vulnerabilities/csrf/
- Method: GET
- Parameters: `password_new`, `password_conf`, `Change`

## 🔍 Observations
- Password change functionality is exposed via GET request.
- No CSRF token or user verification is required.
- Vulnerable to simple CSRF exploitation.

## 🔐 Captured Request (via Burp Suite)
  
GET /dvwa/vulnerabilities/csrf/?password_new=mypassword&password_conf=mypassword&Change=Change HTTP/1.1
Host: 192.168.56.101
Cookie: PHPSESSID=ee14a0fc65da267bc0c284af23452d03; security=low
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0


## ✅ Result
- Password was changed without user interaction.
- Confirms **CSRF vulnerability** due to:
  - Lack of anti-CSRF tokens
  - Use of GET method for a state-changing operation
