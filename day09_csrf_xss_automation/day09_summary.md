# Day 9 – CSRF + XSS Automation Summary

## Objectives
- Identify CSRF vulnerabilities via manual inspection.
- Automate XSS detection using Python.

## Key Actions
- Manually tested DVWA’s password change page for CSRF.
- Captured request and verified exploit worked with no token.
- Wrote and ran `xss_scanner.py` against the Reflected XSS module.
- Logged reflected payloads to confirm vulnerability.

## Results
- DVWA CSRF module lacks basic protection (GET used for password change).
- Several payloads successfully reflected, confirming Reflected XSS.
- Logs and screenshots captured for both tests.

## Next Steps
- Explore Blind XSS detection using external payload collectors.
- Enhance Python scanner to crawl or fuzz deeper pages.
