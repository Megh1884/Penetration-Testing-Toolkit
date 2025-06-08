# Penetration Testing Toolkit

A modular penetration testing toolkit developed in Python, designed to help security enthusiasts and professionals perform basic penetration testing tasks.  
This toolkit currently includes two main modules:

- **Port Scanner**: Automatically scans an IP address to find open ports.
- **SSH Brute Forcer**: Attempts to brute-force SSH login credentials using a password list.

---

## Features

- Easy-to-use command line interface.
- Modular design for adding more penetration testing tools.
- Supports scanning common ports (1-1024) for open services.
- Simple SSH brute-force attack simulation or real attack (if SSH server is accessible).

---

## Installation

1. Clone the repository or download the source code.

2. Install required Python packages:
   ```bash
   pip install paramiko colorama requests
