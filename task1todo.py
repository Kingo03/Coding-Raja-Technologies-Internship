from tkinter import *
from tkinter import simpledialog

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('TO-DO-LIST')
        self.root.geometry('1200x1200')
        self.Label = Label(self.root, text='TO-DO-LIST-APPLICATION', 
                          font='ariel, 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.Label.pack(side='top', fill=BOTH)

        self.Label2 = Label(self.root, text='ADD TASKS', 
                         font='ariel, 15 bold', width=10, bd=5, bg='orange', fg='black')
        self.Label2.place(x=80, y=60)

        self.Label3 = Label(self.root, text='TASKS', 
                         font='ariel, 15 bold', width=30, bd=5, bg='orange', fg='black')
        self.Label3.place(x=450, y=60)

        self.main_text = Listbox(self.root, bd=5, width=50, font="ariel, 20 italic bold", selectmode=SINGLE)
        self.main_text.place(x=300, y=120)

        self.completed_tasks = set()

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=45, y=120)

        # =======================add task=====================#

        def add():
            content = self.text.get(1.0, END).strip()
            if content:
                # Get priority from user input
                priority = simpledialog.askstring("Priority", "Enter priority (High/Medium/Low):", parent=root)
                
                # Get due date from user input
                due_date = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):", parent=root)

                # Format task with priority and due date
                task_with_priority_and_date = f"{content} - Priority: {priority}, Due Date: {due_date}"
                
                # Insert into Listbox
                self.main_text.insert(END, task_with_priority_and_date)
                
                # Save to file
                with open('data.txt', 'a') as file:
                    file.write(f"{task_with_priority_and_date}\n")
                
                # Clear the input field
                self.text.delete(1.0, END)

        # ====================delete task=====================#

        def delete():
            selected_index = self.main_text.curselection()
            if selected_index:
                task = self.main_text.get(selected_index)
                self.main_text.delete(selected_index)

                # Update the data file
                with open('data.txt', 'r') as f:
                    lines = f.readlines()
                with open('data.txt', 'w') as f:
                    for line in lines:
                        if line.strip() != task:
                            f.write(line)

                # Remove from completed tasks if present
                self.completed_tasks.discard(task)

        # ===================mark as completed================#

        def mark_completed():
            selected_index = self.main_text.curselection()
            if selected_index:
                task = self.main_text.get(selected_index)
                # Check if the task is already marked as completed
                if task not in self.completed_tasks:
                    # Mark the task as completed
                    self.completed_tasks.add(task)
                    self.main_text.itemconfig(selected_index, {'fg': 'green'})

        # Populate Listbox with existing tasks from the data file
        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.strip()
                self.main_text.insert(END, ready)

        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic', 
                             width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=80, y=200)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic', 
                              width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=80, y=300)

        self.button3 = Button(self.root, text="Completed", font='sarif, 20 bold italic', 
                              width=10, bd=5, bg='orange', fg='black', command=mark_completed)
        self.button3.place(x=80, y=400)


def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
