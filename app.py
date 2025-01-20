import tkinter as tk

def on_circle_click(event):
    print(f"Kliknięto na kole w pozycji: {event.x}, {event.y}")

def create_app():
    root = tk.Tk()
    root.title("Prosta aplikacja graficzna")

    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # Rysowanie prostokąta
    canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="black")

    # Rysowanie koła
    circle = canvas.create_oval(200, 50, 300, 150, fill="red", outline="black")

    # Dodanie tekstu
    canvas.create_text(250, 100, text="Kliknij mnie", fill="white", font=("Arial", 12))

    # Obsługa zdarzeń - kliknięcie na koło
    canvas.tag_bind(circle, "<Button-1>", on_circle_click)

    root.mainloop()

if __name__ == "__main__":
    create_app()
