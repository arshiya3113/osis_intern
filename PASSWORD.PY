from tkinter import *
from tkinter import messagebox
import string
import random


try:
    import pyperclip
    PYPERCLIP_AVAILABLE = True
except Exception:
    PYPERCLIP_AVAILABLE = False

def generator():
    passwordField.delete(0, END)
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    all_chars = small_alphabets + capital_alphabets + numbers + special_characters

    
    try:
        password_length = int(length_box.get())
        if password_length <= 0:
            raise ValueError
    except Exception:
        messagebox.showerror("Invalid length", "Enter a valid integer password length.")
        return

    
    if choice.get() == 1:   
        population = small_alphabets
    elif choice.get() == 2: 
        population = small_alphabets + capital_alphabets
    elif choice.get() == 3: 
        population = all_chars
    else:                   
        population = all_chars

    
    password = ''.join(random.choices(population, k=password_length))
    passwordField.insert(0, password)

def copy():
    random_password = passwordField.get()
    if not random_password:
        messagebox.showwarning("Nothing to copy", "Generate a password first.")
        return

    
    if PYPERCLIP_AVAILABLE:
        try:
            pyperclip.copy(random_password)
            messagebox.showinfo("Copied", "Password copied to clipboard (pyperclip).")
            return
        except Exception as e:
            
            print("pyperclip failed:", e)

    
    try:
        root.clipboard_clear()
        root.clipboard_append(random_password)
        root.update()  
        messagebox.showinfo("Copied", "Password copied to clipboard (tkinter fallback).")
    except Exception as e:
        messagebox.showerror("Clipboard Error", f"Could not copy to clipboard:\n{e}")


root = Tk()
root.config(bg='gray20')
root.title("Password Generator")
choice = IntVar()
Font = ('arial', 13, 'bold')

passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'),
                      bg='gray20', fg='white')
passwordLabel.grid(pady=5)

weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font, bg='gray20', fg='white')
weakradioButton.grid(pady=5)

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font, bg='gray20', fg='white')
mediumradioButton.grid(pady=5)

strongradioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font, bg='gray20', fg='white')
strongradioButton.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5)

length_box = Spinbox(root, from_=3, to_=64, width=5, font=Font)
length_box.grid()

generateButton = Button(root, text='Generate', font=Font, command=generator, bg='white', fg='black')
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid(pady=5)

copyButton = Button(root, text='Copy', font=Font, bg='white', fg='black', command=copy)
copyButton.grid(pady=10)

root.mainloop()
