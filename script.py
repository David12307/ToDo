from typing import Optional, Tuple, Union
from customtkinter import *
from CTkListbox import *
from tkinter import messagebox, filedialog
from tkinter.filedialog import asksaveasfile

class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def addTask(*args):
            # Clear the input and check if it is empty, if yes, throw an error
            task = my_entry.get().strip()
            if task == "":
                messagebox.showerror(title="Error", message="The task cannot be empty.")
            else:
                listbox.insert("END", task)
                my_entry.delete(0, END)

        def deleteTask():
            # Try to see if there is an error when deleting a task,
            # if it is that means the user didn't select a task to delete
            try:
                listbox.delete(listbox.curselection())
            except:
                messagebox.showerror(title="Error", message="Select what task you want to delete.")

        def readFile():
            listbox.delete("all")
            filepath = filedialog.askopenfilename(title="Open a Text File", filetypes=(("text    files","*.txt"), ("all files","*.*")))
            file = open(filepath, 'r')
            
            for task in file:
                if task.strip() != "":
                    listbox.insert(END, task.strip())

            file.close()

        def writeFile():
            files = [('Text Document', "*.txt")]
            file = asksaveasfile(filetypes = files, defaultextension = files)
            
            if file is None:
                return

            todos = listbox.get("all")
            try:
                file.write("\n".join(todos))
            except Exception as e:
                print(f"Error writing to file: {e}")
            finally:
                file.close()



        main_frame = CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.grid(row = 0, column=0, padx=10, pady=10)

        my_entry = CTkEntry(master=main_frame)
        my_entry.grid(row=1, column=2, pady=(0, 10), padx=10)
        my_entry.bind("<Return>", addTask) # If the 'return' key is pressed the addTask() will execute

        addBtn = CTkButton(master=main_frame, text="Add", command=addTask)
        addBtn.place(x=255, y=150)

        delBtn = CTkButton(master=main_frame, text="Delete", command=deleteTask, fg_color="#d11a2a")
        delBtn.place(x=255, y=200)

        # Create / read files
        openBtn = CTkButton(master=main_frame, text="Open a file", command=readFile)
        openBtn.place(x=255, y=50)

        writeBtn = CTkButton(master=main_frame, text="Write a file", command=writeFile)
        writeBtn.place(x=255, y=10)

        listbox = CTkListbox(main_frame, 100, 200)
        listbox.grid(row=1, column=1, pady=10, padx=10)

# Run the app
app = App()
app.mainloop()