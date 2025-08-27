import tkinter as tk
from tkinter import messagebox
import random
import string

# --- Password Generation Logic ---
def generate_password(length, complexity=True):
    """
    Generates a random password of a specified length.
    'complexity' parameter is for future expansion, e.g., to control character sets.
    """
    if length <= 0:
        return ""

    if complexity:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits # Less complex

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- GUI Application Class ---
class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("400x300")
        master.resizable(False, False)
        master.configure(bg="#2E3A4B") # A deep blue-grey for a modern look

        # A flag to track if a password has been generated
        self.password_generated = False

        # Main frame with a slight padding
        self.main_frame = tk.Frame(master, padx=20, pady=20, bg="#2E3A4B")
        self.main_frame.pack(expand=True)

        # Title Label
        self.title_label = tk.Label(self.main_frame, text="Secure Password Generator", 
                                    font=("Helvetica", 16, "bold"), fg="#FFD700", bg="#2E3A4B") # Gold for a pop of color
        self.title_label.pack(pady=10)

        # Length Input
        self.length_label = tk.Label(self.main_frame, text="Enter Password Length:", font=("Helvetica", 10), 
                                     fg="#E0E0E0", bg="#2E3A4B") # Light gray
        self.length_label.pack()
        self.length_entry = tk.Entry(self.main_frame, width=20, font=("Helvetica", 12), 
                                     bg="#4A5668", fg="#FFFFFF", insertbackground="#FFFFFF") # Darker entry background
        self.length_entry.pack(pady=5)
        self.length_entry.insert(0, "12")

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.main_frame, bg="#2E3A4B")
        self.buttons_frame.pack(pady=15)

        # Generate Button
        self.generate_button = tk.Button(self.buttons_frame, text="Generate", 
                                         command=self.generate_and_display, 
                                         font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", relief=tk.RAISED) # Green for action
        self.generate_button.pack(side=tk.LEFT, padx=5)

        # Regenerate Button (created but not packed initially)
        self.regenerate_button = tk.Button(self.buttons_frame, text="Regenerate", 
                                           command=self.regenerate_password, 
                                           font=("Helvetica", 12, "bold"), bg="#FF5722", fg="white", relief=tk.RAISED) # Orange-red for another action
        
        # Password Display
        self.password_display = tk.Text(self.main_frame, height=2, width=30, wrap=tk.WORD, 
                                        font=("Courier", 12), bg="#4A5668", fg="#FFFFFF", state=tk.DISABLED, relief=tk.FLAT)
        self.password_display.pack(pady=10)

    def generate_and_display(self):
        """Generates a new password based on current length."""
        try:
            length = int(self.length_entry.get())
            if length < 1:
                messagebox.showerror("Invalid Input", "Password length must be at least 1.")
                return
            password = generate_password(length)
            self._update_password_display(password)
            
            # Show the regenerate button only after the first successful generation
            if not self.password_generated:
                self.regenerate_button.pack(side=tk.LEFT, padx=5)
                self.password_generated = True

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def regenerate_password(self):
        """Regenerates the password using the current length."""
        try:
            length = int(self.length_entry.get())
            if length < 1:
                return # Do nothing if length is invalid
            password = generate_password(length)
            self._update_password_display(password)
        except ValueError:
            return # Do nothing if input is invalid

    def _update_password_display(self, password):
        """Helper method to update the text widget."""
        self.password_display.config(state=tk.NORMAL)
        self.password_display.delete("1.0", tk.END)
        self.password_display.insert(tk.END, password)
        self.password_display.config(state=tk.DISABLED)

# --- Main Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()