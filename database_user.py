# everything for database-user
import sqlite3


def create_table():
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS record (
        Sl_No INTEGER,
        Bundle_No INTEGER,
        Locker_No TEXT,
        Row_No INTEGER,
        File_No TEXT,
        Subject TEXT,
        Description TEXT,
        Hint_1 TEXT,
        Hint_2 TEXT,
        Remarks TEXT
    )""")

    conn.commit()
    conn.close()


def fetch_all_records():
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM record LIMIT 200')
    # why limit?
    # loading 1 lakh records from database -> lag in performance
    # So we just reduce the load from 1 lakh to just 200
    employees = cursor.fetchall()
    conn.close()

    return employees


def added():
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM record ORDER BY Sl_No DESC LIMIT 30;")
    result = cursor.fetchall()

    conn.close()
    return result[::-1]


def fetch(col_id, value):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM record WHERE {col_id} LIKE '{value}%'")

    except sqlite3.OperationalError:
        pass

    result = cursor.fetchall()
    conn.close()

    return result


def search_all(value):
    conn = sqlite3.connect('records.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            f"""SELECT * FROM record WHERE
             Locker_No LIKE '%{value}%' OR
             File_No LIKE '%{value}%' OR 
             Subject LIKE '%{value}%' OR 
             Description LIKE '%{value}%' OR 
             Hint_1 LIKE '%{value}%' OR 
             Hint_2 LIKE '%{value}%' OR 
             Remarks LIKE '%{value}%'
            """)

    except sqlite3.OperationalError:
        print('oprtnerr')
        pass

    result = cursor.fetchall()
    conn.close()

    return result

