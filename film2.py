import tkinter as tk
from PIL import Image, ImageTk
from reserveren import FilmsReservationApp as fr
class Films2App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Guardians of the galaxy vol. 3")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#00368c")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bgImage = tk.PhotoImage(file="afbeeldingen/film_achtergrond2.png")
        self.bgLabel = tk.Label(self, image=self.bgImage)
        self.bgLabel.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="Guardians of the galaxy vol. 3", background="#E7B0F8", foreground="#fcffff",
                         font=("Arial", 22, "bold"))
        label.place(x=80, y=100)

        # Afbeelding film
        film1Image = Image.open("afbeeldingen/film2.png")  # Opent het beeldbestand "afbeeldingen/film2.png"
        resized_film1Image = film1Image.resize((200, 300))  # Verkleint de afbeelding
        self.film1Photo = ImageTk.PhotoImage(resized_film1Image)  # Maakt een PhotoImage-object van de verkleinde afbeelding
        film1Label = tk.Label(self, image=self.film1Photo)  # Maakt een Label-widget met de afbeelding
        film1Label.config(borderwidth=0)  # Stelt de randbreedte van het label in op 0
        film1Label.place(x=150, y=160)  # Plaatst het label op de gewenste positie

        # Tekst
        label = tk.Label(self, text="Duration: 150 Minutes", background="#E7B0F8", foreground="#fcffff",
                         font=("Arial", 15, "bold"))
        label.place(x=145, y=480)

        label = tk.Label(self, text="Director: James Gunn", background="#E7B0F8", foreground="#fcffff",
                         font=("Arial", 15, "bold"))
        label.place(x=145, y=530)

        label = tk.Label(self,
                         text="Description:\n\n Still reeling from the loss of Gamora,\n Peter Quill rallies his team to defend\n the universe and one of their own.\n a mission that could mean the end of\n the Guardians if not successful.",
                         background="#E7B0F8", foreground="#fcffff", font=("Arial", 15, "bold"))
        label.place(x=460, y=150)

        label = tk.Label(self, text="Cast:\n\n Chris Pratt, Zoë Saldana, Will Poulter,\n Dace Bautista,Vin Diesel, Pom Klementieff",
                         background="#E7B0F8", foreground="#fcffff", font=("Arial", 15, "bold"))
        label.place(x=440, y=340)

        # Button
        button_style = {
            "font": ("Arial", 14),
            "bg": "#800080",
            "fg": "#fcffff",
            "relief": tk.RAISED, # Style van de button
            "bd": 3, # Border width
            "width": 15,
            "height": 2,
        }

        def button():
            Films2App.destroy(self)
            fr()

        button = tk.Button(self, text="Reserveren", command=button, **button_style)
        button.place(x=645, y=525, anchor=tk.CENTER)

if __name__ == "__main__":
    app = Films2App()
    app.mainloop()
