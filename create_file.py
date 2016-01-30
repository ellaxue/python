import sys

def create_file():
	name = raw_input("name of the file ")+".txt"
	
	try:
		file = open(name,'a')
		file.close()
	except:
		print("something went wrong")
		sys.exit(0)
create_file()

