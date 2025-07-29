# 🔍 Full TCP Port & OS Detection Scan – DVWA (192.168.56.102)

**Date:** 2025-07-28  
**Target:** OWASP BWA / DVWA  
**Attacker Machine:** Kali (192.168.56.101)  
**Scanner:** Nmap v7.95

---

## 🎯 Objective
Perform a full TCP scan with OS and version detection to identify all open ports, running services, and fingerprint the target OS for further exploitation.

---

## 🛠 Command Used

```bash
nmap -p- -A -T4 -oN dvwa_full_tcp_os_scan.txt 192.168.56.102
