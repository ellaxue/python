import MySQLdb

db = MySQLdb.connect("localhost","root","wb3331314","TESTDB")

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE(
	FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), 	INCOME FLOAT)"""


cursor.execute(sql)
print 'created table EMPLOYEE'

 
# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
	print 'fail to insert'
	# Rollback in case there is any error
   	db.rollback()  

cursor.execute("""SELECT * FROM EMPLOYEE""")
for row in cursor:
	print (row[1])

db.close()

