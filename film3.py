import tkinter as tk
from PIL import Image, ImageTk
from reserveren import FilmsReservationApp as fr
class Films3App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fast X")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#BC1823")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bgImage = Image.open("afbeeldingen/film_achtergrond3.png")
        self.bgPhoto = ImageTk.PhotoImage(self.bgImage)
        self.bgLabel = tk.Label(self, image=self.bgPhoto)
        self.bgLabel.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="Fast X", background="#2E2C2B", foreground="#fcffff",
                         font=("Ariel", 22, "bold"))
        label.place(x=200, y=100)

        # Afbeelding film
        filmImage = Image.open("afbeeldingen/film3.png")  # Opent het beeldbestand "afbeeldingen/film3.png"
        resizedFilmImage = filmImage.resize((200, 300))  # Verkleint de afbeelding
        self.filmPhoto = ImageTk.PhotoImage(resizedFilmImage)  # Maakt een PhotoImage-object van de verkleinde afbeelding
        filmLabel = tk.Label(self, image=self.filmPhoto)  # Maakt een Label-widget met de afbeelding
        filmLabel.config(borderwidth=0)  # Stelt de randbreedte van het label in op 0
        filmLabel.place(x=150, y=160)  # Plaatst het label op de gewenste positie

        # Tekst
        label = tk.Label(self, text="Duration: 141 Minutes", background="#2E2C2B", foreground="#fcffff",
                         font=("Ariel", 15, "bold"))
        label.place(x=145, y=480)

        label = tk.Label(self, text="Director: Louis Leterrier", background="#2E2C2B", foreground="#fcffff",
                         font=("Ariel", 15, "bold"))
        label.place(x=145, y=530)

        label = tk.Label(self, text="Description:\n\nDom Toretto and his family\nare targeted by Dante Reyes,\nwho seeks revenge for his father's death\nand loss of his family's fortune.",
                         background="#2E2C2B", foreground="#fcffff", font=("Ariel", 15, "bold"))
        label.place(x=460, y=150)

        label = tk.Label(self, text="Cast:\n\nVin Diesel, Jason Statham, Michelle Rodrigues,\nLudacris, Jason Momoa, Brie Larson",
                         background="#2E2C2B", foreground="#fcffff", font=("Ariel", 15, "bold"))
        label.place(x=430, y=340)

        # Button
        button_style = {
            "font": ("Arial", 14),
            "bg": "#BC1823",
            "fg": "#fcffff",
            "relief": tk.RAISED, # Style van de button
            "bd": 3, # Border width
            "width": 15,
            "height": 2,
        }

        def button():
            Films3App.destroy(self)
            fr()

        self.button = tk.Button(self, text="Reserveren", command=button, **button_style)
        self.button.place(x=655, y=525, anchor=tk.CENTER)


if __name__ == "__main__":
    app = Films3App()
    app.mainloop()
