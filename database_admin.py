# everything database-admin
import sqlite3


def insert_records(l):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO record VALUES (?,?,?,?,?,?,?,?,?,?)", l)

    conn.commit()
    conn.close()

def last_sl_no():
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM record ORDER BY Sl_No DESC LIMIT 1;")
    result = cursor.fetchone()

    conn.close()
    return 0 if result is None else result[0]


# print(last_sl_no())


def check_record_exists(file_no):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM record WHERE File_No = ?", (file_no,))

    result = cursor.fetchone()
    conn.close()

    return result[0] > 0


def fetch_by_sl_No(sl_no):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM record WHERE Sl_No = ?", (sl_no,))
    result = cursor.fetchone()

    conn.close()
    return result


def add_record(l):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO record VALUES (?,?,?,?,?,?,?,?,?,?)""", l)

    conn.commit()
    conn.close()


# FOR TESTING PURPOSES
# for i in range(300001, 400001):
#     if i % 10000 == 0:
#         print(i)
#     i = str(i)
#     add_record([int(i), int(i), i, int(i), i, i, i, i, i, i])


def delete_record(sl_no):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM record WHERE Sl_No = ?", (sl_no,))

    conn.commit()
    conn.close()


def update_record(data):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE record SET 
        Bundle_No = ?,
        Locker_No = ?,
        Row_No = ?,
        File_No = ?,
        Subject = ?,
        Description = ?,
        Hint_1 = ?,
        Hint_2 = ?,
        Remarks = ? WHERE Sl_No = ?
        """, data)

    conn.commit()
    conn.close()
