
from tkinter import Button, Entry, Listbox, Scrollbar
from tkinter import S, W
from tkinter import END
from tkinter import VERTICAL
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
    column=0, columnspan=5,
    sticky=W)


#####################################################
#                SEARCH RESULTS                     #
#####################################################


search_results_scroll = Scrollbar(
    master=main_window,
    orient=VERTICAL
)
search_results_scroll.grid(
    row=1, rowspan=5,
    column=5,
)

search_results = Listbox(
    master=main_window,
    background="green",
    yscrollcommand=search_results_scroll.set
)
search_results.grid(
    row=1, rowspan=5,
    column=0, columnspan=5,
    sticky=S
)

search_results_scroll.config(
    command=search_results.yview
)


#####################################################
#                 SEARCH BUTTON                     #
#####################################################


def search_for_employee():
    employee_query = search_input_value.get()
    employee_results = db.fetch(employee_query)
    if len(employee_results) > 0:
        # Get only the 1st result
        name, eid, role = employee_results[0]
        display = f"{name}, {eid}, {role}"
    else:
        display = f"No match for '{employee_query}''"
    search_results.delete(0, END)
    search_results.insert(END, display)

search_btn = Button(
    master=main_window,
    text="Search",
    command=search_for_employee)
search_btn.grid(
    row=0,
    column=5, columnspan=1,
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
