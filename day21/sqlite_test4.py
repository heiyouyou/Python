import sqlite3,os

db_file = os.path.join(os.path.dirname(__file__), 'test4.db')
if os.path.isfile(db_file):
    os.remove(db_file)
conn = sqlite3.connect(db_file)
print "Opened database successfully";
c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully";
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
print "Records created successfully";

cursor1 = c.execute("SELECT id, name, address, salary  from COMPANY") #每次返回的是执行语句的一个Cursor对象
print cursor1
for row in cursor1:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"
print "Operation select done successfully";

c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
print "Total number of rows updated :", conn.total_changes

cursor2 = conn.execute("SELECT id, name, address, salary  from COMPANY")
print cursor2
for row in cursor2:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation update done successfully";

c.execute("DELETE from COMPANY where ID=2;")
print "Total number of rows deleted :", conn.total_changes
cursor3 = conn.execute("SELECT id, name, address, salary  from COMPANY")
print cursor3
for row in cursor3:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation delete done successfully";

conn.commit()
conn.close()