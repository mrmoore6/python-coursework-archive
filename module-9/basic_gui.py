
"""
Author: Michael Moore
Date: 10/25/20
This program takes and makes a small program that asks the user what there favorite meal is and returns a comment.
"""
import tkinter
def option_one():
    label.config(text="Most important meal of day!")
def option_two():
    label.config(text = "Two is better than one!")
def option_three():
    label.config(text = "Lunch always comes at the right time!")
def option_four():
    label.config(text = "I love dinner too!")


m = tkinter.Tk()
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)
meal1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=meal1, command=option_one).grid(row=1)
meal2 = tkinter.IntVar()
check2 = tkinter.Checkbutton(m, text="Second Breakfast", variable=meal2, command=option_two).grid(row=2)
meal3 = tkinter.IntVar()
check3 = tkinter.Checkbutton(m, text="Lunch", variable=meal3, command=option_three).grid(row=3)
meal4 = tkinter.IntVar()
check4 = tkinter.Checkbutton(m, text="Dinner", variable=meal4, command=option_four).grid(row=4)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)
m.mainloop()
