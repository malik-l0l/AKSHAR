import _tkinter
from tkinter import END, messagebox

import database_user as database
import database_admin as admin_database


class AdminFunctions:
    def __init__(self):
        self.variable1 = None
        self.search_entry = None

        self.remarks_entry = None
        self.hint_2_entry = None
        self.hint_1_entry = None
        self.description_entry = None
        self.subject_entry = None
        self.file_no_entry = None
        self.row_no_entry = None
        self.locker_no_entry = None
        self.bundle_no_entry = None

        self.tree = None
        self.last_focus = None

    def check_entry(self):
        if self.locker_no_entry.get().isspace() or self.locker_no_entry.get() == "":
            messagebox.showwarning("Invalid entry", "Please enter 'Locker No.'")
            return False

        if not self.row_no_entry.get().isdigit():
            messagebox.showwarning("Invalid entry", "Row No. must be a number!")
            return False
        if not self.bundle_no_entry.get().isdigit():
            messagebox.showwarning("Invalid entry", "Bundle No. must be a number!")
            return False

        if self.file_no_entry.get().isspace() or self.file_no_entry.get() == "":
            messagebox.showwarning("Invalid entry", "Please enter 'File No.'")
            return False

        if self.subject_entry.get("1.0", END).isspace() or self.subject_entry.get("1.0", END) == "":
            messagebox.showwarning("Invalid entry", "Please enter 'Subject'")
            return False
        if self.description_entry.get("1.0", END).isspace() or self.description_entry.get("1.0", END) == "":
            messagebox.showwarning("Invalid entry", "Please enter 'Description'")
            return False

        return True

    def add(self):
        if self.check_entry():
            if admin_database.check_record_exists(self.file_no_entry.get()):
                messagebox.showwarning("Warning", f"{self.file_no_entry.get()} already exists!.")
            else:
                last_sl_no = admin_database.last_sl_no() + 1
                data = (
                    int(last_sl_no),
                    int(self.bundle_no_entry.get()),
                    self.locker_no_entry.get(),
                    int(self.row_no_entry.get()),
                    self.file_no_entry.get(),
                    self.subject_entry.get("1.0", END).strip(),
                    self.description_entry.get("1.0", END).strip(),
                    self.hint_1_entry.get(),
                    self.hint_2_entry.get(),
                    self.remarks_entry.get(),
                )
                admin_database.add_record(data)
                self.show_added()
                self.tree.yview_moveto(1)
                messagebox.showinfo("Add info", f"Added FILE : {self.file_no_entry.get()} !")
                self.clear()

    def delete(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning('WARNING!', 'Choose a record to delete')
        else:
            sl_no = self.tree.item(self.tree.focus())['values'][0]
            data = admin_database.fetch_by_sl_No(sl_no)
            if messagebox.askokcancel(title="Confirm", message=f"Do you want to delete FILE : {data[4]} ?",
                                      default="cancel"):
                admin_database.delete_record(sl_no)
                self.add_to_treeview()
                self.clear()

    def update(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning('WARNING!', 'Choose a record to Update!')
        else:
            if self.check_entry():
                sl_no = self.tree.item(self.tree.focus())['values'][0]
                data = (
                    int(self.bundle_no_entry.get()),
                    self.locker_no_entry.get(),
                    int(self.row_no_entry.get()),
                    self.file_no_entry.get(),
                    self.subject_entry.get("1.0", END).strip(),
                    self.description_entry.get("1.0", END).strip(),
                    self.hint_1_entry.get(),
                    self.hint_2_entry.get(),
                    self.remarks_entry.get(),
                    sl_no
                )
                x = admin_database.fetch_by_sl_No(sl_no)
                if x[1:] == data[:-1]:
                    messagebox.showwarning("Warning", "No changes detected, Update failed")
                else:
                    admin_database.update_record(data)
                    self.add_to_treeview()
                    messagebox.showinfo("Update info", f"Updated FILE : {self.file_no_entry.get()} !")
                    self.clear()

    def clear_button(self):
        self.clear()
        self.tree.selection_remove(self.tree.selection())

    def clear(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')
        self.bundle_no_entry.delete(0, END)
        self.locker_no_entry.delete(0, END)
        self.row_no_entry.delete(0, END)
        self.file_no_entry.delete(0, END)
        self.subject_entry.delete("1.0", END)
        self.description_entry.delete("1.0", END)
        self.hint_1_entry.delete(0, END)
        self.hint_2_entry.delete(0, END)
        self.remarks_entry.delete(0, END)

    def show_added(self):
        all_records = database.added()
        self.tree.delete(*self.tree.get_children())

        TRUNCATE_FILE_NUMBER_LENGTH = 15
        TRUNCATE_DESCRIPTION_LENGTH = 20


        def format_string(s, length):
            # Remove newlines and replace with spaces
            formatted_str = ' '.join(s.splitlines())
            # Truncate if necessary and add "..."
            return formatted_str[:length] + '...' if len(formatted_str) > length else formatted_str

        for repo in all_records:
            tableview_id = repo[0]
            tableview_filenumber = format_string(repo[4],TRUNCATE_FILE_NUMBER_LENGTH)
            tableview_description = format_string(repo[6],TRUNCATE_DESCRIPTION_LENGTH)

            self.tree.insert('', END, values=(tableview_id, tableview_filenumber, tableview_description))




    def add_to_treeview(self, search_result=None):
        """
        add/shows the data to table
        :return: None
        """
        TRUNCATE_FILE_NUMBER_LENGTH = 15
        TRUNCATE_DESCRIPTION_LENGTH = 20

        def format_string(s, length):
            # Remove newlines and replace with spaces
            formatted_str = ' '.join(s.splitlines())
            # Truncate if necessary and add "..."
            return formatted_str[:length] + '...' if len(formatted_str) > length else formatted_str


        if search_result is None:
            all_repos = database.fetch_all_records()
        else:
            all_repos = search_result

        self.tree.delete(*self.tree.get_children())  # prevent inserting same row multiple times

        for repo in all_repos:
            tableview_id = repo[0]
            tableview_filenumber = format_string(repo[4],TRUNCATE_FILE_NUMBER_LENGTH)
            tableview_description = format_string(repo[6],TRUNCATE_DESCRIPTION_LENGTH)
                
            self.tree.insert('', END, values=(tableview_id, tableview_filenumber, tableview_description))

    def display_data(self, event):
        try:
            selected_item = self.tree.item(self.tree.focus())['values'][0]
            if selected_item:
                data = database.fetch("Sl_No", selected_item)
                self.clear()
                self.bundle_no_entry.insert(0, str(data[0][1]))
                self.locker_no_entry.insert(0, str(data[0][2]))
                self.row_no_entry.insert(0, str(data[0][3]))
                self.file_no_entry.insert(0, str(data[0][4]))
                self.subject_entry.insert("1.0", str(data[0][5]))
                self.description_entry.insert("1.0", str(data[0][6]))
                self.hint_1_entry.insert(0, str(data[0][7]))
                self.hint_2_entry.insert(0, str(data[0][8]))
                self.remarks_entry.insert(0, str(data[0][9]))
        except IndexError:
            pass

    def handle_click(self, event):
        if self.tree.identify_region(event.x, event.y) == "separator":
            return "break"

    def mycallback(self, event):
        try:
            _iid = self.tree.identify_row(event.y)
            if _iid != self.last_focus:
                if self.last_focus:
                    self.tree.item(self.last_focus, tags=[])
                self.tree.item(_iid, tags=['focus'])
                self.last_focus = _iid
        except _tkinter.TclError:
            pass

    def search_admin(self):
        self.clear()
        self.add_to_treeview(database.search_all(self.search_entry.get().strip()))

