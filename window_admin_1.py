# ADMIN GUI FOR SMALLER WINDOW RESOLUTIONS

import _tkinter
import tkinter as tk
import customtkinter
from tkinter import SUNKEN, END, ttk, messagebox

import database_user as database
import database_admin as admin_database

from function_admin import AdminFunctions


class Admin(AdminFunctions):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.font1 = ("Arial", 17, "bold")

        self.admin_frame = customtkinter.CTkFrame(app,
                                                  fg_color="#161C25",
                                                  bg_color="#161C25",
                                                  corner_radius=15,
                                                  )
        self.admin_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.left_frame = customtkinter.CTkFrame(self.admin_frame,
                                                 fg_color="#161C25",
                                                 bg_color="#161C25",
                                                 corner_radius=15,
                                                 )
        self.left_frame.grid(row=0, column=0, pady=2)

        self.middle_frame = customtkinter.CTkFrame(self.admin_frame,
                                                   height=550,
                                                   width=2,
                                                   fg_color="grey",
                                                   bg_color="#161C25",
                                                   corner_radius=15,
                                                   )
        self.middle_frame.grid(row=0, column=1, padx=10)

        self.right_frame = customtkinter.CTkFrame(self.admin_frame,
                                                  fg_color="#161C25",
                                                  bg_color="#161C25",
                                                  corner_radius=15,

                                                  )
        self.right_frame.grid(row=0, column=2, padx=13, pady=0)

        self.pady_for_left_frame = 12

        self.locker_no_label = customtkinter.CTkLabel(self.left_frame,
                                                      font=self.font1,
                                                      text="Locker No.    :",
                                                      text_color="#fff",
                                                      bg_color="#161C25")

        self.locker_no_label.grid(row=0, column=0, pady=self.pady_for_left_frame)

        self.locker_no_entry = customtkinter.CTkEntry(self.left_frame,
                                                      font=self.font1,
                                                      text_color="#000",
                                                      fg_color="#fff",
                                                      border_color="#0C9295",
                                                      border_width=2,
                                                      width=410)
        self.locker_no_entry.grid(row=0, column=1, pady=self.pady_for_left_frame)

        self.row_bundle_frame = customtkinter.CTkFrame(self.left_frame,
                                                       fg_color="#161C25",
                                                       bg_color="#161C25",
                                                       corner_radius=15,
                                                       )
        self.row_bundle_frame.grid(row=1, column=0, pady=2, columnspan=2)

        # 4.row number
        self.row_no_label = customtkinter.CTkLabel(self.row_bundle_frame,
                                                   font=self.font1,
                                                   text="Row No.         : ",
                                                   text_color="#fff",
                                                   bg_color="#161C25")
        self.row_no_label.grid(row=0, column=0, pady=self.pady_for_left_frame)
        self.row_no_entry = customtkinter.CTkEntry(self.row_bundle_frame,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=140)
        self.row_no_entry.grid(row=0, column=1, pady=self.pady_for_left_frame)

        # 2.bundle_number
        self.bundle_no_label = customtkinter.CTkLabel(self.row_bundle_frame,
                                                      font=self.font1,
                                                      text="  Bundle No.    : ",
                                                      text_color="#fff",
                                                      bg_color="#161C25")

        self.bundle_no_label.grid(row=0, column=2, pady=self.pady_for_left_frame)

        self.bundle_no_entry = customtkinter.CTkEntry(self.row_bundle_frame,
                                                      font=self.font1,
                                                      text_color="#000",
                                                      fg_color="#fff",
                                                      border_color="#0C9295",
                                                      border_width=2,
                                                      width=140)
        self.bundle_no_entry.grid(row=0, column=3, pady=self.pady_for_left_frame)

        # 5.file number
        self.file_no_label = customtkinter.CTkLabel(self.left_frame,
                                                    font=self.font1,
                                                    text="File No.          :",
                                                    text_color="#fff",
                                                    bg_color="#161C25")
        self.file_no_label.grid(row=2, column=0, pady=self.pady_for_left_frame)
        self.file_no_entry = customtkinter.CTkEntry(self.left_frame,
                                                    font=self.font1,
                                                    text_color="#000",
                                                    fg_color="#fff",
                                                    border_color="#0C9295",
                                                    border_width=2,
                                                    width=410)
        self.file_no_entry.grid(row=2, column=1, pady=self.pady_for_left_frame)

        # 6.subject
        self.subject_label = customtkinter.CTkLabel(self.left_frame,
                                                    font=self.font1,
                                                    text="Subject          :",
                                                    text_color="#fff",
                                                    bg_color="#161C25")
        self.subject_label.grid(row=3, column=0, pady=self.pady_for_left_frame)

        self.subject_entry = customtkinter.CTkTextbox(self.left_frame,
                                                      font=self.font1,
                                                      text_color="#000",
                                                      fg_color="#fff",
                                                      border_color="#0C9295",
                                                      border_width=2,
                                                      width=410,
                                                      height=100
                                                      )
        self.subject_entry.grid(row=3, column=1, pady=self.pady_for_left_frame)

        # 7.description
        self.description_label = customtkinter.CTkLabel(self.left_frame,
                                                        font=self.font1,
                                                        text="Description   :",
                                                        text_color="#fff",
                                                        bg_color="#161C25")
        self.description_label.grid(row=4, column=0, pady=self.pady_for_left_frame)

        self.description_entry = customtkinter.CTkTextbox(self.left_frame,
                                                          font=self.font1,
                                                          text_color="#000",
                                                          fg_color="#fff",
                                                          border_color="#0C9295",
                                                          border_width=2,
                                                          width=410,
                                                          height=100,

                                                          )
        self.description_entry.grid(row=4, column=1, pady=self.pady_for_left_frame)

        # 8.hint1
        self.hint_1_label = customtkinter.CTkLabel(self.left_frame,
                                                   font=self.font1,
                                                   text="Hint 1              :",
                                                   text_color="#fff",
                                                   bg_color="#161C25")

        self.hint_1_label.grid(row=5, column=0, pady=self.pady_for_left_frame)

        self.hint_1_entry = customtkinter.CTkEntry(self.left_frame,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=410,
                                                   )
        self.hint_1_entry.grid(row=5, column=1, pady=self.pady_for_left_frame)

        # 9.hint 2
        self.hint_2_label = customtkinter.CTkLabel(self.left_frame,
                                                   font=self.font1,
                                                   text="Hint 2              :",
                                                   text_color="#fff",
                                                   bg_color="#161C25")

        self.hint_2_label.grid(row=6, column=0, pady=self.pady_for_left_frame)

        self.hint_2_entry = customtkinter.CTkEntry(self.left_frame,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=410,

                                                   )
        self.hint_2_entry.grid(row=6, column=1, pady=self.pady_for_left_frame)

        # 10.remarks
        self.remarks_label = customtkinter.CTkLabel(self.left_frame,
                                                    font=self.font1,
                                                    text="Remarks        :",
                                                    text_color="#fff",
                                                    bg_color="#161C25")

        self.remarks_label.grid(row=7, column=0, pady=self.pady_for_left_frame)

        self.remarks_entry = customtkinter.CTkEntry(self.left_frame,
                                                    font=self.font1,
                                                    text_color="#000",
                                                    fg_color="#fff",
                                                    border_color="#0C9295",
                                                    border_width=2,
                                                    width=410,
                                                    )
        self.remarks_entry.grid(row=7, column=1, pady=self.pady_for_left_frame)

        # ----------- END DETAILS ---------------------------------------------------
        # ----------- BUTTONS -------------------------------------------------------

        self.button_frame = customtkinter.CTkFrame(self.left_frame,
                                                   fg_color="#161C25",
                                                   bg_color="#161C25",
                                                   corner_radius=15,
                                                   )
        self.button_frame.grid(row=8, column=0, pady=4, columnspan=3)
        self.button_padding = 12
        self.delete_button = customtkinter.CTkButton(self.button_frame,
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
        self.delete_button.grid(row=0, column=0, padx=self.button_padding)

        self.update_button = customtkinter.CTkButton(self.button_frame,
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
        self.update_button.grid(row=0, column=1, padx=self.button_padding)

        self.add_button = customtkinter.CTkButton(self.button_frame,
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
        self.add_button.grid(row=0, column=2, padx=self.button_padding)

        self.clear_button = customtkinter.CTkButton(self.button_frame,
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
        self.clear_button.grid(row=0, column=3, padx=self.button_padding)
        # --------END BUTTONS-------------------------------------------------------
        # ------- SEARCH_BAR -----------------------------------------

        self.search_frame = customtkinter.CTkFrame(self.right_frame,
                                                   fg_color="#161C25",
                                                   bg_color="#161C25",
                                                   corner_radius=15,
                                                   )
        self.search_frame.grid(row=0, column=0, pady=15, columnspan=3)

        self.search_entry = customtkinter.CTkEntry(self.search_frame,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=375)
        self.search_entry.grid(row=0, column=0)

        self.search_button = customtkinter.CTkButton(self.search_frame,
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
                                                     width=95,
                                                     command=self.search_admin
                                                     )
        self.search_button.grid(row=0, column=1, padx=10)

        # ------- SEARCH_BAR -----------------------------------------
        # -------- TREE/TABLE_VIEW RECORDS --------------------------------------
        style = ttk.Style(app)

        style.theme_use('clam')
        style.configure('Treeview',
                        font=("Arial", 14),
                        foreground='#fff',
                        background='#000',
                        fieldbackground='#313837',
                        rowheight=36
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

        self.tree = ttk.Treeview(self.right_frame, height=14, cursor="hand2")
        self.tree['columns'] = ('Sl_No', 'File_No', 'Description')

        self.tree.column('#0', width=0, stretch=tk.NO)  # hide the default first column

        self.tree.column('Sl_No', anchor=tk.W, width=60)
        self.tree.column('File_No', anchor=tk.W, width=230)
        self.tree.column('Description', anchor=tk.W, width=240)

        self.tree.heading('Sl_No', text='ID', )
        self.tree.heading('File_No', text='File_number')
        self.tree.heading('Description', text='Description')
        self.tree.grid(row=2, column=0, columnspan=2, pady=10)

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

