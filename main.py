import tkinter as tk
#anden slet klik virker ikke
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.entries = -1
        self.people = []

        self.names = []
        self.id = []
        self.tlf = []
        self.frames = []

        self.master = master
        self.pack()
        self.create_widgets()

    #Create the first two rows of the application
    def create_widgets(self):
        # Row 0: Input boxes
        self.inputName = tk.Entry(self, bd=4)
        self.inputName.grid(row=0, column=0)

        self.inputID = tk.Entry(self, bd=4)
        self.inputID.grid(row=0, column=1)

        self.inputTLF = tk.Entry(self, bd=4)
        self.inputTLF.grid(row=0, column=2)
        # Row 0: "Add" button
        self.addButton = tk.Button(self, text="Add", command=self.AddMember)
        self.addButton.grid(row=0, column=3)

        # Row 1: Labels
        tk.Label(self, text = "Navn", borderwidth = 4).grid(row=1, column=0)
        tk.Label(self, text="ID", borderwidth=4).grid(row=1, column=1)
        tk.Label(self, text="Tlf", borderwidth=4).grid(row=1, column=2, ipadx=30)
        tk.Label(self, text="   ", borderwidth=4).grid(row=1, column=3)

    # What the "add" button does
    def AddMember(self):
        self.people.append([self.inputName.get(), self.inputID.get(), self.inputTLF.get()]) #Add textbox-text to list
        self.entries += 1
        self.updateMembers()


    def updateMembers(self):  # Display new member
        # This is declared to make sure that self.entries is assigned by value, and not by index
        entry = self.entries
        # Add the new name from 'people' to the list of name entries, and display
        self.names.append(tk.Label(self, text=self.people[entry][0], borderwidth=4))
        self.names[entry].grid(row=entry + 2, column=0)
        # -//- but with ids
        self.id.append(tk.Label(self, text=self.people[entry][1], borderwidth=4))
        self.id[entry].grid(row=entry + 2, column=1)
        # -//- but with phone numbers
        self.tlf.append(tk.Label(self, text=self.people[entry][2], borderwidth=4))
        self.tlf[entry].grid(row=entry + 2, column=2)
        # Create a frame to but multiple buttons in one grid-cell
        self.frames.append(tk.Frame(self))
        self.frames[entry].grid(row=entry + 2, column=3)
        #Create such buttons
        removeButton = tk.Button(self.frames[entry], text="X", command=lambda: self.remove(entry))
        msgButton = tk.Button(self.frames[entry], text="SMS", command=lambda: self.sendSMS(entry))
        callButton = tk.Button(self.frames[entry], text="Ring", command=lambda: self.makeCall(entry))
        #Display such buttons
        removeButton.pack(side='top')
        callButton.pack(side = 'right')
        msgButton.pack(side='left')

    def sendSMS(self, sender_id):
        print("SMSMSMSM")

    def makeCall(self, sender_id):
        print("RINGRINGRING")

    def remove(self, sender_id):
        print("")
        print(self.entries)
        self.people.pop(sender_id)  # Remove from the "People" list



        if self.entries >= 0:
            # Un-display the lowest entry
            self.tlf[self.entries].destroy()
            self.frames[self.entries].destroy()
            self.id[self.entries].destroy()
            self.names[self.entries].destroy()
            
            for i in range(self.entries):  # RE-display all current entries (deleted one excluded)
                tk.Label(self, text=self.people[i][0], borderwidth=4).grid(row=i + 2, column=0)
                tk.Label(self, text=self.people[i][1], borderwidth=4).grid(row=i + 2, column=1)
                tk.Label(self, text=self.people[i][2], borderwidth=4).grid(row=i + 2, column=2)

             # Remove deleted user's info in the display lists.
            self.names.pop(sender_id)
            self.id.pop(sender_id)
            self.tlf.pop(sender_id)
            self.frames.pop(sender_id)

        self.entries -= 1  # Decrement size of people
        print(self.entries)


#Actually start the program
root = tk.Tk()
app = Application(master=root)
app.mainloop()

