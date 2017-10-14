#Carol Pan
#SoftDev1 pd7
#HW9 -- No Treble
#2017-10-14

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================


#creating first table

#put SQL statement in this string
command = "CREATE TABLE peeps (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)" 
c.execute(command)    #run SQL statement

#open le file and make dicts
with open ('peeps.csv') as csvfile: 
    peeps = csv.DictReader(csvfile)
    '''what does this come out as?
    for row in peeps:
        print row
    '''
    for row in peeps:
        command = "INSERT INTO peeps VALUES ("+ row["id"] + ",\"" + row["name"] + "\"," + row["age"] + ")"
        c.execute(command)


#second table
#put SQL statement in this string
command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)" 
c.execute(command)    #run SQL statement

#open file
with open ('courses.csv') as csvfile:
    course = csv.DictReader(csvfile)
    for row in course:
        command = "INSERT INTO courses VALUES (" + row["id"] + ",\"" + row["code"] + "\"," + row["mark"] + ")"
        c.execute(command)






#==========================================================
db.commit() #save changes
db.close()  #close database


