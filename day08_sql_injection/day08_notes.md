# Day 8 – SQL Injection

## Set DVWA Security
- URL: http://192.168.56.101/dvwa/security.php
- Level: Low


## Log Interpretation

- **Banner:** `'11.8.2-MariaDB-1 from Debian'` indicates the target uses MariaDB, a MySQL fork, version 11.8.2 on Debian Linux.
- **Injection Type:** Time-based blind SQL injection detected via `SLEEP()` function shows database is vulnerable to blind techniques.
- **UNION Query:** Successfully used to extract data from database tables, confirming full exploitation possible.
- **Requests:** Total of 75 HTTP requests sent by sqlmap indicates a thorough enumeration process.
