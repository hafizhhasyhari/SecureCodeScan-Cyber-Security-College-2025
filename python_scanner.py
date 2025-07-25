# scanners/python_scanner.py

import re

# Deteksi pola sederhana dalam file Python
def scan_python_file(filepath):
    findings = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if re.search(r'password\s*=\s*["\'].*["\']', line):
                findings.append((i+1, "Hardcoded password"))
            if re.search(r'cursor\.execute\(.+\+.+\)', line):
                findings.append((i+1, "Possible SQL Injection (unsafe query)"))
            if 'eval(' in line:
                findings.append((i+1, "Use of eval() is dangerous"))
    return findings
