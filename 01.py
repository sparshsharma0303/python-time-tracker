import sqlite3
import datetime

def show_list():
    pass

def add_task():
    pass

def update_task():
    pass

def track_task():
    pass

def main():
    while(True):
        print("enter 1 to show complete list:\n")
        print("enter 2 to add tasks:\n")
        print("enter 3 to update task:\n")
        print("enter 4 to track:\n")
        print("enter 5 to exit:\n")
        
    
        choice = input("enter your choice:\n")

        match(choice):
            case '1':
                show_list()

            case '2':
                add_task()

            case '3':
                update_task()

            case '4':
                track_task()

            case '5':
                break
  