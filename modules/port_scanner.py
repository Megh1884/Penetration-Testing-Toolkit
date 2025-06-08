import socket

def auto_scan_ports(host, start_port=1, end_port=100):  # reduced range for quick test
    print(f"[+] Scanning {host} from port {start_port} to {end_port}...")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)  # reduced timeout
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[*] Port {port} is OPEN")
                open_ports.append(port)
            else:
                print(f"[x] Port {port} is CLOSED")
            sock.close()
        except socket.error as e:
            print(f"[!] Error on port {port}: {e}")

    print(f"\n[✓] Scanning complete. {len(open_ports)} open ports found.")
    if open_ports:
        print(f"[+] Open ports: {open_ports}")
    else:
        print("[i] No open ports found.")
