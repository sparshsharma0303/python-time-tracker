import sqlite3
from datetime import datetime,timedelta 
import time 

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
        print('-'*50)
        time.sleep(0.5)

    print('*'*50)
# ------------------------------------------------------------------------------------------------------


def add_task(name,date,start_time,end_time):
    cursor.execute("INSERT INTO time_tracker (name , date, start_time, end_time) VALUES(?,?,?,?)",(name,date,start_time,end_time))
    conn.commit()
    time.sleep(0.5)
    print("data entered succesfully")
    print('*'*50)

# ------------------------------------------------------------------------------------------------------

def update_task(id,name,date,start_time,end_time):
    cursor.execute("UPDATE time_tracker SET name = ?,date = ?, start_time = ?, end_time = ? WHERE id = ?",(name,date,start_time,end_time,id))
    conn.commit()
    time.sleep(0.5)
    print('*'*50)

# ------------------------------------------------------------------------------------------------------


def delete_task(id):
    cursor.execute("DELETE FROM time_tracker WHERE id = ?",(id,))
    conn.commit()
    time.sleep(0.5)
    print("task deleted succefully")
    print('*'*50)

# ------------------------------------------------------------------------------------------------------
    
def track_task(name):
    row = cursor.execute("SELECT date,start_time, end_time FROM time_tracker where LOWER(name) = LOWER(?)",(name,)).fetchall()

    if not row :
        print("no record found")
        print('*'*50)
        time.sleep(0.5)
    else:
        print(f"your time routine for {name} is as follow :")
        print('-'*50)
        for da, st , et in row:
            print(f"on {da} start time: {st} and end time: {et}")
            print('-'*50)
            time.sleep(0.5)
        
    print('*'*50)

# ------------------------------------------------------------------------------------------------------

def track_day(date):
    res = cursor.execute("SELECT * FROM time_tracker WHERE date = ?",(date,))
    if not res :
        print("no record found")
        print('*'*50)
        time.sleep(0.5)
    else:
        print("your record for date {date} is:\n")
        print('-'*50)
        time.sleep(0.5)
        for row in res :
            print(row)
            print('-'*50)
            time.sleep(0.5)

# -------------------------------------------------------------------------------------------------------------

def total_time_spent(task_name):

    res = cursor.execute("SELECT start_time, end_time FROM time_tracker WHERE name = ?",(task_name,))
    total_duration = timedelta()
    for st, et in res :
        st_obj  = datetime.strptime(st,"%H:%M")
        et_obj  = datetime.strptime(et,"%H:%M")
        accumulator = et_obj-st_obj
        total_duration += accumulator
    
    print(f"the total time you spent doing{task_name} is {total_duration}")
    

# -------------------------------------------------------------------------------------------------------------


def main():
    while(True):
        print("enter 1 to show complete list:\n")
        time.sleep(0.25)
        print("enter 2 to add tasks:\n")
        time.sleep(0.25)
        print("enter 3 to update task:\n")
        time.sleep(0.25)
        print("enter 4 to track specific task:\n")
        time.sleep(0.25)
        print("enter 5 to fetch record of specific day:\n")
        time.sleep(0.25)
        print("enter 6 to delete:\n")
        time.sleep(0.25)
        # print("enter 7 to track today:\n")
        time.sleep(0.25)
        print("enter 7 to fetch total time spent doing the task ")
        time.sleep(0.25)
        print("enter 8 to break ")
        
    
        choice = input("enter your choice:\n")

        match(choice):
            case '1':
                show_list()

            case '2':
                name = input("enter the task name:\n")
                time.sleep(0.5)
                while True:
                    try:
                        date = input("enter the date in format dd-mm-yyyy:\n")
                        date_obj = datetime.strptime(date,"%d-%m-%Y").date()
                        time.sleep(0.5)
                        break
                    except ValueError:
                        print("enter the correct date,")

                print('*'*50)
                while True:
                    try:
                        start_time = input("enter the start time in format hh:mm:\n")
                        st_format = datetime.strptime(start_time, "%H:%M").time()
                        print('*'*50)
                        time.sleep(0.5)
                        break
                    except ValueError:
                        print("enter the time in correct format,")

                while True:
                    try:
                        end_time = input("enter the end time in format hh:mm:\n")
                        et_format = datetime.strptime(end_time, "%H:%M").time()
                        print('*'*50)
                        break
                    except ValueError:
                        print("enter the time in correct format,")


                while(True):
                    if et_format<st_format :
                        print("ending timing must be after start time:\n")
                        end_time = input("enter the end time in format hh:mm:\n")
                        print('*'*50)
                        et_format = datetime.strptime(end_time, "%H:%M").time()
                    else:
                        break
                            

                add_task(name,date,start_time,end_time)

            case '3':
                id = input("enter the id of the task you want to update:\n")
                time.sleep(0.5)

                name = input("enter the new task name:\n")
                time.sleep(0.5)

                print('*'*50)
                while True:
                    try:
                        date = input("enter the new date in format dd-mm-yyyy:\n")
                        date_obj = datetime.strptime(date,"%d-%m-%Y").date()
                        time.sleep(0.5)
                        break
                    except ValueError:
                        print("enter the correct date,")
                while True:
                    try:
                        start_time = input("enter the new start time in format hh:mm:\n")
                        st_format = datetime.strptime(start_time, "%H:%M").time()
                        print('*'*50)
                        time.sleep(0.5)
                        break
                    except:
                        print("please enter correct time,")
                        
                while True:
                    try:
                        end_time = input("enter the new pyend time in format hh:mm:\n")
                        et_format = datetime.strptime(end_time, "%H:%M").time()
                        print('*'*50)
                        time.sleep(0.5)
                        break

                    except:
                        print("please enter correct time, ")


                while(True):
                    if et_format<st_format :
                        print("ending timing must be after start time:\n")
                        end_time = input("enter the end time in format hh:mm:\n")
                        print('*'*50)
                        time.sleep(0.5)
                        et_format = datetime.strptime(end_time, "%H:%M").time()
                    else:
                        break

                update_task(id,name,date,start_time,end_time)

            case '4':
                show_list()
                print('*'*50)
                name = input("enter the name of task you want to track:\n")
                print('*'*50)
                time.sleep(0.5)
                track_task(name)
            case '5':
                while True:
                    try:
                        date = input("enter the date in dd-mm-yyyy format you want to fetch data of:\n")
                        date_obj = datetime.strptime(date,"%d-%m-%Y").date()
                        time.sleep(0.5)
                        break
                    except ValueError:
                        print("enter the correct date,")
                time.sleep(0.5)
                track_day(date)
            case '6':
                id = input("enter the id of task you want to delete:\n")
                print('*'*50)
                time.sleep(0.5)
                delete_task(id)

            case '7':
                name = input("enter the name of task you want to calculate total time spent:\n")
                total_time_spent(name)
            
            case '8':
                break

            
            

if __name__ == "__main__":
    main()

conn.close()