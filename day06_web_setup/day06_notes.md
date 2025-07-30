# 🧪 Day 6 Lab Notes – DVWA Setup + Burp Suite Interception

---

## ✅ DVWA Installation & Configuration (Kali Linux)

### 1. Update System & Install DVWA
```bash
sudo apt update
sudo apt install dvwa -# Day 6 Notes – DVWA Setup + Burp Suite

## 🧰 DVWA & MariaDB Setup

```bash
# Update & install DVWA
sudo apt update && sudo apt install dvwa -y

# Start required services
sudo systemctl start apache2
sudo systemctl start mariadb
sudo systemctl enable apache2
sudo systemctl enable mariadb

# Copy DVWA to web root
sudo cp -r /usr/share/dvwa /var/www/html/
sudo chown -R www-data:www-data /var/www/html/dvwa
sudo chmod -R 755 /var/www/html/dvwa

🛢️ MariaDB Configuration
sql
Copy code
# Access MariaDB
sudo mariadb

# Set root password (if needed)
ALTER USER 'root'@'localhost' IDENTIFIED BY 'YourStrongRootPassword';
FLUSH PRIVILEGES;

# Create DVWA DB & user
CREATE DATABASE dvwa;
CREATE USER 'dvwauser'@'localhost' IDENTIFIED BY 'dvwapass';
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwauser'@'localhost';
FLUSH PRIVILEGES;
🌐 DVWA Access & Setup
Navigate to http://192.168.56.101/dvwa/setup.php

Click "Create / Reset Database"

🛡️ Burp Suite Workflow
Launch Burp: burpsuite

Configure Firefox proxy: 127.0.0.1:8080

Intercept DVWA login request (Proxy → Intercept)

Forward to Repeater → Send → Analyze HTTP response
