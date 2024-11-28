import _tkinter
from tkinter import *

# DATABASE IMPORT
import database_user as database


class UserFunctions:
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



    def change_state(self, normal=True):
        if normal:
            self.bundle_no_entry.configure(state="normal")
            self.locker_no_entry.configure(state="normal")
            self.row_no_entry.configure(state="normal")
            self.file_no_entry.configure(state="normal")

            self.subject_entry.configure(state="normal")
            self.description_entry.configure(state="normal")

            self.hint_1_entry.configure(state="normal")
            self.hint_2_entry.configure(state="normal")
            self.remarks_entry.configure(state="normal")
        elif not normal:
            self.bundle_no_entry.configure(state="readonly")
            self.locker_no_entry.configure(state="readonly")
            self.row_no_entry.configure(state="readonly")
            self.file_no_entry.configure(state="readonly")

            self.subject_entry.configure(state="disabled")
            self.description_entry.configure(state="disabled")

            self.hint_1_entry.configure(state="readonly")
            self.hint_2_entry.configure(state="readonly")
            self.remarks_entry.configure(state="readonly")

    def clear(self, *clicked):
        if clicked:
            # remove highlighted
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')

        self.change_state(normal=True)
        self.bundle_no_entry.delete(0, END)
        self.locker_no_entry.delete(0, END)
        self.row_no_entry.delete(0, END)
        self.file_no_entry.delete(0, END)

        self.subject_entry.delete("1.0", END)
        self.description_entry.delete("1.0", END)

        self.hint_1_entry.delete(0, END)
        self.hint_2_entry.delete(0, END)
        self.remarks_entry.delete(0, END)

    def display_data(self, event):
        """
        if a row is selected all its data will be available
         in the corresponding entry boxes
        :param event: event listener -> '<ButtonRelease>'
        :return: None
        """
        try:
            selected_item = self.tree.item(self.tree.focus())['values'][0]

            if selected_item:
                # 2 files with same file name but only 1 details is showing
                # soln 1 :- avoid duplicate file_name   -> not in my control
                # soln 2 :- show sl_No on trees_view     -> done!
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

                self.change_state(normal=False)
        except IndexError:
            pass

    def search(self):
        key = self.search_entry.get("1.0", END).strip()
        if len(key) != 0:
            col_id = self.variable1.get()  # ['All','Sl_no',...]

            if col_id == 'All':
                self.clear()
                self.add_to_treeview(database.search_all(key))

            else:
                self.clear()
                self.add_to_treeview(database.fetch(col_id, key))
        else:
            self.add_to_treeview()

    def handle_click(self, event):
        if self.tree.identify_region(event.x, event.y) == "separator":
            return "break"
