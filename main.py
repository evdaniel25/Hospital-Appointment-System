# import tkinter
import tkinter
import sqlite3
with sqlite3.connect('details.db') as db:
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Appointment(id integer PRIMARY KEY AUTOINCREMENT, name text, age integer, gender text, doctor text);''')
# window defn
root = tkinter.Tk()
root.geometry('1920x1080')
root.title('Hospital Appointment System')
root.config(background='#f8c3e0')

# widget defn
label_heading = tkinter.Label(root,text='Register',font=('Pacifico',35,'bold'))
label_heading.config(fg='#ee2244',bg='#f8c3e0')
label_heading.place(x=100,y=100)

# run 
root.mainloop()

