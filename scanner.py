import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        if sock.connect_ex((ip, port)) == 0:  # Port otwarty
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown Service"
            results.append((port, service))  # Dodanie wyniku do listy
        sock.close()
    except Exception as e:
        pass

def scan_ports(ip, start_port, end_port):
    #Skanuje porty i zwraca listę otwartych
    results = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port, results)
    return results

def main(ip, start_port, end_port):
    open_ports = scan_ports(ip, start_port, end_port)
    return open_ports
