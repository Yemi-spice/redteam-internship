# 🧪 Day 4 – Web Recon Summary

## Target: 192.168.56.102 (DVWA/WordPress)

---

### 🔍 Tools Used
- Nikto
- WPScan (API)
- Gobuster

---

### 🔓 Key Findings

#### WordPress:
- Version: 2.0 (16+ core vulns)
- Plugin: `myGallery` – Unauthenticated File Inclusion (CVE-2007-2426)
- Theme: `Classic` – XSS (CVE-2007-4483)
- User Found: `admin`
- XML-RPC Enabled

#### Sensitive Files:
- `.bash_history`, `.svn`, `#wp-config.php#`

#### Interesting Folders:
- `/evil/`, `/test/`, `/gallery2/`, `/phpmyadmin/`, `/phpBB2/`, `/cgi-bin/`

---

✍ **Intern:** Ahmed “Yemi-spice”  
📅 Day 4 – Web Enumeration Complete
