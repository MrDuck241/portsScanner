import tkinter as tk
import scanner as sc
from datetime import datetime

open_ports = []

def create_app():
    # Utworzenie głównego okna
    root = tk.Tk()
    root.title("Ports Scanner")

    # Utworzenie canvas
    canvas = tk.Canvas(root, width=1000, height=600, bg="grey")
    canvas.pack()

    # Dodanie linii i tekstów tytułowych
    canvas.create_line(0, 80, 1000, 80, fill="black", width=2)
    canvas.create_text(14, 25, text="Ports Scanner", fill="green", font=("Arial", 16), anchor="nw")

    # Pola tekstowe i etykiety
    canvas.create_text(235, 15, text="IP Address", fill="black", font=("Arial", 12), anchor="nw")
    ip_address = tk.Entry(root, bd=2, width=16)
    canvas.create_window(270, 50, window=ip_address)

    canvas.create_text(408, 15, text="Start Port", fill="black", font=("Arial", 12), anchor="nw")
    start_port = tk.Entry(root, bd=2, width=16)
    canvas.create_window(440, 50, window=start_port)

    canvas.create_text(580, 15, text="End Port", fill="black", font=("Arial", 12), anchor="nw")
    end_port = tk.Entry(root, bd=2, width=16)
    canvas.create_window(610, 50, window=end_port)

    # Dodanie przycisku "Scan"
    canvas.create_rectangle(720, 15, 820, 70, outline="black", fill="#4C6A4E", width=2, tags="scanButton")
    canvas.create_text(770, 40, text="Scan", fill="white", font=("Arial", 16, "bold"), anchor="center")

    # Dodanie przycisku "Save"
    canvas.create_rectangle(860, 15, 960, 70, outline="black", fill="#4C6A4E", width=2, tags="saveButton")
    canvas.create_text(910, 40, text="Save", fill="white", font=("Arial", 16, "bold"), anchor="center")

    # Listbox do wyświetlania wyników
    results_listbox = tk.Listbox(root, height=20, width=70)
    results_listbox.place(x=50, y=150)

    # Funkcja wywoływana po kliknięciu przycisku "Scan"
    def on_scan_click():
        global open_ports
        results_listbox.delete(0, tk.END)  # Czyszczenie poprzednich wyników
        ip = ip_address.get().strip()
        start = start_port.get().strip()
        end = end_port.get().strip()

        if not ip or not start or not end:
            results_listbox.insert(tk.END, "Please provide all input data: IP, Start Port, End Port")
            return

        try:
            start = int(start)
            end = int(end)
            if start > end:
                results_listbox.insert(tk.END, "Start port must be less than end port")
                return
            if start < 0 or end <= 0:
                results_listbox.insert(tk.END, "Invalid ports numbers values")
                return
            
        except ValueError:
            results_listbox.insert(tk.END, "Ports must be valid number")
            return

        try:
            results_listbox.insert(tk.END, f"Scanning {ip} from port {start} to {end}...")
            root.update()  # Aktualizacja interfejsu
            open_ports = sc.main(ip, start, end)

            if open_ports:
                results_listbox.insert(tk.END, "Open ports found:")
                for port, service in open_ports:
                    results_listbox.insert(tk.END, f"Port {port}: {service}")
            else:
                results_listbox.insert(tk.END, "No open ports found.")
        except Exception as e:
            results_listbox.insert(tk.END, f"Error: {e}")

    def on_save_click():

        if not open_ports:
            results_listbox.insert(tk.END, "No ports to save!")
            return
        
        with open("portsData.txt", "a") as file:
            file.write(f"Scanning date: {datetime.now()}\n")
            file.write("Detected open ports:\n")

            for port, service in open_ports:
                file.write(f"Port {port} opened | Service: {service}\n")
            file.write("End of scanned ports\n\n")
        results_listbox.insert(tk.END, "Results saved to portsData.txt")

    canvas.tag_bind("scanButton", "<Button-1>", lambda event: on_scan_click())
    canvas.tag_bind("saveButton", "<Button-1>", lambda event: on_save_click())

    def highlight_scan_button(event):
        canvas.itemconfig("scanButton", fill="#6B8E23")

    def reset_scan_button(event):
        canvas.itemconfig("scanButton", fill="#4C6A4E")

    def highlight_save_button(event):
        canvas.itemconfig("saveButton", fill="#6B8E23")

    def reset_save_button(event):
        canvas.itemconfig("saveButton", fill="#4C6A4E")

    canvas.tag_bind("scanButton", "<Enter>", highlight_scan_button)
    canvas.tag_bind("scanButton", "<Leave>", reset_scan_button)
    
    canvas.tag_bind("saveButton", "<Enter>", highlight_save_button)
    canvas.tag_bind("saveButton", "<Leave>", reset_save_button)

    # Uruchomienie pętli głównej
    root.mainloop()


if __name__ == "__main__":
    create_app()
