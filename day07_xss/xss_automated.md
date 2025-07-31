# Automated XSS Testing with XSStrike

## 🧪 Target
- DVWA XSS Reflected Module
- URL: `http://192.168.56.101/dvwa/vulnerabilities/xss_r/?name=test`

## ⚙️ Tool Used
- [XSStrike](https://github.com/s0md3v/XSStrike)
- Version: 3.1.5
- Mode: Automatic testing and crawling

## 🔧 Steps Taken
1. Cloned XSStrike: `git clone https://github.com/s0md3v/XSStrike`
2. Created Python virtual environment:
    ```bash
    python3 -m venv venv && source venv/bin/activate
    ```
3. Installed requirements:
    ```bash
    pip install -r requirements.txt
    ```
4. Ran crawler:
    ```bash
    python3 xsstrike.py -u "http://192.168.56.101/dvwa/vulnerabilities/xss_r/?name=test" --crawl
    ```
5. Ran full scan (next step):
    ```bash
    python3 xsstrike.py -u "http://192.168.56.101/dvwa/vulnerabilities/xss_r/?name=test"
    ```

## ✅ Result
- Reflection: Not found
- DOM-based XSS: Not detected
- WAF Status: Offline
- Recommendation: Manually test using script payloads like `<script>alert('XSS')</script>`

