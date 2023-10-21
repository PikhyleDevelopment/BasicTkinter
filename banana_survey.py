"""A banana preferences survey written in Python with Tkinter"""
import tkinter as tk

# Our root window
root = tk.Tk()
# Set the root window title
root.title('Banana interest survey')
# Set the root window size
root.geometry('640x480+300+300')
# Disable resize of root window
root.resizable(False, False)

# Add our title widget
title = tk.Label(
    root,
    text='Please take the survey',
    font='Ariel 16 bold',
    bg='brown',
    fg='#FF0'
)

# Our name label and input
name_var = tk.StringVar(root)
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root, textvariable=name_var)
# Check button
eater_var = tk.BooleanVar()
eater_inp = tk.Checkbutton(
    root,
    variable=eater_var,
    text='Check this box if you eat bananas'
)

# How many bananas?
num_var = tk.IntVar(value=3)
num_label = tk.Label(
    root,
    text='How many bananas do you ear per day?'
)
num_inp = tk.Spinbox(
    root,
    textvariable=num_var,
    from_=0,
    to=1000,
    increment=1
)

# A ListBox to choose a color
color_var = tk.StringVar(value='Any')
color_label = tk.Label(
    root,
    text='What is the best color for a banana?'
)
# add choices
color_choices = (
    'Any', 'Green', 'Green-Yellow',
    'Yellow', 'Brown Spotted', 'Black'
)
color_inp = tk.OptionMenu(
    root, color_var, *color_choices
)

# Radio Button input to answer a simple Yes/No question
plantain_label = tk.Label(root, text='Do you eat plantains?')
plantain_frame = tk.Frame(root)
plantain_var = tk.BooleanVar()
plantain_yes_inp = tk.Radiobutton(
    plantain_frame,
    text='Yes',
    value=True, variable=plantain_var
)
plantain_no_inp = tk.Radiobutton(
    plantain_frame,
    text='Ewww, no!',
    value=False,
    variable=plantain_var
)

# Multi-line text entry
banana_haiku_label = tk.Label(
    root,
    text='Write a haiku about bananas'
)
banana_haiku_inp = tk.Text(root, height=3)

# Complete the survey with a submit button
submit_btn = tk.Button(root, text='Submit Survey')


def on_submit():
    """To be run when the user submits the form"""
    name = name_var.get()
    try:
        number = num_var.get()
    except tk.TclError:
        number = 10_000

    color = color_var.get()
    banana_eater = eater_var.get()
    plantain_eater = plantain_var.get()
    haiku = banana_haiku_inp.get('1.0', tk.END)
    message = f'Thanks for taking the survey, {name}.\n'
    if not banana_eater:
        message += "Sorry you don't like bananas!\n"
    else:
        message += f'Enjoy your {number} {color} bananas!\n'
    if plantain_eater:
        message += 'Enjoy your plantains!'
    else:
        message += 'May you successfully avoid plantains!'
    if haiku.strip():
        message += f'\n\nYour Haiku:\n{haiku}'
    output_var.set(message)
    print(haiku)
    print(name_var.get())


submit_btn.configure(command=on_submit)

# Use a label to display a message during runtime
output_var = tk.StringVar(value='')
output_line = tk.Label(
    root,
    textvariable=output_var,
    anchor='w',
    justify='left'
)

# Use grid geometry manager to arrange widgets in a 2D grid
title.grid(columnspan=2)
# Counting from top-left, starting at 0
name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)
eater_inp.grid(row=2, columnspan=2, sticky='we')  # sticky tells Tk to stick the sides indicated by cardianl direction
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))
color_label.grid(row=4, columnspan=2, stick=tk.W, pady=10)  # Pad y axis by 10 (external)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)  # Pad x axis by 25 (external)
plantain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)  # ipadx and y are internal padding
plantain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, sticky=tk.W)
banana_haiku_label.grid(row=8, columnspan=2, sticky=tk.W)
banana_haiku_inp.grid(row=9, columnspan=2, sticky='NSEW')
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky='NSEW')

# Expand the second column into unused space
root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

root.mainloop()
