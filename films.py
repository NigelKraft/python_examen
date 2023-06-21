import tkinter as tk
from PIL import Image, ImageTk
from film1 import Films1App as f1
from film2 import Films2App as f2
from film3 import Films3App as f3
class FilmsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Movies")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#FF914D")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bg2Image = tk.PhotoImage(file="afbeeldingen/main_achtergrond.png")
        self.bg2Label = tk.Label(self, image=self.bg2Image)
        self.bg2Label.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="|Current film offer in the cinema|", background="#FFBD59",
                         foreground="#fcffff", font=("Arial", 32, "bold"))
        label.place(x=160, y=75)

        # Films
        film1Image = Image.open("afbeeldingen/film1.png")  # Opent het beeldbestand "afbeeldingen/film1.png"
        resized_film1Image = film1Image.resize((179, 254))  # Verkleint de afbeelding
        self.film1Photo = ImageTk.PhotoImage(resized_film1Image)  # Maakt een PhotoImage-object van de verkleinde afbeelding
        film1Label = tk.Label(self, image=self.film1Photo)  # Maakt een Label-widget met de afbeelding
        film1Label.config(borderwidth=0)  # Stelt de randbreedte van het label in op 0
        film1Label.place(x=165, y=180)  # Plaatst het label op de gewenste positie

        film2Image = Image.open("afbeeldingen/film2.png")
        resized_film2Image = film2Image.resize((179, 254))
        self.film2Photo = ImageTk.PhotoImage(resized_film2Image)
        film2Label = tk.Label(self, image=self.film2Photo)
        film2Label.config(borderwidth=0)
        film2Label.place(x=410, y=180)

        film3Image = Image.open("afbeeldingen/film3.png")
        resized_film3Image = film3Image.resize((179, 254))
        self.film3Photo = ImageTk.PhotoImage(resized_film3Image)
        film3Label = tk.Label(self, image=self.film3Photo)
        film3Label.config(borderwidth=0)
        film3Label.place(x=650, y=180)

        # Filmtekst
        label = tk.Label(self, text="The little mermaid", background="#FFBD59", foreground="#fcffff",
                         font=("Arial", 12, "bold"))
        label.place(x=185, y=440)

        label = tk.Label(self, text="Guardians of the galaxy vol. 3", background="#FFBD59", foreground="#fcffff",
                         font=("Arial", 12, "bold"))
        label.place(x=385, y=440)

        label = tk.Label(self, text="Fast X", background="#FFBD59", foreground="#fcffff",
                         font=("Arial", 12, "bold"))
        label.place(x=710, y=440)

        # Buttons
        button_style = {
            "font": ("Arial", 14),
            "bg": "#FF914D",
            "fg": "black",
            "relief": tk.RAISED, # Style van de button
            "bd": 3, # Border width
            "width": 10,
            "height": 2,
        }

        button1 = tk.Button(self, text="Info", command=self.button1_click, **button_style)
        button1.place(x=255, y=520, anchor=tk.CENTER)

        button2 = tk.Button(self, text="Info", command=self.button2_click, **button_style)
        button2.place(x=495, y=520, anchor=tk.CENTER)

        button3 = tk.Button(self, text="Info", command=self.button3_click, **button_style)
        button3.place(x=740, y=520, anchor=tk.CENTER)

    def button1_click(self):
        FilmsApp.destroy(self)
        f1()

    def button2_click(self):
        FilmsApp.destroy(self)
        f2()

    def button3_click(self):
        FilmsApp.destroy(self)
        f3()

app = FilmsApp()
app.mainloop()
