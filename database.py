import sqlite3

# Connect to simpsons database
conn = sqlite3.connect('simpsons.db')

def createTable():
    conn.execute("CREATE TABLE if not exists \
        SIMPSONS_INFO( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        NAME TEXT, \
        GENDER TEXT, \
        AGE INT, \
        OCCUPATION TEXT \
        );")
    
def printData(data):
    for row in data:
        print "Id:", row[0]
        print "Name:", row[1]
        print "Gender:", row[2]
        print "Age:", row[3]
        print "Occupation:", row[4], "\n"

def newCharacter(name,gender,age,occupation):   
    # Create values part of sql command
    val_str = "'{}', '{}', {}, '{}'".format(\
        name, gender, age, occupation)
    
    sql_str = "INSERT INTO SIMPSONS_INFO \
        (NAME, GENDER, AGE, OCCUPATION) \
        VALUES ({});".format(val_str)
    print sql_str
    
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes
    
def viewAll():
    # Create sql string
    sql_str = "SELECT * from SIMPSONS_INFO"
    cursor = conn.execute(sql_str)
    
    # Get data from cursor in array
    rows = cursor.fetchall()
    return rows

def updateCharacter(change_id,name,gender,age,occupation):
    # Create values part of sql command
    val_str = "NAME='{}', GENDER='{}',\
              AGE={}, OCCUPATION='{}'".format(\
              name, gender, age, occupation)
    
    sql_str = "UPDATE SIMPSONS_INFO set \
       {} where ID={};".format(val_str,change_id)
    print sql_str
    
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

def deleteCharacter(change_id):
    # Create sql string
    sql_str = "DELETE from SIMPSONS_INFO where ID={}"\
             .format(change_id)
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

createTable()

        


