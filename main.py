# import tkinter
import tkinter
import customtkinter
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

label_name = tkinter.Label(root,text='Name',font=('Pacifico',18))
label_name.config(fg='#ee2244',bg='#f8c3e0')
label_name.place(x=105,y=200)

name_entry = tkinter.Entry(root)
name_entry.place(x=210,y=207)


label_age = tkinter.Label(root,text='Age',font=('Pacifico',18))
label_age.config(fg='#ee2244',bg='#f8c3e0')
label_age.place(x=105,y=250)

age_entry = tkinter.Entry(root)
age_entry.place(x=210,y=257)

label_gender = tkinter.Label(root,text='Gender',font=('Pacifico',18))
label_gender.config(fg='#ee2244',bg='#f8c3e0')
label_gender.place(x=105,y=300)

gender = ["Male", "Female","Other"]
gender_entry= customtkinter.CTkComboBox(root,values=gender)
gender_entry.place(x=210, y=305)

label_doctor = tkinter.Label(root,text='Doctor',font=('Pacifico',18))
label_doctor.config(fg='#ee2244',bg='#f8c3e0')
label_doctor.place(x=105,y=350)

doctor = ['Dr.Leena','Dr.Athira','Dr. Sayanora','Dr.Dejena','Dr.Chaithanya']
doctor_entry= customtkinter.CTkComboBox(root,values=doctor)
doctor_entry.place(x=210, y=350)

submit_button= customtkinter.CTkButton(root, text = 'Submit')
submit_button.place(x= 210, y=400)


# run 
root.mainloop()

