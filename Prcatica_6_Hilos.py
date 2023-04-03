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
