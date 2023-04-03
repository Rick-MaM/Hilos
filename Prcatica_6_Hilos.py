from tkinter import *
from PIL import Image, ImageTk
import threading
import time


class move_image:

    def __init__(self, window, image, direction):
        self.window = window
        self.image = image
        self.direction = direction
        self.limit_date = False
        self.insert()

    def insert(self):
        self.lbl_image = Label(self.window, image=self.image)
        self.move_image(0,0)
    
    def limit(self, date_x_or_y):
        if date_x_or_y >= 400:
            self.limit_date = True
        elif date_x_or_y <= 0:
            self.limit_date = False
    
    def increase_or_decrease(self, date):
        self.limit(date)
        if self.limit_date:
            date -= 5
        else:
            date += 5
        return date
    
    def move_image(self, date_x, date_y):
        while True:
            if self.direction == "left_to_right":
                date_x = self.increase_or_decrease(date_x)
            elif self.direction == "up_to_bottom":
                date_y = self.increase_or_decrease(date_y)
            self.lbl_image.place(x=date_x, y=date_y)
            time.sleep(0.15)


if __name__ == "__main__":
    window = Tk()
    window.title("Hilos")
    window.geometry("500x600")

    image = Image.open('DVD.jpg')
    new_image = image.resize((100, 100))
    render = ImageTk.PhotoImage(new_image)

    frame = Frame(window)
    frame.place(x=0, y=100, width=500,height=500)

    thread = threading.Thread(name="Hilo_1", target=move_image, args=(
        frame, render, "left_to_right", ))
    thread_2 = threading.Thread(
        name="Hilo_2", target=move_image, args=(frame, render, "up_to_bottom", ))

    thread.start()
    thread_2.start()

    window.mainloop()
