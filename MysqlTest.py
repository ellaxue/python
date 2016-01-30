import MySQLdb

db = MySQLdb.connect("localhost","root","wb3331314","TESTDB",local_infile = 1)

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE(
	FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20), AGE INT, SEX CHAR(1), INCOME FLOAT)"""

cursor.execute(sql)
print 'created table EMPLOYEE'
 
# Prepare SQL query to IMPORT data file into the database.
sql = """LOAD DATA LOCAL INFILE 'input.txt' INTO TABLE EMPLOYEE
		FIELDS TERMINATED BY '\t'
		LINES TERMINATED BY '\n' """
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit changes in the database
   db.commit()
except:
	print 'fail to insert'
	# Rollback in case there is any error
   	db.rollback()  

cursor.execute("""SELECT * FROM EMPLOYEE""")
result = cursor.fetchall()
for row in result:
	print row

db.close()

