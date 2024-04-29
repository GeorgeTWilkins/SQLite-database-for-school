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
    print("Name                          Speed   Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finsihed now
    db.close()

def print_all_aircraft_sorted_speed_desc():
    '''print all the aircraft data neatly, ordered by speed desc'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighters ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results first
    print("Name                          Speed   Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finsihed now
    db.close()

def print_all_aircraft_sorted_climb_rate_desc():
    '''print all the aircraft data neatly, ordered by climb rate desc'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighters ORDER BY climbrate DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results first
    print("Name                          Speed   Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finsihed now
    db.close()

def print_all_aircraft_sorted_range_desc():
    '''print all the aircraft data neatly, ordered by range desc'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighters ORDER BY range DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results first
    print("Name                          Speed   Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finsihed now
    db.close()

def print_all_aircraft_sorted_payload_desc():
    '''print all the aircraft data neatly, ordered by payload desc'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighters ORDER BY payload DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results first
    print("Name                          Speed   Max_g Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finsihed now
    db.close()



#main code
while True:
    user_input = input("\nWhat would you like to do.\n1. Print all aircraft\n2. Print all aircraft ordered by speed desc\n3. Print all aircraft ordered by climb ratedesc\n4. Print all aircraft ordered by range desc\n5. Print all ordered by payload desc\n0. Exit\n")
    if user_input == "1":
        print_all_aircraft()
    if user_input == "2":
        print_all_aircraft_sorted_speed_desc()
    if user_input == "3":
        print_all_aircraft_sorted_climb_rate_desc()
    if user_input == "4":
        print_all_aircraft_sorted_range_desc()
    if user_input == "5":
        print_all_aircraft_sorted_payload_desc()
    if user_input == "0":
        break
    else:
        print("That was not an option\n")


