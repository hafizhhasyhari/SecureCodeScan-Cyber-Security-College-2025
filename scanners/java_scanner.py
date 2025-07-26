import re

# Fungsi untuk memindai file Java
def scan_java_file(filepath):
    findings = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            # Deteksi hardcoded password
            if re.search(r'String\s+\w*\s*password\s*=\s*".+";', line):
                findings.append((i+1, "Hardcoded password"))

            # Deteksi SQL Injection (query digabung string)
            if re.search(r'String\s+\w*\s*=\s*".*"\s*\+\s*\w+', line) and "SELECT" in line.upper():
                findings.append((i+1, "Possible SQL Injection (unsafe concatenation in query)"))

            # Deteksi penggunaan Runtime exec
            if re.search(r'Runtime\.getRuntime\(\)\.exec\(', line):
                findings.append((i+1, "Use of Runtime.exec() is dangerous"))

            # Deteksi XSS jika output langsung println input
            if re.search(r'out\.println\(\s*\w+\s*\)', line):
                findings.append((i+1, "Potential XSS: Unvalidated user input in out.println()"))
    return findings
