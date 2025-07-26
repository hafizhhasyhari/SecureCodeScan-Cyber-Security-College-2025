# main.py

import os
from scanners import python_scanner

def scan_file(path):
    if path.endswith('.py'):
        results = python_scanner.scan_python_file(path)
        if results:
            print(f"Results for {path}:")
            for line_num, issue in results:
                print(f"  Line {line_num}: {issue}")
        else:
            print(f"No issues found in {path}")
    else:
        print("File type not supported yet.")

if __name__ == '__main__':
    target_file = "examples/vulnerable.py"  # ganti dengan file target
    scan_file(target_file)
