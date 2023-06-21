import tkinter as tk
from PIL import Image, ImageTk
from reserveren import FilmsReservationApp as fr
class Films1App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Little Mermaid")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#00368c")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bgImage = tk.PhotoImage(file="afbeeldingen/film_achtergrond1.png")
        self.bgLabel = tk.Label(self, image=self.bgImage)
        self.bgLabel.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="The Little Mermaid", background="#4942E4", foreground="#fcffff",
                         font=("Arial", 25, "bold"))
        label.place(x=110, y=95)

        # Afbeelding film
        film1Image = Image.open("afbeeldingen/film1.png")  # Opent het beeldbestand "afbeeldingen/film1.png"
        resized_film1Image = film1Image.resize((200, 300))  # Verkleint de afbeelding
        self.film1Photo = ImageTk.PhotoImage(resized_film1Image)  # Maakt een PhotoImage-object van de verkleinde afbeelding
        film1Label = tk.Label(self, image=self.film1Photo)  # Maakt een Label-widget met de afbeelding
        film1Label.config(borderwidth=0)  # Stelt de randbreedte van het label in op 0
        film1Label.place(x=150, y=160)  # Plaatst het label op de gewenste positie

        # Tekst
        label = tk.Label(self, text="Duration: 135 Minutes", background="#4942E4", foreground="#fcffff",
                         font=("Arial", 15, "bold"))
        label.place(x=145, y=480)

        label = tk.Label(self, text="Director: Rob Marshall", background="#4942E4", foreground="#fcffff",
                         font=("Arial", 15, "bold"))
        label.place(x=145, y=530)

        label = tk.Label(self, text="Description:\n\nA young mermaid makes a deal\nwith a sea witch to trade her beautiful voice for\nhuman legs so she can discover the world\nabove water and impress a prince.",
                         background="#4942E4", foreground="#fcffff", font=("Arial", 15, "bold"))
        label.place(x=410, y=150)

        label = tk.Label(self, text="Cast:\n\nHalle Bailey, Jonah Hauer-King,\nMelissa McCarthy, Javier Bardem,\nNoma Dumezweni",
                         background="#4942E4", foreground="#fcffff", font=("Arial", 15, "bold"))
        label.place(x=470, y=325)

        # Button
        button_style = {
            "font": ("Arial", 14),
            "bg": "#00368c",
            "fg": "#fcffff",
            "relief": tk.RAISED, # Style van de button
            "bd": 3, # Border width
            "width": 15,
            "height": 2,
        }

        button = tk.Button(self, text="Reserveren", command=self.button, **button_style)
        button.place(x=635, y=525, anchor=tk.CENTER)
    def button(self):
        Films1App.destroy(self)
        fr()


if __name__ == "__main__":
    app = Films1App()
    app.mainloop()
