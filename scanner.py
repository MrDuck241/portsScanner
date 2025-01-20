import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) 
    result = sock.connect_ex((ip, port)) 
    if result == 0:
        try:
     
            service = socket.getservbyport(port)
        except OSError:

            service = "Nieznana usługa"
        print(f"Port {port} jest otwarty, Usługa: {service}")
    sock.close()


def scan_ports(ip, start_port, end_port):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

def main():
    parser = argparse.ArgumentParser(description="Skaner portów")
    parser.add_argument("ip", help="Adres IP, który ma zostać zeskanowany")
    parser.add_argument("start_port", type=int, help="Początkowy port")
    parser.add_argument("end_port", type=int, help="Końcowy port")

    args = parser.parse_args()

    print(f"Skanowanie adresu {args.ip} w zakresie portów od {args.start_port} do {args.end_port}...")
    scan_ports(args.ip, args.start_port, args.end_port)

main()