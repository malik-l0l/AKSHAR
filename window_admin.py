# ADMIN GUI FOR BIGGER WINDOW RESOLUTIONS

import customtkinter
import tkinter as tk
from tkinter import SUNKEN, ttk

from function_admin import AdminFunctions


class Admin(AdminFunctions):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.font1 = ("Arial", 15, "bold")

        # ---------- DETAILS -------------------------------------------------

        # 3.locker number
        self.locker_no_label = customtkinter.CTkLabel(app,
                                                      font=self.font1,
                                                      text="Locker No.    :",
                                                      text_color="#fff",
                                                      bg_color="#161C25",
                                                      )

        self.locker_no_label.place(x=20, y=20)

        self.locker_no_entry = customtkinter.CTkEntry(app,
                                                      font=self.font1,
                                                      text_color="#000",
                                                      fg_color="#fff",
                                                      border_color="#0C9295",
                                                      border_width=2,
                                                      width=370)
        self.locker_no_entry.place(x=130, y=20)

        # 4.row number
        self.row_no_label = customtkinter.CTkLabel(app,
                                                   font=self.font1,
                                                   text="Row No.         :",
                                                   text_color="#fff",
                                                   bg_color="#161C25")
        self.row_no_label.place(x=20, y=80)
        self.row_no_entry = customtkinter.CTkEntry(app,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=120)
        self.row_no_entry.place(x=130, y=80)

        # 2.bundle_number
        self.bundle_no_label = customtkinter.CTkLabel(app,
                                                      font=self.font1,
                                                      text="Bundle No.    :",
                                                      text_color="#fff",
                                                      bg_color="#161C25")

        self.bundle_no_label.place(x=270, y=80)

        self.bundle_no_entry = customtkinter.CTkEntry(app,
                                                      font=self.font1,
                                                      text_color="#000",
                                                      fg_color="#fff",
                                                      border_color="#0C9295",
                                                      border_width=2,
                                                      width=120)
        self.bundle_no_entry.place(x=380, y=80)

        # 5.file number
        self.file_no_label = customtkinter.CTkLabel(app,
                                                    font=self.font1,
                                                    text="File No.          :",
                                                    text_color="#fff",
                                                    bg_color="#161C25")
        self.file_no_label.place(x=20, y=140)
        self.file_no_entry = customtkinter.CTkEntry(app,
                                                    font=self.font1,
                                                    text_color="#000",
                                                    fg_color="#fff",
                                                    border_color="#0C9295",
                                                    border_width=2,
                                                    width=370)
        self.file_no_entry.place(x=130, y=140)

        # 6.subject
        self.subject_label = customtkinter.CTkLabel(app,
                                                    font=self.font1,
                                                    text="Subject          :",
                                                    text_color="#fff",
                                                    bg_color="#161C25")
        self.subject_label.place(x=20, y=200)

        self.subject_entry = customtkinter.CTkTextbox(app,
                                                      font=self.font1,
                                                      text_color="#000",
                                                      fg_color="#fff",
                                                      border_color="#0C9295",
                                                      border_width=2,
                                                      width=370,
                                                      height=100
                                                      )
        self.subject_entry.place(x=130, y=200)

        # 7.description
        self.description_label = customtkinter.CTkLabel(app,
                                                        font=self.font1,
                                                        text="Description   :",
                                                        text_color="#fff",
                                                        bg_color="#161C25")
        self.description_label.place(x=20, y=330)

        self.description_entry = customtkinter.CTkTextbox(app,
                                                          font=self.font1,
                                                          text_color="#000",
                                                          fg_color="#fff",
                                                          border_color="#0C9295",
                                                          border_width=2,
                                                          width=370,
                                                          height=100,

                                                          )
        self.description_entry.place(x=130, y=330)

        # 8.hint1
        self.hint_1_label = customtkinter.CTkLabel(app,
                                                   font=self.font1,
                                                   text="Hint 1              :",
                                                   text_color="#fff",
                                                   bg_color="#161C25")

        self.hint_1_label.place(x=20, y=460)

        self.hint_1_entry = customtkinter.CTkEntry(app,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=370)
        self.hint_1_entry.place(x=130, y=460)

        # 9.hint 2
        self.hint_2_label = customtkinter.CTkLabel(app,
                                                   font=self.font1,
                                                   text="Hint 2              :",
                                                   text_color="#fff",
                                                   bg_color="#161C25")

        self.hint_2_label.place(x=20, y=520)

        self.hint_2_entry = customtkinter.CTkEntry(app,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=370)
        self.hint_2_entry.place(x=130, y=520)

        # 10.remarks
        self.remarks_label = customtkinter.CTkLabel(app,
                                                    font=self.font1,
                                                    text="Remarks        :",
                                                    text_color="#fff",
                                                    bg_color="#161C25")

        self.remarks_label.place(x=20, y=580)

        self.remarks_entry = customtkinter.CTkEntry(app,
                                                    font=self.font1,
                                                    text_color="#000",
                                                    fg_color="#fff",
                                                    border_color="#0C9295",
                                                    border_width=2,
                                                    width=370)
        self.remarks_entry.place(x=130, y=580)

        # ----------- END DETAILS ---------------------------------------------------

        # ----------- BUTTONS -------------------------------------------------------

        self.delete_button = customtkinter.CTkButton(app,
                                                     font=('Arial', 19, 'bold'),
                                                     text="Delete",
                                                     text_color="#fff",
                                                     fg_color="#161C25",
                                                     bg_color="#161C25",
                                                     hover_color="dark red",
                                                     cursor="hand2",
                                                     border_color="red",
                                                     corner_radius=22,
                                                     border_width=2,
                                                     width=130,
                                                     command=self.delete
                                                     )
        self.delete_button.place(x=20, y=639)

        self.update_button = customtkinter.CTkButton(app,
                                                     font=('Sans serif', 19, 'bold'),
                                                     text="Update",
                                                     text_color="#fff",
                                                     fg_color="#161C25",
                                                     bg_color="#161C25",
                                                     hover_color="#677bda",
                                                     cursor="hand2",
                                                     border_color="#6f69d8",
                                                     corner_radius=12,
                                                     border_width=2,
                                                     width=130,
                                                     command=self.update
                                                     )
        self.update_button.place(x=165, y=639)

        self.add_button = customtkinter.CTkButton(app,
                                                  font=('Sans serif', 19, 'bold'),
                                                  text="Add",
                                                  text_color="#fff",
                                                  fg_color="#161C25",
                                                  bg_color="#161C25",
                                                  hover_color="#00850B",
                                                  cursor="hand2",
                                                  border_color="#05A312",
                                                  corner_radius=12,
                                                  border_width=2,
                                                  width=130,
                                                  command=self.add
                                                  )
        self.add_button.place(x=310, y=639)

        self.clear_button = customtkinter.CTkButton(app,
                                                    font=('Sans serif', 19, 'bold'),
                                                    text="C",
                                                    text_color="#fff",
                                                    fg_color="#161C25",
                                                    hover_color="#94a0ad",
                                                    bg_color="#161C25",
                                                    cursor="hand2",
                                                    border_color="#94a0ad",
                                                    corner_radius=18,
                                                    border_width=2,
                                                    width=10,
                                                    command=self.clear_button
                                                    )
        self.clear_button.place(x=455, y=639)
        # --------END BUTTONS-------------------------------------------------------

        # -------- SEPERATOR -----------------------------------------
        self.seperator_label = customtkinter.CTkLabel(app,
                                                      font=self.font1,
                                                      text="",
                                                      text_color="#fff",
                                                      bg_color="grey",
                                                      height=610,
                                                      width=1
                                                      )

        self.seperator_label.place(x=525, y=40)
        # -------- END SEPERATOR -------------------------------------

        # ------- SEARCH_BAR -----------------------------------------

        self.search_entry = customtkinter.CTkEntry(app,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=355)
        self.search_entry.place(x=550, y=20)

        self.search_button = customtkinter.CTkButton(app,
                                                     font=('Sans serif', 15, 'bold'),
                                                     text="search",
                                                     text_color="#fff",
                                                     fg_color="#05A312",
                                                     hover_color="#00850B",
                                                     bg_color="#161C25",
                                                     cursor="hand2",
                                                     border_color="black",
                                                     # corner_radius=22,
                                                     border_width=1,
                                                     width=55,
                                                     command=self.search_admin

                                                     )
        self.search_button.place(x=910, y=20)

        # ------- SEARCH_BAR -----------------------------------------

        # -------- TREE/TABLE_VIEW RECORDS --------------------------------------
        style = ttk.Style(app)

        style.theme_use('clam')
        style.configure('Treeview',
                        font=("Arial", 14),
                        foreground='#fff',
                        background='#000',
                        fieldbackground='#313837',
                        rowheight=35
                        )
        style.configure("Treeview.Heading",
                        relief=SUNKEN,
                        background="#161C21",
                        foreground="white",
                        font=('Arial', 15, 'bold'),
                        bd=10,
                        )

        style.map("Treeview.Heading", background=[('active', '#161C21')])
        style.map('Treeview',
                background=[('selected', '#1A8F2D')],
                foreground=[('selected', '#FFFFFF')],
                font=[('selected', ('Arial', 17, 'bold'))],
                relief=[('pressed', 'sunken')]
        )

        self.tree = ttk.Treeview(app, height=20, cursor="hand2")
        self.tree['columns'] = ('Sl_No', 'File_No', 'Description')

        self.tree.column('#0', width=0, stretch=tk.NO)  # hide the default first column

        self.tree.column('Sl_No', anchor=tk.W, width=60)
        self.tree.column('File_No', anchor=tk.W, width=230)
        self.tree.column('Description', anchor=tk.W, width=240)

        self.tree.heading('Sl_No', text='ID', )
        self.tree.heading('File_No', text='File_number')
        self.tree.heading('Description', text='Description')
        self.tree.place(x=685, y=100)

        self.tree.bind('<Button-1>', self.handle_click)  # to solve a tree column bug
        self.tree.bind('<ButtonRelease>', self.display_data)

        # -------------- HOVER EFFECT --------------------------------------
        # Here begins the key step
        self.tree.tag_configure('focus', background='#161C25')
        self.tree.bind("<Motion>", self.mycallback)
        self.last_focus = None
        # -------------- HOVER EFFECT --------------------------------------

        self.add_to_treeview()
        # -------- END TREE/TABLE_VIEW RECORDS ----------------------------------
