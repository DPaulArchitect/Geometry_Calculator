import tkinter as tk

from tkinter import ttk

from tkinter.messagebox import showinfo

root = tk.Tk()
ttk.Label(root, text='GRADE CALCULATOR').pack()
root.title('Grade Calculator')
root.geometry('300x400+50+50')
root.resizable(False, False)
root.attributes('-topmost', 1)

text = tk.StringVar()
textbox = ttk.Entry(root, textvariable=text)

grade = ttk.Frame(root)
grade.pack(padx=10, pady=10, fill='x', expand=True)

grade_entry = ttk.Entry(grade, textvariable=grade)
grade_entry.focus()





root.mainloop()

flag = True
while flag:
    user_inp = input("Insert your score to get your grade: ")
    try:
        score = int(user_inp)
    except ValueError:
        print("A score must be a number from 0 to 100")
    else:
        if score < 0 or score > 100:
            print("The score inserted cannot be negative or above 100")
        else:
            flag = False
if score >= 90:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else:
    print('F')