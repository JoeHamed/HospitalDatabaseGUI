from tkinter import ttk
from tkinter import *
from ttkthemes import themed_tk as tk
from PIL import Image, ImageTk
import os
import psycopg2
from psycopg2 import OperationalError
from tkinter import messagebox

bg_color = '#ddedea'
FONT_NAME = "pixer"


def get_query(input_text, cursor2, output_text):
    output_text.delete('1.0', 'end')
    query = input_text.get('1.0', 'end')
    cursor2.execute(query)
    for index, row in enumerate(cursor2.fetchall()):
        output_text.insert(f'{index}.0', f'{row}\n')


def get_info(username, password, window):
    Username = username.get()
    Password = password.get()
    # Checking for validity
    second_page()



def first_page():
    # ---------------------- UI Setup ---------------------- #
    window = tk.ThemedTk()
    window.get_themes()
    window.config(bg=bg_color)
    window.set_theme("adapta")
    window_width = 1200
    window_height = 800
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # width x height + x + y
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Images
    wallpaper_image = PhotoImage(file="wallpaper.png")
    hospital_image = PhotoImage(file="Hospital.png")
    meme_image = PhotoImage(file="meme.png")
    meme_photo = Image.open("meme.png")
    resize_image = meme_photo.resize((330, 165), Image.ANTIALIAS)
    new_meme_image = ImageTk.PhotoImage(resize_image)

    # Background
    background_image = Image.open("wallpaper.png")
    resize_background = background_image.resize((1200, 800), Image.ANTIALIAS)
    new_background = ImageTk.PhotoImage(resize_background)
    # Background label

    Background_label = Label(window, image=new_background)
    Background_label.place(x=0, y=0)

    # Hospital Image
    hospital_label = Label(window, image=hospital_image, borderwidth=0)
    hospital_label.config(width=480, height=470, bg=bg_color, pady=60)
    hospital_label.grid(column=1, row=0, columnspan=2)
    # Hospital_canvas = Canvas(width=480, height=470, highlightthickness=0, bg=bg_color)
    # Hospital_canvas.create_image(240, 240, image=hospital_image)
    # Hospital_canvas.grid(column=1, row=0, columnspan=2)

    # Rest of the Labels
    user_label = Label(window, text="Username : ", font=(FONT_NAME, 32, "bold"), padx=130, justify="right", bg=bg_color)
    user_label.config(width=4, height=1)
    user_label.grid(column=0, row=1)

    pass_label = Label(window, text="Password : ", font=(FONT_NAME, 32, "bold"), padx=130, justify="right", bg=bg_color)
    pass_label.config(width=4, height=1)
    pass_label.grid(column=0, row=2)

    # Entries
    user_entry = ttk.Entry(window, width=40, cursor="hand1", font=(FONT_NAME, 15, "bold"))
    user_entry.grid(column=1, row=1, columnspan=2)
    pass_entry = ttk.Entry(window, width=40, show="*", cursor="hand1", font=(FONT_NAME, 15, "bold"))
    pass_entry.grid(column=1, row=2, columnspan=2)

    # Buttons
    login_image = PhotoImage(file="login.png")
    login_button = Button(window, image=login_image, borderwidth=0, bg=bg_color, activebackground=bg_color, command=lambda:get_info(user_entry, pass_entry, window))
    login_button.config(width=360, height=130)
    login_button.grid(column=1, row=3, columnspan=2)

    window.mainloop()


def second_page(window):
    sec_window = Tk()
    sec_window.config(bg=bg_color)
    sec_window_width = 700
    sec_window_height = 500
    screen_width = sec_window.winfo_screenwidth()
    screen_hight = sec_window.winfo_screenheight()
    center_x = int(screen_width / 2 - sec_window_width / 2)
    center_y = int(screen_hight / 2 - sec_window_height / 2)
    # width x hight + x + y

    # sec_window.geometry(f'{sec_window_width}x{sec_window_height}+{center_x}+{center_y}')
    # sec_window.resizable(False, False)
    sec_window.title('pgAdmin')
    # set  transparency level from 0.0 to 1.0
    sec_window.attributes('-alpha', 0.7)
    # make screen always at the top of stack if more than one application is running
    sec_window.attributes('-topmost', 1)
    # add icon instead of default one
    #sec_window.iconbitmap(r'server.ico')
    #sec_window.iconbitmap()
    text_frame = Frame(sec_window)
    h1_label = Label(sec_window, text='Query Editor', bg=bg_color, fg='white', font=('arial', 20))
    h1_label.grid(column=0, row=0, sticky='nw', pady=10)
    input_text = Text(sec_window, height=8)
    input_text.insert('1.0', 'select * from "TABLE NAME"')
    input_text.grid(column=0, row=1)
    # run_image = PhotoImage(file=r'R.png')
    run_image = Image.open('run_button.png')
    resized_img = run_image.resize((80, 80))
    img = ImageTk.PhotoImage(resized_img)
    yscroll_bar = Scrollbar(text_frame)
    yscroll_bar.grid(column=1, row=3, sticky='ns')
    xscroll_bar = Scrollbar(text_frame, orient="horizontal")
    xscroll_bar.grid(column=0, row=4, sticky='we')

    # +++++++++==+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    output_text = Text(text_frame, height=20, wrap='none')
    output_text.grid(column=0, row=3)
    run_button = Button(image=img, text='Run', borderwidth=0, bg=bg_color, compound='right', font=('arial', 28),
                        activebackground=bg_color)
    run_button.grid(column=0, row=2, sticky='ne', padx=10, pady=4)
    output_text.config(yscrollcommand=yscroll_bar.set)
    output_text.config(xscrollcommand=xscroll_bar.set)
    yscroll_bar.config(command=output_text.yview)
    xscroll_bar.config(command=output_text.xview)
    text_frame.grid(column=0, row=3)
    sec_window.mainloop()


first_page()


