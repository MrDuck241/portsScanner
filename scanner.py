import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

openPorts = {}

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) 
    result = sock.connect_ex((ip, port)) 
    if result == 0:
        try:
            
            service = socket.getservbyport(port)
        except OSError:

            service = "Nieznana usługa"
        #print(f"Port {port} jest otwarty, Usługa: {service}")
        openPorts.add({port, service})
    sock.close()


def scan_ports(ip, start_port, end_port):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for port in range(start_port, end_port):
            executor.submit(scan_port, ip, port)
    return openPorts

def main(ip, start_port, end_port):



    #print(f"Skanowanie adresu {args.ip} w zakresie portów od {args.start_port} do {args.end_port}...")
    values = scan_ports(ip, int(start_port), int(end_port))
    return values