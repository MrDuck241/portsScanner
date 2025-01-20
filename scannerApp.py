import tkinter as tk
import scanner as sc
import argparse

def create_app():
    # Utworzenie głównego okna
    root = tk.Tk()
    root.title("Ports Scanner")

    # Utworzenie canvas
    canvas = tk.Canvas(root, width=1000, height=600, bg="grey")
    canvas.pack()

    # Pobranie rozmiarów canvas po jego utworzeniu
    root.update_idletasks()  # Aktualizacja GUI, aby uzyskać wymiary
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Dodanie poziomej linii
    canvas.create_line(0, 80, 1000, 80, fill="black", width=2)

    # Dodanie tekstu "Ports Scanner"
    canvas.create_text(14, 25, text="Ports Scanner", fill="green", font=("Arial", 16), anchor="nw")

    # Dodanie tekstów i Entry dla IP, portu początkowego i końcowego
    canvas.create_text(235, 15, text="Ip address", fill="black", font=("Arial", 12), anchor="nw")
    ip_address = tk.Entry(root, bd=2, width=16)
    canvas.create_window(270, 50, window=ip_address)

    canvas.create_text(408, 15, text="Start port", fill="black", font=("Arial", 12), anchor="nw")
    start_port = tk.Entry(root, bd=2, width=16)
    canvas.create_window(440, 50, window=start_port)

    canvas.create_text(580, 15, text="End port", fill="black", font=("Arial", 12), anchor="nw")
    end_port = tk.Entry(root, bd=2, width=16)
    canvas.create_window(610, 50, window=end_port)

    ##################################################
    # Stworzenie zaokrąglonego prostokąta (przycisk)
    # Zaokrąglony przycisk z gradientem
    canvas.create_rectangle(765, 15, 875, 70, outline="black", fill="#4C6A4E", width=2, tags="button")

    # Tekst na przycisku
    canvas.create_text(820, 40, text="Scan", fill="white", font=("Arial", 16, "bold"), anchor="center")

    # Funkcja uruchamiana po kliknięciu przycisku "Scan"
    def on_scan_click():
        ip_address_value = ip_address.get()  # Pobranie wartości z pola IP
        start_port_value = start_port.get()
        end_port_value = end_port.get()
        print(f"IP Address: {ip_address_value}")  # Wyświetlenie w konsoli
        print(f"Start port: {start_port_value}")
        print(f"End port: {end_port_value}")
        openPorts = sc.main(ip_address_value, start_port_value, end_port_value)
        print("Scanned ports from module")
        for val in openPorts:
            print(val)

    # Zdarzenia przycisku
    canvas.tag_bind("button", "<Button-1>", lambda event: on_scan_click())

    # Efekty najechania na przycisk
    def highlight_button(event):
        canvas.itemconfig("button", fill="#6B8E23")

    def reset_button(event):
        canvas.itemconfig("button", fill="#4C6A4E")

    # Zdarzenia przycisku
    canvas.tag_bind("button", "<Enter>", highlight_button)
    canvas.tag_bind("button", "<Leave>", reset_button)
    ##################################################

    # Dodanie tekstu "Detected opened ports"
    canvas.create_text(85, 110, text="Detected opened ports", fill="green", font=("Arial", 16), anchor="nw")

    # Dodanie pionowej linii
    canvas.create_line(440, 80, 440, 600, fill="black", width=2)

    # Utworzenie frame dla Listbox i Scrollbar
    frame = tk.Frame(root)
    frame.place(x=40, y=150)

    # Utworzenie Scrollbar
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)

    # Utworzenie Listbox
    listbox = tk.Listbox(frame, height=20, width=50, yscrollcommand=scrollbar.set)

    # Dodanie elementów do Listbox
    for i in range(100):  # Lista z 100 elementami
        listbox.insert(tk.END, f"Element {i + 1}")

    # Powiązanie Scrollbar z Listbox
    scrollbar.config(command=listbox.yview)

    # Umieszczanie Listbox i Scrollbar w ramce
    listbox.pack(side=tk.LEFT)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Uruchomienie głównej pętli
    root.mainloop()

if __name__ == "__main__":
    #openPorts = sc.main()
    #print("Opened ports lists from scanner.py")
    create_app()

