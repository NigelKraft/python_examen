import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pytz

class FilmsReservationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reservation")
        self.geometry("990x660+50+50")
        self.resizable(False, False)
        self.config(bg="#ED5EAB")

        self.create_widgets()

    def create_widgets(self):
        # Achtergrond
        self.bgImage = tk.PhotoImage(file="afbeeldingen/reserveren_achtergrond.png")
        self.bgLabel = tk.Label(self, image=self.bgImage)
        self.bgLabel.place(x=0, y=0)

        # Titel
        label = tk.Label(self, text="|Reserve|", background="#FFAEE2", foreground="#fcffff", font=("Ariel", 32, "bold"))
        label.place(x=390, y=75)

        # Film_keuzes
        dropdown_label = Label(self, text="Movies", font=("Ariel", 15, "bold"), bg="#FFAEE2", fg="#fcffff")
        dropdown_label.place(x=440, y=165)

        choices = ["The little mermaid", "Guardians of the galaxy vol. 3", "Fast X"]
        self.selected_option = StringVar()
        self.selected_option.set(choices[0])

        dropdown = OptionMenu(self, self.selected_option, *choices)
        dropdown.config(width=25, highlightbackground="#FFAEE2")
        dropdown.place(x=385, y=200)

        # Aanwezigen
        attendees_label = Label(self, text="Number of People", font=("Ariel", 15, "bold"), bg="#FFAEE2", fg="#fcffff")
        attendees_label.place(x=395, y=270)

        self.selected_attendees = StringVar()
        self.selected_attendees.set("1")

        attendees_spinbox = Spinbox(self, textvariable=self.selected_attendees, from_=1, to=10, font=("Arial", 12), width=5)
        attendees_spinbox.place(x=450, y=310)

        # Tijd keuze
        time_label = Label(self, text="Time Selection", font=("Arial", 15, "bold"), bg="#FFAEE2", fg="#fcffff")
        time_label.place(x=410, y=360)

        self.selected_time = tk.StringVar()

        amsterdam_tz = pytz.timezone("Europe/Amsterdam") # Hier word de actuele tijd van amsterdam gehaald
        current_time = datetime.now(amsterdam_tz).time()

        time1 = datetime.strptime("10:06", "%H:%M").time() # Hier word gekeken welke tijd beschikbaar is om te laten zien
        time2 = datetime.strptime("12:06", "%H:%M").time() # Hier word gekeken welke tijd beschikbaar is om te laten zien
        time3 = datetime.strptime("20:06", "%H:%M").time() # Hier word gekeken welke tijd beschikbaar is om te laten zien
        time4 = datetime.strptime("22:06", "%H:%M").time() # Hier word gekeken welke tijd beschikbaar is om te laten zien

        time_choices = []
        if current_time <= time1:
            time_choices.append("10:00")
        if current_time <= time2:
            time_choices.append("12:00")
        if current_time <= time3:
            time_choices.append("20:00")
        if current_time <= time4:
            time_choices.append("22:00")

        if time_choices:
            self.selected_time.set(time_choices[0]) # Hier kiest je de eerst tijd die beschikbaar is
            time_dropdown = OptionMenu(self, self.selected_time, *time_choices) # Hier maakt die de dropdown
        else:
            self.selected_time.set("No available time") # Hier geeft die aan dat er geen tijd beschikbaar is
            time_dropdown = OptionMenu(self, self.selected_time, "No available time") # Hier maakt die een dropdown met "geen beschikbare tijd"
            time_dropdown.configure(state='disabled') # Hier schakelt die de dropdown uit

        time_dropdown.config(width=25, highlightbackground="#FFAEE2")
        time_dropdown.place(x=385, y=395)

        # Zitplekken_button
        def validate_attendees_input():
            value = self.selected_attendees.get()

            if not value.isdigit():
                return "Please enter a valid number."

            if int(value) < 1 or int(value) > 10:
                return "Number of attendees should be between 1 and 10."

            return None

        def reserve_seats():
            selected_time = self.selected_time.get()
            attendees_error = validate_attendees_input()

            if selected_time == "No available time":
                messagebox.showinfo("Error", "No time available. Please come back later.")
            elif attendees_error:
                messagebox.showinfo("Error", attendees_error)
                self.selected_attendees.set("1") #om de box te resetten naar 1
            else:
                print("seats!")

        seats_button = Button(self, text="Reserve Seats", font=("Arial", 20, "bold"), bg="#ED5EAB", fg="#fcffff", command=reserve_seats)
        seats_button.place(x=378, y=500)


if __name__ == "__main__":
    app = FilmsReservationApp()
    app.mainloop()
