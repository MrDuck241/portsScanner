from scapy.all import sr1, IP, TCP

def detect_os(ip):
    try:
        # Przygotowanie pakietu TCP SYN
        pkt = IP(dst=ip)/TCP(dport=80, flags="S")
        response = sr1(pkt, timeout=2, verbose=0)

        if response is None:
            return "Nie można określić systemu operacyjnego (brak odpowiedzi)"

        # Analiza odpowiedzi
        ttl = response.ttl
        window_size = response[TCP].window if TCP in response else None
        flags = response[TCP].flags if TCP in response else ""

        # Prosta heurystyka systemów operacyjnych
        if "R" in flags:  # Reset flag
            if ttl <= 64:
                return f"Linux (port odrzucony) TTL value {ttl}"
            elif ttl <= 128:
                return f"Windows (port odrzucony) TTL value {ttl}"
            else:
                return f"Router lub urządzenie sieciowe (port odrzucony) TTL value {ttl}"

        if ttl <= 64:
            if window_size == 64240:
                return f"Linux TTL value {ttl}"
            elif window_size == 65535:
                return f"FreeBSD/Unix TTL value {ttl}"
        elif ttl <= 128:
            if window_size == 8192:
                return f"Windows TTL value {ttl}"
            elif window_size == 65535:
                return f"Windows Server TTL value {ttl}"
        elif ttl > 128:
            return f"Router lub urządzenie sieciowe TTL value {ttl}"

        return f"Nieznany system operacyjny TTL value {ttl}"
    except Exception as e:
        return f"Błąd podczas detekcji systemu: {e} TTL value {ttl}"
