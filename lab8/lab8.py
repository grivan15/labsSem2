import sqlite3
conn = sqlite3.connect(r':memory:')
cur = conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS Classes(
    class varchar(50) PRIMARY KEY NOT NULL,
    type varchar(2) NOT NULL,
    country varchar(20) NOT NULL,
    numGuns INT,
    bore REAL,
    displacement INT);
""")
conn.commit()
cur.execute(""" CREATE TABLE IF NOT EXISTS Ships(
    name varchar(50) PRIMARY KEY NOT NULL,
    class varchar(50) NOT NULL,
    launched SMALLINT);
""")
conn.commit()
cur.execute(""" CREATE TABLE IF NOT EXISTS Outcomes(
    ship varchar(50) PRIMARY KEY NOT NULL,
    battle varchar(20) NOT NULL,
    result varchar(10) NOT NULL);
""")
conn.commit()
cur.execute(""" CREATE TABLE IF NOT EXISTS Battles(
    name varchar(20) PRIMARY KEY NOT NULL,
    [date] datetime NOT NULL);
""")
conn.commit()

aClasses = [('c1', 'bb', 'russia', 5, 90, 3000),
           ('c2', 'bc', 'germany', 6, 50, 2000),
           ('c3', 'bb', 'USA', 8, 30, 1500)]
aShips = [('s1', 'c1', 1900),
         ('s2', 'c1', 1910),
         ('s3', 'c1', 1920),
         ('s4', 'c2', 1930),
         ('s5', 'c2', 1940),
         ('s6', 'c2', 1950),
         ('s7', 'c3', 1960)]
aOutcomes = [('s1','Fourth World War', 'damaged'),
            ('s2','First World War', 'damaged'),
            ('s3','First World War', 'passed'),
            ('s4','Third World War', 'passed'),
            ('s5','Second World War', 'passed'),
            ('s6','Third World War', 'passed'),
            ('s7','Second World War', 'damaged')]
aBattles = [
    ('b1', '2005-01-01'),
    ('b2','2005-01-02'),
    ('b3','2005-01-03'),
    ('b4','2005-01-04')]

cur.executemany("INSERT INTO Classes VALUES(?, ?, ?, ?, ?, ?);", aClasses)
cur.executemany("INSERT INTO Ships VALUES(?, ?, ?);", aShips)
cur.executemany("INSERT INTO Outcomes VALUES(?, ?, ?);", aOutcomes)
cur.executemany("INSERT INTO Battles VALUES(?, ?);", aBattles)
conn.commit()

cur.execute("""SELECT class, MIN(launched) FROM Ships GROUP BY class""")
print(cur.fetchall())