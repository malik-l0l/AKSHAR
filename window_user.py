# USER GUI FOR BIGGER WINDOW RESOLUTIONS
# GUI IMPORTS
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk

# DATABASE IMPORT
import database_user as database
# METHODS IMPORT
from function_user import UserFunctions


class User(UserFunctions):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.font1 = ("Arial", 15, "bold")

        self.seperator_label = customtkinter.CTkLabel(app,
                                                      font=self.font1,
                                                      text="",
                                                      text_color="#fff",
                                                      bg_color="grey",
                                                      height=610,
                                                      width=1
                                                      )

        self.seperator_label.place(x=475, y=35)

        # ----------- DETAILS -------------------------------------------------------

        # 3.locker number
        self.locker_no_label = customtkinter.CTkLabel(app,
                                                      font=self.font1,
                                                      text="Locker No.    :",
                                                      text_color="#fff",
                                                      bg_color="#161C25")

        self.locker_no_label.place(x=500, y=20)

        self.locker_no_entry = customtkinter.CTkEntry(app,
                                                      font=self.font1,
                                                      text_color="#000",
                                                      fg_color="#fff",
                                                      border_color="#0C9295",
                                                      border_width=2,
                                                      width=370)
        self.locker_no_entry.place(x=610, y=20)

        # 4.row number
        self.row_no_label = customtkinter.CTkLabel(app,
                                                   font=self.font1,
                                                   text="Row No.         :",
                                                   text_color="#fff",
                                                   bg_color="#161C25")
        self.row_no_label.place(x=500, y=80)
        self.row_no_entry = customtkinter.CTkEntry(app,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=370)
        self.row_no_entry.place(x=610, y=80)

        # 2.bundle_number
        self.bundle_no_label = customtkinter.CTkLabel(app,
                                                      font=self.font1,
                                                      text="Bundle No.    :",
                                                      text_color="#fff",
                                                      bg_color="#161C25")

        self.bundle_no_label.place(x=500, y=140)

        self.bundle_no_entry = customtkinter.CTkEntry(app,
                                                      font=self.font1,
                                                      text_color="#000",
                                                      fg_color="#fff",
                                                      border_color="#0C9295",
                                                      border_width=2,
                                                      width=370)
        self.bundle_no_entry.place(x=610, y=140)

        # 5.file number
        self.file_no_label = customtkinter.CTkLabel(app,
                                                    font=self.font1,
                                                    text="File No.          :",
                                                    text_color="#fff",
                                                    bg_color="#161C25")
        self.file_no_label.place(x=500, y=200)
        self.file_no_entry = customtkinter.CTkEntry(app,
                                                    font=self.font1,
                                                    text_color="#000",
                                                    fg_color="#fff",
                                                    border_color="#0C9295",
                                                    border_width=2,
                                                    width=370)
        self.file_no_entry.place(x=610, y=200)

        # 6.subject
        self.subject_label = customtkinter.CTkLabel(app,
                                                    font=self.font1,
                                                    text="Subject          :",
                                                    text_color="#fff",
                                                    bg_color="#161C25")
        self.subject_label.place(x=500, y=260)

        self.subject_entry = customtkinter.CTkTextbox(app,
                                                      font=self.font1,
                                                      text_color="#000",
                                                      fg_color="#fff",
                                                      border_color="#0C9295",
                                                      border_width=2,
                                                      width=370,
                                                      height=100
                                                      )
        self.subject_entry.place(x=610, y=260)

        # 7.description
        self.description_label = customtkinter.CTkLabel(app,
                                                        font=self.font1,
                                                        text="Description   :",
                                                        text_color="#fff",
                                                        bg_color="#161C25")
        self.description_label.place(x=500, y=380)

        self.description_entry = customtkinter.CTkTextbox(app,
                                                          font=self.font1,
                                                          text_color="#000",
                                                          fg_color="#fff",
                                                          border_color="#0C9295",
                                                          border_width=2,
                                                          width=370,
                                                          height=100,

                                                          )
        self.description_entry.place(x=610, y=380)

        # 8.hint1
        self.hint_1_label = customtkinter.CTkLabel(app,
                                                   font=self.font1,
                                                   text="Hint 1              :",
                                                   text_color="#fff",
                                                   bg_color="#161C25")

        self.hint_1_label.place(x=500, y=510)

        self.hint_1_entry = customtkinter.CTkEntry(app,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=370,
                                                   )
        self.hint_1_entry.place(x=610, y=510)

        # 9.hint 2
        self.hint_2_label = customtkinter.CTkLabel(app,
                                                   font=self.font1,
                                                   text="Hint 2              :",
                                                   text_color="#fff",
                                                   bg_color="#161C25")

        self.hint_2_label.place(x=500, y=570)

        self.hint_2_entry = customtkinter.CTkEntry(app,
                                                   font=self.font1,
                                                   text_color="#000",
                                                   fg_color="#fff",
                                                   border_color="#0C9295",
                                                   border_width=2,
                                                   width=370,

                                                   )
        self.hint_2_entry.place(x=610, y=570)

        # 10.remarks
        self.remarks_label = customtkinter.CTkLabel(app,
                                                    font=self.font1,
                                                    text="Remarks        :",
                                                    text_color="#fff",
                                                    bg_color="#161C25")

        self.remarks_label.place(x=500, y=630)

        self.remarks_entry = customtkinter.CTkEntry(app,
                                                    font=self.font1,
                                                    text_color="#000",
                                                    fg_color="#fff",
                                                    border_color="#0C9295",
                                                    border_width=2,
                                                    width=370,
                                                    )
        self.remarks_entry.place(x=610, y=630)

        # ----------- END DETAILS ---------------------------------------------------
        self.left_frame = customtkinter.CTkFrame(app,
                                                 width=430,
                                                 height=630,
                                                 fg_color="#161C25",
                                                 bg_color="#161C25",
                                                 corner_radius=15,

                                                 )
        self.left_frame.place(x=20, y=20)

        # -------- SEARCH BAR -----------------------------------------------
        self.label_frame_1 = customtkinter.CTkFrame(self.left_frame,
                                                    width=410,
                                                    height=240,
                                                    fg_color="#161C21",
                                                    bg_color="#161C25",
                                                    corner_radius=15,
                                                    border_width=2,
                                                    border_color="#0C9295"

                                                    )
        self.label_frame_1.grid(row=0, column=0)

        self.search_label = customtkinter.CTkLabel(self.label_frame_1,
                                                   font=("Consoles", 20, "bold"),
                                                   text="Search bar",
                                                   text_color="#fff",
                                                   bg_color="#161C21",
                                                   )

        self.search_label.place(x=150, y=10)

        options = ['All',
                   'Sl_No',
                   'Bundle_No',
                   'Locker_No',
                   'Row_No',
                   'File_No',
                   'Subject',
                   'Description',
                   'Hint_1',
                   'Hint_2',
                   'Remarks']

        self.variable1 = StringVar()
        self.Web_shown_options = customtkinter.CTkComboBox(self.label_frame_1,
                                                           font=self.font1,
                                                           text_color="#000",
                                                           fg_color="#fff",
                                                           button_color="#0C9295",
                                                           button_hover_color="#0C9295",
                                                           dropdown_hover_color="#0C9295",
                                                           border_color="#0C9295",
                                                           variable=self.variable1,
                                                           values=options,
                                                           width=370,
                                                           state="readonly")
        self.Web_shown_options.set('All')
        self.Web_shown_options.place(x=20, y=50)

        self.search_entry = customtkinter.CTkTextbox(self.label_frame_1,
                                                     font=self.font1,
                                                     text_color="#000",
                                                     fg_color="#fff",
                                                     border_color="#0C9295",
                                                     border_width=2,
                                                     width=370,
                                                     height=110
                                                     )
        self.search_entry.place(x=20, y=85)

        self.search_button = customtkinter.CTkButton(self.label_frame_1,
                                                     font=('Sans serif', 19, 'bold'),
                                                     text="Search",
                                                     text_color="#fff",
                                                     fg_color="#05A312",
                                                     hover_color="#00850B",
                                                     bg_color="#161C21",
                                                     cursor="hand2",
                                                     border_color="black",
                                                     corner_radius=12,
                                                     border_width=1,
                                                     width=150,
                                                     command=self.search
                                                     )
        self.search_button.place(x=130, y=202)

        # -------- END SEARCH BAR -------------------------------------------

        # -------- TREE/TABLE_VIEW --------------------------------------
        style = ttk.Style(self.left_frame)

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

        self.tree = ttk.Treeview(self.left_frame, height=12, cursor="hand2")
        self.tree['columns'] = ('Sl_No', 'File_No', 'Description')

        self.tree.column('#0', width=0, stretch=tk.NO)  # hide the default first column

        self.tree.column('Sl_No', anchor=tk.W, width=40)
        self.tree.column('File_No', anchor=tk.W, width=230)
        self.tree.column('Description', anchor=tk.W, width=240)

        self.tree.heading('Sl_No', text='ID')
        self.tree.heading('File_No', text='File_number')
        self.tree.heading('Description', text='Description')

        # =
        # Placing the treeview and scrollbar widgets inside the left_frame
        self.tree.grid(row=3, column=0, pady=40, sticky=tk.NSEW)

        # Configuring grid weights to allow resizing
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(3, weight=1)

        self.tree.bind('<Button-1>', self.handle_click)
        self.tree.bind('<ButtonRelease>', self.display_data)

        # -------------- HOVER EFFECT --------------------------------------
        # Here begins the key step
        self.tree.tag_configure('focus', background='#161C21')
        self.tree.bind("<Motion>", self.mycallback)
        self.last_focus = None
        # -------------- HOVER EFFECT --------------------------------------

        database.create_table()

        self.add_to_treeview()
        self.change_state(normal=False)  # no typing in the starting of app

        # -------- END TREE/TABLE_VIEW ----------------------------------
