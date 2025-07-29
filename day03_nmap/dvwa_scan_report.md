# 🔍 Nmap Recon Report – DVWA Target

## 🎯 Target Info
- **IP:** 192.168.56.102
- **Scan Type:** SYN scan with version detection
- **Date:** 2025-07-28
- **Scanner:** Nmap 7.95

---

## 📡 Open Ports & Services

| Port | Protocol | Service     | Version Info                                              |
|------|----------|-------------|-----------------------------------------------------------|
| 22   | TCP      | SSH         | OpenSSH 5.3p1 Debian 3ubuntu4                             |
| 80   | TCP      | HTTP        | Apache 2.2.14 with PHP/5.3.2                              |
| 139  | TCP      | NetBIOS     | Samba smbd 3.X - 4.X                                      |
| 143  | TCP      | IMAP        | Courier Imapd (2008)                                      |
| 443  | TCP      | HTTPS       | Apache with SSL                                           |
| 445  | TCP      | SMB         | Samba smbd 3.X - 4.X                                      |
| 5001 | TCP      | Java Object | Java Object Serialization ⚠️                             |
| 8080 | TCP      | HTTP Alt    | Apache Tomcat/Coyote JSP engine 1.1                       |
| 8081 | TCP      | HTTP Alt    | Jetty 6.1.25 ⚠️                                            |

---

## 🧠 Analysis

- **Apache 2.2.14**: Vulnerable to multiple CVEs including path traversal, RFI, and buffer overflow.
- **PHP 5.3.2**: Outdated, vulnerable to RCE.
- **Samba SMB 3.X–4.X**: Potential for exploits like EternalBlue or Null Sessions.
- **Tomcat 1.1 & Jetty**: Often misconfigured or allow file uploads.

---

## 📝 Notes

- Next step: Cross-reference versions with SearchSploit
- Target is a goldmine for exploitation in future phases
