# examples/vulnerable.py

password = "admin123"

query = "SELECT * FROM users WHERE username = '" + user_input + "'"

eval("os.system('rm -rf /')")
