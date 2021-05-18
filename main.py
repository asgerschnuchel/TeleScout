from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import dbmanager
import ATlibrary


root = Tk()
root.title('TeleScout')
#root.iconbitmap('path_to_bmp')
root.geometry("525x800")

query_label = Label(root, text="")
query_label.grid(row=14, column=0, columnspan=2)


def update():
	record_id = delete_box.get()
	dbmanager.edit_patrol(f_name_editor.get(), l_name_editor.get(), address_editor.get(), city_editor.get(), record_id)
	editor.destroy()
	root.deiconify()

# Create Edit function to update a record
def edit():
	root.withdraw()
	global editor
	editor = Tk()
	editor.title('Opdater patruljeinformation')
	#editor.iconbitmap('')
	editor.geometry("400x300")
	# Create a database or connect to one
	conn = sqlite3.connect('test.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()
	# Query the database
	#c.execute("SELECT * FROM patrols WHERE id = " + record_id)
	#records = c.fetchall()
	records = dbmanager.get_patrol(record_id)
	
	#Create Global Variables for text box names
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor

	# Create Text Boxes
	f_name_editor = Entry(editor, width=30)
	f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
	l_name_editor = Entry(editor, width=30)
	l_name_editor.grid(row=1, column=1)
	address_editor = Entry(editor, width=30)
	address_editor.grid(row=2, column=1)
	city_editor = Entry(editor, width=30)
	city_editor.grid(row=3, column=1)
	
	# Create Text Box Labels
	f_name_label = Label(editor, text="Patruljenavn")
	f_name_label.grid(row=0, column=0, pady=(10, 0))
	l_name_label = Label(editor, text="Ledernavn")
	l_name_label.grid(row=1, column=0)
	address_label = Label(editor, text="Telefonnummer")
	address_label.grid(row=2, column=0)
	city_label = Label(editor, text="Telefon-ID")
	city_label.grid(row=3, column=0)

	#Loop thru results
	for record in records:
		f_name_editor.insert(0, record[1])
		l_name_editor.insert(0, record[2])
		address_editor.insert(0, record[3])
		city_editor.insert(0, record[4])

	
	# Create a Save Button To Save edited record
	edit_btn = Button(editor, text="Gen ændringer", command=update)
	edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

	


# Create Function to Delete A Record
def delete():
	dbmanager.delete_patrol(delete_box.get())
	delete_box.delete(0, END)
	query()


# Create Submit Function For database
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('test.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO patrols VALUES (:id, :patrolname, :leadername, :phone, :phoneid)",
			{
				'id': id.get(),
				'patrolname': patrolname.get(),
				'leadername': leadername.get(),
				'phone': phone.get(),
				'phoneid': phoneid.get(),
			})


	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()
	# Clear The Text Boxes
	id.delete(0, END)
	patrolname.delete(0, END)
	leadername.delete(0, END)
	phone.delete(0, END)
	phoneid.delete(0, END)
	query()

# Create Query Function
def query():
	
	#gets patrols from database
	records = dbmanager.get_patrols()
	# Loop Thru Results
	entries = []
	print_records = ''
	x = 20

	for record in records:
		
		#Generate boxes and insert values
		id = Entry(root, width=5)
		id.grid(row=x, column=0, sticky=W)
		id.insert(0, str(record[0]))
		patrolname = Entry(root, width=20)
		patrolname.grid(row=x, column=0, ipadx=45, sticky=E)
		patrolname.insert(0, str(record[1]))
		leadername = Entry(root, width=20)
		leadername.grid(row=x, column=1, ipadx=30, columnspan=1, sticky=NSEW)
		leadername.insert(0, str(record[2]))
		phone = Entry(root, width=10)
		phone.grid(row=x, column=1, columnspan=1, sticky=E)
		phone.insert(0, str(record[3]))
		phoneid = Entry(root, width=5)
		phoneid.grid(row=x, column=2, sticky=N)
		phoneid.insert(0, str(record[4]))
		print (x)
		x = x+1
		clear()
		print_records += str(record[0]) + " "+ "\t"  + str(record[1]) + " " + "\t" + str(record[2]) + " " + "\t" + str(record[3])+  " " + "\n"

	
	#print(print_records)
	#query_label.configure(text=print_records)

def clear():
	id.delete(0, END)
	patrolname.delete(0, END)
	leadername.delete(0, END)
	phone.delete(0, END)
	phoneid.delete(0, END)

def sendsms():
    root.withdraw()
    global editor
    editor = Tk()
    editor.title('Send SMS')
    #editor.iconbitmap('placeholder')
    editor.geometry("400x300")
    # Create a database or connect to one
    conn = sqlite3.connect('test.db')
    # Create cursor
    c = conn.cursor()
    global record_id
    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM patrols WHERE id = " + record_id)
    records = c.fetchall()

    #Create Global Variables for text box names
    global message_send

    # Create Text Boxes 
    message_send = Entry(editor, width=30)
    message_send.grid(row=0, column=1, padx=20, pady=(10, 0))

    # Create Text Box Labels
    message_send_label = Label(editor, text="Besked")
    message_send.grid(row=0, column=0, pady=(10, 0))


    # Create a Save Button To Save edited record
    edit_btn = Button(editor, text="Send besked", command=send)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

	# Create a Save Button To Save edited record
    sendall_btn = Button(editor, text="Send til alle", command=sendtoall)
    sendall_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

def send():
	record_id = delete_box.get()
	number = str(dbmanager.get_number(record_id))
	ATlibrary.sendmessage(number, message_send.get())
	editor.destroy()
	root.deiconify()

def sendtoall():
	records = dbmanager.get_patrols()
	message = message_send.get()
	for record in records:
		print(str(record[3]))
		ATlibrary.sendmessage(str(record[3]), message)
	editor.destroy()
	root.deiconify()


# Create Text Boxes
id = Entry(root, width=30)
id.grid(row=0, column=1, padx=20, pady=(10, 0))
patrolname = Entry(root, width=30)
patrolname.grid(row=1, column=1)
leadername = Entry(root, width=30)
leadername.grid(row=2, column=1)
phone = Entry(root, width=30)
phone.grid(row=3, column=1)
phoneid = Entry(root, width=30)
phoneid.grid(row=4, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


# Create Text Box Labels
f_name_label = Label(root, text="Patrulje ID")
f_name_label.grid(row=0, column=0, pady=(10, 0))
patrolname_label = Label(root, text="Patruljenavn")
patrolname_label.grid(row=1, column=0)
leadername_label = Label(root, text="Anfører-navn")
leadername_label.grid(row=2, column=0)
phone_label = Label(root, text="Telefonnummer")
phone_label.grid(row=3, column=0)
phoneid_label = Label(root, text="Telefon-ID")
phoneid_label.grid(row=4, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Tilføj Patrulje", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Vis patruljer", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=75, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Slet patrulje", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Rediger patrulje", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

# Create an *SMS button
edit_btn = Button(root, text="Send besked", command=sendsms)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
query()



root.mainloop()