import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

root = tk.Tk()
root.title("Task Tracker")

task_list = tk.Listbox(root)
task_list.pack()

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Add Task", command = add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command = remove_task)
remove_button.pack()

root.mainloop()