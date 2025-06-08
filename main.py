from modules import port_scanner, brute_forcer

def main():
    print("=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. SSH Brute Forcer")
    choice = input("Select a module (1/2): ")

    if choice == '1':
        target = input("Enter target IP: ")
        port_scanner.auto_scan_ports(target)

    elif choice == '2':
        target = input("Enter SSH target IP: ")
        port = int(input("Enter port (default 22): ") or 22)
        username = input("Enter username: ")
        try:
            with open("common_passwords.txt") as f:
                passwords = f.read().splitlines()
        except FileNotFoundError:
            print("[x] common_passwords.txt not found.")
            return
        brute_forcer.ssh_brute_force(target, port, username, passwords)

if __name__ == "__main__":
    main()
