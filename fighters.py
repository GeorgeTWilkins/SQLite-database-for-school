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
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<4}{fighter[4]:<4}{fighter[5]:<4}{fighter[6]:<4}")
    #loop finsihed now
    db.close()



#main code
print_all_aircraft()


