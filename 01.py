import sqlite3
import datetime
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS time_tracker(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
date TEXT NOT NULL,
start_time TEXT NOT NULL,
end_time TEXT NOT NULL
)'''
)
# ----------------------------------------------------------------------------------------------------------------------------------------------

def show_list():
    res = cursor.execute("SELECT * FROM time_tracker")
    for row in res:
        print(row)

def add_task(name,date,start_time,end_time):
    cursor.execute("INSERT INTO time_tracker (name , date, start_time, end_time) VALUES(?,?,?,?)",(name,date,start_time,end_time))
    conn.commit()
    print("data entered succesfully")

def update_task(id,name,date,start_time,end_time):
    cursor.execute("UPDATE time_tracker SET name = ?,date = ?, start_time = ?, end_time = ? WHERE id = ?",(name,date,start_time,end_time,id))
    conn.commit()

def delete_task(id):
    cursor.execute("DELETE FROM time_tracker WHERE id = ?",(id,))
    conn.commit()
    
def track_task(name):
    row = cursor.execute("SELECT date,start_time, end_time FROM time_tracker where LOWER(name) = LOWER(?)",(name,)).fetchall()

    if not row :
        print("no record found")
    print(f"your time routine for {name} is as follow :")
    for da, st , et in row:
        print(f"on {da} start time: {st} and end time: {et}")





def main():
    while(True):
        print("enter 1 to show complete list:\n")
        print("enter 2 to add tasks:\n")
        print("enter 3 to update task:\n")
        print("enter 4 to track:\n")
        print("enter 5 to delete:\n")
        print("enter 6 to break:\n")
        
    
        choice = input("enter your choice:\n")

        match(choice):
            case '1':
                show_list()

            case '2':
                name = input("enter the task name")
                date = input("enter the date in format dd-mm-yyyy")
                start_time = input("enter the start time in format hh:mm")
                end_time = input("enter the end time in format hh:mm")
                add_task(name,date,start_time,end_time)

            case '3':
                id = input("enter the id of the task you want to update")
                name = input("enter the new task name")
                date = input("enter the new date in format dd-mm-yyyy")
                start_time = input("enter the new start time in format hh:mm")
                end_time = input("enter the new end time in format hh:mm")
                update_task(id,name,date,start_time,end_time)

            case '4':
                name = input("enter the name of task you want to track")
                track_task(name)

            case '5':
                id = input("enter the id of task you want to delete")
                delete_task(id)

            case '6':
                break
            

if __name__ == "__main__":
    main()

conn.close()