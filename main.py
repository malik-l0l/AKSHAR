# GUI IMPORTS
import os

import customtkinter
from tkinter import messagebox


from window_about import About
from window_help import Help


RESIZABLE = False
SET = "User"
PASSWORD = "password"
APP_TITLE = "AKSHAR"

font1 = ("Arial", 15, "bold")  # password box


def screen_type():
    """
    it checks the display resolution of the monitor
    and make the application responsive if needed
    [
    to find display resolution of your window/screen :-
    right click on desktop -> Display settings -> display resolution
    ]
    :return: True if grid arrangement needed else place arrangement is used
    """
    # with_grid = ["1600x900", "1440x900",
    #              "1366x768", "1360x768",
    #              "1280x960", "1280x800",
    #              "1280x768", "1280x720",
    #              "1152x864", "1024x768"
    #              ]

    with_place = ["1024x819", "1120x840",
                  "1344x840", "1536x864",
                  ]

    res = f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}"

    # print(res)

    if res in with_place:
        return False
    # elif res in with_grid:
    #     return True
    else:
        return True


def change_tab():
    """
    activated when the tab button in the top is selected by user.
    :return: None
    """
    # if "User" tab is selected -
    if tabs.get() == "User":
        if screen_type():
            # grid arrangement
            from window_user_1 import User
            User(user_window)
        else:
            # place arrangement
            from window_user import User
            User(user_window)

    # if "Admin" tab is selected -
    if tabs.get() == "Admin":

        # asks for authentication
        # admin tab require password -
        dialog = customtkinter.CTkInputDialog(text="Admin access require password \nEnter password :",
                                              title="Authentication", font=font1)
        dialog.geometry("400x170+100+0")

        # if password is correct go to Admin tab
        if dialog.get_input() == PASSWORD:
            if screen_type():
                # grid arrangement
                from window_admin_1 import Admin
                Admin(admin_window)
            else:
                # place arrangement
                from window_admin import Admin
                Admin(admin_window)

        # if password is not correct go to User tab
        else:
            tabs.set("User")
            messagebox.showwarning("Authentication Error", "Access Denied: Incorrect Password!")


    # if "About" tab is selected -
    if tabs.get() == "About":
        About(about_window)

    # if "Help" tab is selected -
    if tabs.get() == "Help":
        Help(help_window)


# ===== APP INITIALIZATION ==========================================================================
app = customtkinter.CTk()
app.title(APP_TITLE)
app.resizable(RESIZABLE, RESIZABLE)

# making app responsive for different type of monitors
app.geometry(f"1150x690+100+0") if screen_type() else app.geometry(f"1025x740+100+0")

# initializing tabs
tabs = customtkinter.CTkTabview(app,
                                command=change_tab,
                                corner_radius=10,
                                fg_color="#161C25",
                                # segmented_button_fg_color="#161C25",
                                segmented_button_selected_color="#161C25",
                                )

# making different tabs
tabs.add("Admin")
tabs.add("User")
tabs.add("About")
tabs.add("Help")

# User tab is set to default
# the first window to open when the app starts
tabs.set(SET)

tabs.pack(expand=True, fill="both")

user_window = tabs.tab("User")
admin_window = tabs.tab("Admin")
about_window = tabs.tab("About")
help_window = tabs.tab("Help")

change_tab()

app.mainloop()
# ===== END APP INITIALIZATION ======================================================================
