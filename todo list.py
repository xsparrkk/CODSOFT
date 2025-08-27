import tkinter as tk
from tkinter import messagebox

# --- Theming Colors ---
COLOR_BACKGROUND = "#f0f0f0"  # Light Gray
COLOR_PRIMARY = "#5b9bd5"     # Blue
COLOR_ACCENT = "#e06c75"      # Coral Red
COLOR_TEXT = "#333333"        # Dark Gray

def create_gui():
    """Sets up the GUI window and widgets."""
    
    # Initialize the main window
    root = tk.Tk()
    root.title("My To-Do List")
    root.geometry("450x550")
    root.configure(bg=COLOR_BACKGROUND)

    # --- Task Management Logic ---
    tasks = []

    def update_listbox():
        listbox_tasks.delete(0, tk.END)
        for i, task in enumerate(tasks, start=1):
            display_text = f"{i}. {task}"
            listbox_tasks.insert(tk.END, display_text)
            # Add a separator line after each item (optional but good for visual separation)
            if i < len(tasks):
                listbox_tasks.insert(tk.END, "-------------------------------------------------------------------------------------------------------------------------------------------------")
                listbox_tasks.itemconfig(tk.END, fg="#cccccc", bg=COLOR_BACKGROUND)

    def add_task():
        task = entry_task.get()
        if task:
            tasks.append(task)
            update_listbox()
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task():
        try:
            # Get the index of the selected item in the listbox
            selected_index = listbox_tasks.curselection()[0]
            # Account for the separator lines. The actual task index is half of the listbox index.
            task_index = selected_index // 2
            tasks.pop(task_index)
            update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_complete():
        try:
            selected_index = listbox_tasks.curselection()[0]
            task_index = selected_index // 2
            task = tasks[task_index]
            if not task.startswith("✔ "):
                tasks[task_index] = "✔ " + task
                update_listbox()
            else:
                messagebox.showinfo("Info", "This task is already marked as complete.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as complete.")
    
    # --- UI Layout and Widgets ---

    # Main Frame
    main_frame = tk.Frame(root, bg=COLOR_BACKGROUND, padx=20, pady=20)
    main_frame.pack(expand=True, fill="both")

    # Title Label
    label_title = tk.Label(main_frame, text="My To-Do List", font=("Helvetica", 28, "bold"), fg=COLOR_PRIMARY, bg=COLOR_BACKGROUND)
    label_title.pack(pady=(0, 20))

    # Frame for the listbox
    list_frame = tk.Frame(main_frame, bg="white", relief="solid", bd=1)
    list_frame.pack(pady=10, fill="both", expand=True)

    # Listbox to display tasks
    listbox_tasks = tk.Listbox(
        list_frame,
        bg="white", 
        fg=COLOR_TEXT, 
        font=("Helvetica", 14),
        selectbackground=COLOR_ACCENT, 
        selectforeground="white",
        borderwidth=0,
        highlightthickness=0,
        activestyle="none" # Prevents an extra border on selection
    )
    listbox_tasks.pack(side=tk.LEFT, fill="both", expand=True)

    # Scrollbar
    scrollbar_tasks = tk.Scrollbar(list_frame)
    scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    # Entry widget for new tasks
    entry_task = tk.Entry(
        main_frame, 
        bg="white", 
        fg=COLOR_TEXT, 
        font=("Helvetica", 14),
        insertbackground=COLOR_PRIMARY,
        relief="solid", bd=1
    )
    entry_task.pack(pady=10, fill="x")

    # Buttons Frame
    button_frame = tk.Frame(main_frame, bg=COLOR_BACKGROUND)
    button_frame.pack(pady=10)

    # Button Styling
    button_style = {
        "bg": COLOR_PRIMARY, 
        "fg": "white", 
        "font": ("Helvetica", 12, "bold"), 
        "relief": "flat",
        "padx": 15,
        "pady": 8
    }

    # Add Task Button
    button_add = tk.Button(button_frame, text="Add Task", command=add_task, **button_style)
    button_add.pack(side=tk.LEFT, padx=5)

    # Delete Task Button
    button_delete = tk.Button(button_frame, text="Delete", command=delete_task, **button_style)
    button_delete.pack(side=tk.LEFT, padx=5)

    # Mark Complete Button
    button_mark_complete = tk.Button(button_frame, text="Complete", command=mark_complete, **button_style)
    button_mark_complete.pack(side=tk.LEFT, padx=5)

    # Run the application
    root.mainloop()

# Run the GUI
create_gui()