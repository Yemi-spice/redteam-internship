# Day 9 – CSRF & XSS Automation Notes

## CSRF Manual Test (DVWA)
- Set DVWA security to: **Low**
- Target: `/dvwa/vulnerabilities/csrf/`
- Changed password via GET request
- No CSRF token present
- Vulnerability confirmed with Burp Suite

### Key Screenshot Files:
- `csrf_burp_get_request.png` – raw captured GET request
- `csrf_success_message.png` – confirmed password change

---

## Automated XSS Scan
- Tool: Custom Python Script (`scripts/xss_scanner.py`)
- Target: `/dvwa/vulnerabilities/xss_r/`
- Payloads used:
  - `<script>alert(1)</script>`
  - `"><svg/onload=alert(1)>`
  - `';alert(1);//`
  - `<img src=x onerror=alert(1)>`
- Reflected Payloads logged in: `logs/xss_auto_output.txt`

