
from tkinter import Button, Entry, Text
from tkinter import N, S, E, W, END
from tkinter import StringVar
from tkinter import Tk

from appdb import EmployeesDB


#####################################################
#                 APP DATABASE                      #
#####################################################


db = EmployeesDB()
db.connect()
db.create_table()
db.insert_employee("Bob", "001", "DEV")
db.insert_employee("Charlie", "002", "DEV")
db.insert_employee("John", "003", "QA")
print(db.fetch_all())
db.delete_employee("002")
print(db.fetch_all())
db.update_employee_name("001", "Bobby")
db.update_employee_position("003", "QA Lead")
print(db.fetch_all())


#####################################################
#                  MAIN WINDOW                      #
#####################################################


main_window = Tk()
main_window.resizable(width=False, height=False)


#####################################################
#                 SEARCH INPUT                      #
#####################################################


search_input_value = StringVar()
search_input = Entry(
    master=main_window,
    textvariable=search_input_value)
search_input.grid(
    row=0,
    column=0, columnspan=3,
    sticky=W)


#####################################################
#                SEARCH RESULTS                     #
#####################################################


search_results = Text(
    master=main_window,
    background="green",
    height=10,
    width=40)
search_results.grid(
    row=1,
    column=0, columnspan=4,
    sticky=S)


#####################################################
#                 SEARCH BUTTON                     #
#####################################################


def search_for_employee():
    employee_query = search_input_value.get()
    employee_results = db.fetch(employee_query)
    if len(employee_results) > 0:
        # Get only the 1st result
        name, eid, role = employee_results[0]
        display = f"Found!\n  Name:{name}\n  ID:{eid}\n  Role:{role}"
    else:
        display = f"No match for '{employee_query}''"
    search_results.delete(1.0, END)
    search_results.insert(END, display)

search_btn = Button(
    master=main_window,
    text="Search",
    command=search_for_employee)
search_btn.grid(
    row=0,
    column=3, columnspan=1,
    sticky=W)


#####################################################
#                    MAIN LOOP                      #
#####################################################

def on_close():
    print("Closing..")
    db.disconnect()
    main_window.destroy()

main_window.protocol("WM_DELETE_WINDOW", on_close)
main_window.mainloop()
