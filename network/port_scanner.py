import socket

def scan_ports(target, start_port, end_port):
    print(f"\n[+] Escaneando {target} desde {start_port} hasta {end_port}\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Puerto {port}")

            sock.close()

        except Exception as e:
            print(f"[ERROR] {e}")
            break
