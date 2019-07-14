
from tkinter import Button, Entry, Listbox, Scrollbar
from tkinter import S, W
from tkinter import END
from tkinter import VERTICAL
from tkinter import StringVar
from tkinter import Tk

from appdb import EmployeesDB


#####################################################
#                  CONSTANTS                        #
#####################################################


LIST_ITEM_DELIM = ", "


#####################################################
#                 APP DATABASE                      #
#####################################################


db = EmployeesDB()
db.connect()
db.create_table()
db.insert_employee("ADMIN", "ADMIN")
db.insert_employee("Lyn", "DEV")
db.insert_employee("Lynda", "DEV")
db.insert_employee("Charlie", "DEV")
db.insert_employee("John", "QA")
db.insert_employee("Jaclyn", "QA")
print(db.fetch_all())
db.delete_employee(5)
print(db.fetch_all())
db.update_employee_name(2, "Lynnie")
db.update_employee_position(4, "QA Lead")
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


def on_select_item(event):
    selection = search_results.curselection()
    if len(selection) == 0:
        # listbox is empty, ignore click
        return

    item_idx = search_results.curselection()[0]
    item = search_results.get(item_idx)
    _, name, _ = item.split(LIST_ITEM_DELIM)
    search_input.delete(0, END)
    search_input.insert(END, name)


search_results.bind("<<ListboxSelect>>", on_select_item)


#####################################################
#                 SEARCH BUTTON                     #
#####################################################


def search_for_employee():
    search_results.delete(0, END)
    employee_query = search_input_value.get()
    fetch_results = db.fetch(employee_query)
    if len(fetch_results) == 0:
        search_results.insert(END, f"No match for '{employee_query}''")
    else:
        for employee in fetch_results:
            eid, name, role = employee
            list_item = LIST_ITEM_DELIM.join((str(eid), name, role))
            search_results.insert(END, list_item)

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
