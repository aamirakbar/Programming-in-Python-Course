import tkinter as tk
from pass_manager import PasswordManager

def handle_set_password():
    pass_for = entry_pass_for.get()
    password = entry_pass.get()
    
    if pm.set_password(pass_for, password):
        label_result.config(text="Password set succesfully")
    else:
        label_result.config(text="Setting password failed")
        
def handle_check_password():
    pass_for = entry_pass_for.get()
    password = entry_pass.get()
    
    if pm.check_password(pass_for, password):
        label_result.config(text=f"Password for {pass_for} is correct")
    else:
        label_result.config(text=f"Password for {pass_for} is wrong")

pm = PasswordManager()

window = tk.Tk()

window.title("My Secure Password Manager")
window.geometry("400x200")

label_pass_for = tk.Label(window, text="Password For:")
label_pass_for.pack()

entry_pass_for = tk.Entry(window)
entry_pass_for.pack()

label_pass = tk.Label(window, text="Password:")
label_pass.pack()

entry_pass = tk.Entry(window, show="*")
entry_pass.pack()

button_set_pass = tk.Button(window, text="Set Password", command=handle_set_password)
button_set_pass.pack()

button_check_pass = tk.Button(window, text="Check Password", command=handle_check_password)
button_check_pass.pack()

label_result = tk.Label(window, text="")
label_result.pack()


window.mainloop()