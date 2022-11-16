import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE messages(dialog_id, content, update_time)")
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()