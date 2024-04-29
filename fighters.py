#Database application - George Wilkins - Following tutorial
#Imports

import sqlite3

#constants and variables

DATABASE = "fighters.db"



#functions
def print_all_aircraft():
    '''print all the aircraft data neatly'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighters;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results first
    for fighter in results:
        print(fighter)
    #loop finsihed now
    db.close()



#main code
print_all_aircraft()


