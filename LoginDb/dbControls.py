file1 = open("LoginDb.sql", "w")
#File_object.writelines(L) for L = ["CREATE TABLE Users{" ,"UniqueID int","Username varchar(255),", "}"]


file1.close()

def readinUsers(String[] users )
	for 
	readin()

def readin(String select, String frm, String where):
 try:
        connDBI = mariadb.connect(
            user="ms",
            password="+DAB-team+",
            host="149.165.155.188",
            port=3306,
            database="ms"
            
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    c = connDBI.cursor()
    try:
    	stmt ="SELECT %s FROM %s WHERE %s"
    	data =(select, frm, where)
    	if c.execute(stmt,data):
    except mariadb.Error as e:	
    	print(f"Error retriving data")
     
        
def insertUser(int ID, String name):
 try:
        connDBI = mariadb.connect(
            user="ms",
            password="+DAB-team+",
            host="149.165.169.119",
            port=3306,
            database="ms"
            
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    c = connDBI.cursor()
    if c.execute('insert into usernames (uniqueID, name) VALUE (%i, %s)', (ID,name) ):
        
