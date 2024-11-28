# ABOUT GUI FOR BIGGER WINDOW RESOLUTIONS
import io

import tkinter as tk
from PIL import Image
import customtkinter
from customtkinter import CTkImage


# the error arise because I made a python script as a database which is 6.07MB while the limit is 2.57 MB
# ignore this error.it is not a problem now.
from database_image_bytes import saleem_byte, ismail_byte, lavya_byte, bindima_miss_byte, reghuraj_principal_byte


class About:
    def __init__(self, app):
        self.app = app

        self.font_name = ("Bahnschrift", 15,)
        self.font_who = ("Bahnschrift", 15,)
        self.font_about = ("Bahnschrift", 18,)
        self.font_copyright = ("Bahnschrift", 15, "underline")

        self.photo1 = CTkImage(Image.open(io.BytesIO(reghuraj_principal_byte)), size=(95, 95))
        self.photo2 = CTkImage(Image.open(io.BytesIO(lavya_byte)), size=(100, 100))
        self.photo3 = CTkImage(Image.open(io.BytesIO(saleem_byte)), size=(120, 120))
        self.photo4 = CTkImage(Image.open(io.BytesIO(ismail_byte)), size=(100, 100))
        self.photo5 = CTkImage(Image.open(io.BytesIO(bindima_miss_byte)), size=(95, 95))

        copyright_text = "Copyright © CSD[22-26]"

        about_text = """
Welcome to Akshar,


\tAkshar is a file management software specially designed for Government Engineering College - Kozhikode, This software is designed to revolutionize the way files are organized and retrieved within our college.
         
\tThe need for this software arose from the time-consuming process of manually searching for files in our college, wasting valuable time and effort. It became evident that more efficient and automated solution was required to save time and improve the productivity of college staff members. The principal, recognizing this challenge,requested the development of a software solution to address this issue. 

\tOur dedicated team of developers and designers from the Computer Science and Design department, with their experience in software development, took on the challenge. They understood the needs of our college and worked tirelessly to create a solution that would meet those needs effectively. 

\tThe goal of this software is to streamline file organization, improve efficiency, and save time for our college staff members. With its user-friendly interface and advanced search capabilities, users can easily search for files without spending valuable time searching through shelves or cabinets for specific files. Our software simplifies the process, allowing them to focus on more important tasks. 

\tWe would like to express our gratitude to the principal and all the staff who supported and contr-ibuted to the development of this software. Their feedback were invaluable in creating a solution that truly meets the needs of our college.

            For any support or further information about this software,please feel free to reach out to us at 
                                                             saleemmalikgeck24@gmail.com.
        """

        # ------------ PHOTO FRAME ----------------------------------------------------
        self.about_frame = customtkinter.CTkFrame(app,
                                                  fg_color="#161C25",
                                                  corner_radius=20,
                                                  )
        self.about_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.photo_frame = customtkinter.CTkFrame(self.about_frame,
                                                  # width=500,
                                                  # height=50,
                                                  fg_color="#161C21",
                                                  bg_color="#161C25",
                                                  corner_radius=20,
                                                  border_color="#0C9295",
                                                  border_width=2,
                                                  )
        self.photo_frame.grid(row=0, column=0, pady=5)

        self.people_label = customtkinter.CTkLabel(self.photo_frame,
                                                   text="Meet the team",
                                                   font=("Arial", 20, "bold")

                                                   )
        self.people_label.grid(row=0, column=2, pady=4)

        # photos ----------------------------------------
        self.photo1_label = customtkinter.CTkLabel(self.photo_frame,
                                                   text="",
                                                   image=self.photo1,
                                                   compound="bottom"
                                                   )
        self.photo1_label.grid(row=1, column=0, padx=20)

        self.photo2_label = customtkinter.CTkLabel(self.photo_frame,
                                                   text="",
                                                   image=self.photo2,
                                                   compound="bottom"
                                                   )
        self.photo2_label.grid(row=1, column=1, padx=10)

        self.photo3_label = customtkinter.CTkLabel(self.photo_frame,
                                                   text="",
                                                   image=self.photo3,
                                                   compound="bottom"
                                                   )
        self.photo3_label.grid(row=1, column=2, padx=10)
        self.photo4_label = customtkinter.CTkLabel(self.photo_frame,
                                                   text="",
                                                   image=self.photo4,
                                                   compound="bottom"
                                                   )
        self.photo4_label.grid(row=1, column=3, padx=10)

        self.photo5_label = customtkinter.CTkLabel(self.photo_frame,
                                                   text="",
                                                   image=self.photo5,
                                                   compound="bottom"
                                                   )
        self.photo5_label.grid(row=1, column=4, padx=20)

        # end photo ----------------------------------------

        # name --------------
        self.photo1_name_text = customtkinter.CTkLabel(self.photo_frame,
                                                       text="Dr PC Reghuraj\n(Principal)",
                                                       font=self.font_name,
                                                       )
        self.photo1_name_text.grid(row=2, column=0)
        self.photo2_name_text = customtkinter.CTkLabel(self.photo_frame,
                                                       text="Lavya Shaji\n(Documentation)",
                                                       font=self.font_name,

                                                       )
        self.photo2_name_text.grid(row=2, column=1)
        self.photo3_name_text = customtkinter.CTkLabel(self.photo_frame,
                                                       text="Saleem Malik\n(Project Head)",
                                                       font=self.font_name,

                                                       )
        self.photo3_name_text.grid(row=2, column=2)
        self.photo4_name_text = customtkinter.CTkLabel(self.photo_frame,
                                                       text="Muhd. Ismail\n(Design)",
                                                       font=self.font_name,

                                                       )
        self.photo4_name_text.grid(row=2, column=3)
        self.photo5_name_text = customtkinter.CTkLabel(self.photo_frame,
                                                       text="Dr Bindima T\n(HOD CSD)",
                                                       font=self.font_name,

                                                       )
        self.photo5_name_text.grid(row=2, column=4)

        # end name ----------

        # batch --------------
        customtkinter.CTkLabel(self.photo_frame,
                               text="Students, Computer Science & Design (2022-2026)",
                               font=self.font_who,
                               corner_radius=150,
                               compound="bottom"
                               ).grid(row=3, column=1, columnspan=3, pady=2)

        # end batch ----------

        # ------------ PHOTO FRAME ----------------------------------------------------

        self.about_text = customtkinter.CTkTextbox(self.about_frame,
                                                   font=self.font_about,
                                                   text_color="#fff",
                                                   fg_color="#161C21",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=890,
                                                   height=370,
                                                   corner_radius=20,
                                                   scrollbar_button_hover_color="#0C9295"

                                                   )
        self.about_text.grid(row=1, column=0, pady=5, padx=10)
        self.about_text.insert("1.0", about_text)
        self.about_text.configure(state="disabled", border_spacing=10)

        # ------------- COPYRIGHT ---------------------------------------------------------------------

        self.copy_right_label = customtkinter.CTkLabel(self.about_frame,
                                                       font=self.font_copyright,
                                                       text=copyright_text,
                                                       text_color="#fff",
                                                       bg_color="#161C25",
                                                       )
        self.copy_right_label.grid(row=3, column=0, pady=1)

        # ------------- COPYRIGHT ---------------------------------------------------------------------

        # # -------- SEPERATOR -----------------------------------------
        # self.seperator_label = customtkinter.CTkLabel(app,
        #                                               font=self.font_name,
        #                                               text="",
        #                                               text_color="#fff",
        #                                               bg_color="grey",
        #                                               height=950,
        #                                               width=1
        #                                               )
        #
        # self.seperator_label.place(x=495, y=0)
        # # -------- END SEPERATOR -------------------------------------

#
# if __name__ == '__main__':
#     app = customtkinter.CTk()
#     app.geometry("1025x740+330+50")
#     app.config(bg="#161C25")
#     x = About(app)
#     app.mainloop()
