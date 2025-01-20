import tkinter as tk

def create_app():
    root = tk.Tk()
    root.title("Ports Scanner")

    # Utworzenie canvas
    canvas = tk.Canvas(root, width=1000, height=600, bg="grey")
    canvas.pack()

    # Pobranie rozmiarów canvas po jego utworzeniu
    root.update_idletasks()  # Aktualizacja GUI, aby uzyskać wymiary
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    canvas.create_line(0, 80, 1000, 80, fill="black", width=2)  # Linia pozioma

    canvas.create_text(14, 25, text="Ports Scanner", fill="green", font=("Arial", 16), anchor="nw")

    canvas.create_text(235, 15, text="Ip address", fill="black", font=("Arial", 12), anchor="nw")
    canvas.create_rectangle(220, 40, 320, 65, outline="black", fill="white")

    canvas.create_text(408, 15, text="Start port", fill="black", font=("Arial", 12), anchor="nw")
    canvas.create_rectangle(390, 40, 490, 65, outline="black", fill="white")

    canvas.create_text(580, 15, text="End port", fill="black", font=("Arial", 12), anchor="nw")
    canvas.create_rectangle(560, 40, 660, 65, outline="black", fill="white")

    canvas.create_rectangle(770, 30, 870, 70, outline="black", fill="grey")
    canvas.create_text(798, 37, text="Scan", fill="green", font=("Arial", 16), anchor="nw")

    canvas.create_text(85, 110, text="Detected opened ports", fill="green", font=("Arial", 16), anchor="nw")

  # Utworzenie frame dla Listbox i Scrollbar
    frame = tk.Frame(root)
    frame.place(x=40, y=150)  # Ustawienie lokalizacji ramki w oknie

    # Utworzenie Scrollbar
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)

    # Utworzenie Listbox
    listbox = tk.Listbox(frame, height=20, width=50, yscrollcommand=scrollbar.set)

    # Dodawanie elementów do listy
    for i in range(100):  # Lista z 100 elementami
        listbox.insert(tk.END, f"Element {i+1}")

    # Powiązanie Scrollbar z Listbox
    scrollbar.config(command=listbox.yview)

    # Umieszczanie Listbox i Scrollbar w ramce
    listbox.pack(side=tk.LEFT)  # Używamy pack() do umieszczenia listy
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    root.mainloop()

if __name__ == "__main__":
    create_app()
