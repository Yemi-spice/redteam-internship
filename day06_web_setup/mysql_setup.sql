-- MariaDB root password setup
ALTER USER 'root'@'localhost' IDENTIFIED BY 'YourStrongRootPassword';
FLUSH PRIVILEGES;

-- DVWA database and user
CREATE DATABASE dvwa;
CREATE USER 'dvwauser'@'localhost' IDENTIFIED BY 'dvwapass';
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwauser'@'localhost';
FLUSH PRIVILEGES;
