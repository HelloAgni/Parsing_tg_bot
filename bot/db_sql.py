import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# <row> TEXT UNIQUE if need,
cur.execute('''
CREATE TABLE IF NOT EXISTS krakoz(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    url TEXT,
    xpath TEXT
);
''')

# default data in DB if need 
# cur.execute('''
# INSERT INTO krakoz(name, url, xpath)
# VALUES
# ('name', 'url', 'xpath');
# ''')

con.commit()
con.close()