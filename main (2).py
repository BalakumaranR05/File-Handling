import json
from tkinter import *
from pop_up import Pop_up

welcome_screen = Tk()
welcome_screen.title("USER REGISTRATION")
welcome_screen.config(padx=100, pady=100)


def checks_user_pass(user, password):
    if user[len(user) - 10:] == "@gmail.com" and 5 < len(password) < 16 and not user[0].isdigit():
        count_spec = 0
        count_num = 0
        count_lower = 0
        count_upper = 0
        for i in password:
            if i in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                count_spec += 1
            if i.isdigit():
                count_num += 1
            if i.isupper():
                count_upper += 1
            if i.islower():
                count_lower += 1
        if count_spec >= 1 and count_upper >= 1 and count_lower >= 1 and count_num >= 1:
            return True
        else:
            return False


def login():
    login_page = Toplevel(login_button)
    login_page.title("Login page")
    login_page.config(padx=60, pady=60)
    user_name_label = Label(login_page, text="Username:", font=("Arial", 12, "bold"))
    user_name_label.grid(column=0, row=0)

    password_label = Label(login_page, text="Password:", font=("Arial", 12, "bold"))
    password_label.grid(column=0, row=1)

    user_entry = Entry(login_page)
    user_entry.grid(column=1, row=0)

    password_entry = Entry(login_page)
    password_entry.grid(column=1, row=1)

    def read_data():
        global username_list_global
        with open("data.txt", "r") as file:
            data_dic = file.readlines()

        data_dic = [json.loads(i.replace("'", '"')) for i in data_dic]

        update_user()

        if user_entry.get() not in username_list_global:
            pop_up_box1 = Pop_up("Username doesn't exist! Try registering", login_page)
        elif {user_entry.get(): password_entry.get()} in data_dic:
            pop_up_box2 = Pop_up("Logged In successfully", login_page)
        else:
            pop_up_box3 = Pop_up("Password incorrect! Try forgot password", login_page)

    def forgot_password():
        global username_list_global

        forgot_pass = Toplevel(forgot_password_button)
        forgot_pass.config(padx=60, pady=60)

        username_label = Label(forgot_pass, text="Username:", font=("Arial", 12, "bold"))
        username_label.grid(column=0, row=0)

        username_forgot = Entry(forgot_pass)
        username_forgot.grid(column=1, row=0)

        def show_password():
            if username_forgot.get() not in username_list_global:
                pop_up_box4 = Pop_up("Username doesnt exist! Try registering", login_page)
            else:
                with open("data.txt", "r") as file:
                    dic_data = file.readlines()

                dic_data = [json.loads(i.replace("'", '"')) for i in dic_data]

                for dict in dic_data:
                    for i, j in dict.items():
                        if i == username_forgot.get():
                            pop_up_box5 = Pop_up(f"Your password is {j}", login_page)

        ok_button = Button(forgot_pass, text="Ok", font=("Arial", 12, "bold"), command=show_password)
        ok_button.grid(column=1, row=1)

    ok_button = Button(login_page, text="OK", command=read_data)
    ok_button.grid(column=2, row=2)

    forgot_password_button = Button(login_page, text="forgot password", command=forgot_password)
    forgot_password_button.grid(column=1, row=2)


def register():
    register_page = Toplevel(register_button)
    register_page.title("Registration")
    register_page.config(padx=60, pady=60)

    user_name_label = Label(register_page, text="Enter a username:", font=("Arial", 12, "bold"))
    user_name_label.grid(column=0, row=0)

    password_label = Label(register_page, text="Enter a password:", font=("Arial", 12, "bold"))
    password_label.grid(column=0, row=1)

    user_entry = Entry(register_page)
    user_entry.grid(column=1, row=0)

    password_entry = Entry(register_page)
    password_entry.grid(column=1, row=1)

    def store_data():
        global username_list_global

        data_dic_write = {user_entry.get(): password_entry.get()}

        if checks_user_pass(user_entry.get(), password_entry.get()):
            if user_entry.get() not in username_list_global:
                with open("data.txt", mode='a') as data:
                    data.write(f"{data_dic_write}\n")
                    pop_up_box6 = Pop_up("User created successfully", register_page)
            else:
                pop_up_box7 = Pop_up("User already exists! Try different username", register_page)
        else:
            pop_up_box8 = Pop_up("Invalid user and password, must have at least one digit,uppercase, lowercase and "
                                 "special character", register_page)

    ok_button = Button(register_page, text="OK", command=store_data)
    ok_button.grid(column=1, row=2)


username_list_global = []


def update_user():
    with open("data.txt", mode='r') as data:
        data_dic = data.readlines()

    data_dic = [json.loads(i.replace("'", '"')) for i in data_dic]

    for dic in data_dic:
        for user in dic:
            if user not in username_list_global:
                username_list_global.append(user)


update_user()

login_button = Button(text="Login", font=("Arial", 12, "bold"), command=login)
login_button.grid(column=1, row=0)

register_button = Button(text="Register", font=("Arial", 12, "bold"), command=register)
register_button.grid(column=1, row=2)

welcome_screen.mainloop()
