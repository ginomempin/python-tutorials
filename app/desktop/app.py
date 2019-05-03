
from tkinter import Button, Entry, Text
from tkinter import N, S, E, W, END
from tkinter import StringVar
from tkinter import Tk


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


def search_for_member():
    member_query = search_input_value.get()
    member_results = member_query.title()
    search_results.delete(1.0, END)
    search_results.insert(END, "Found '{}'!".format(member_results))

search_btn = Button(
    master=main_window,
    text="Search",
    command=search_for_member)
search_btn.grid(
    row=0,
    column=3, columnspan=1,
    sticky=W)


#####################################################
#                    MAIN LOOP                      #
#####################################################

main_window.mainloop()
