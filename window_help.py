# HELP WINDOW

import io

from PIL import Image
import customtkinter
from customtkinter import CTkImage
import tkinter as tk

# the error arise because I made a python script as a database which is 6.07MB while the limit is 2.57 MB
# ignore this error.it is not a problem now.
from database_image_bytes import help1_byte, help2_byte


class Help:
    def __init__(self, app):
        self.app = app

        self.font1 = ("Arial", 15, "bold")
        self.help1 = CTkImage(Image.open(io.BytesIO(help1_byte)), size=(1000, 750))
        self.help2 = CTkImage(Image.open(io.BytesIO(help2_byte)), size=(1000, 750))

        self.label_frame = customtkinter.CTkScrollableFrame(app,
                                                            width=920,
                                                            height=610,
                                                            fg_color="#161C21",
                                                            bg_color="#161C25",
                                                            corner_radius=15,
                                                            )
        self.label_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.photo5_label = customtkinter.CTkLabel(self.label_frame,
                                                   text="",
                                                   image=self.help2,
                                                   compound="bottom"
                                                   )
        self.photo5_label.pack()

        self.photo5_label = customtkinter.CTkLabel(self.label_frame,
                                                   text="",
                                                   image=self.help1,
                                                   compound="bottom"
                                                   )
        self.photo5_label.pack()
