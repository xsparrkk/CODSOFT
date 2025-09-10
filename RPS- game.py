# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 23:30:07 2025

@author: Mimansha Pandit


"""

import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors")
        master.geometry("400x400")
        master.config(bg="#F0F0F0")

        self.user_score = 0
        self.computer_score = 0
        self.choices = ['Rock', 'Paper', 'Scissors']

        self.show_welcome_screen()

    def show_welcome_screen(self):
        # Clear any existing widgets
        for widget in self.master.winfo_children():
            widget.destroy()

        self.welcome_frame = tk.Frame(self.master, bg="#F0F0F0")
        self.welcome_frame.pack(expand=True)

        self.title_label = tk.Label(self.welcome_frame, text="Rock-Paper-Scissors", font=("Helvetica", 20, "bold"), bg="#F0F0F0")
        self.title_label.pack(pady=20)

        self.rules_label = tk.Label(self.welcome_frame, text="Rules:\nRock beats Scissors\nScissors beats Paper\nPaper beats Rock", font=("Helvetica", 12), bg="#F0F0F0")
        self.rules_label.pack(pady=10)

        self.start_button = tk.Button(self.welcome_frame, text="Start Game", font=("Helvetica", 14, "bold"), command=self.show_game_screen, bg="#4CAF50", fg="white", relief=tk.RAISED)
        self.start_button.pack(pady=20)

    def show_game_screen(self):
        # Destroy the welcome screen frame
        self.welcome_frame.destroy()

        self.game_frame = tk.Frame(self.master, bg="#F0F0F0")
        self.game_frame.pack(expand=True)

        # Scoreboard
        self.score_label = tk.Label(self.game_frame, text=f"Score: You {self.user_score} | Computer {self.computer_score}", 
                                    font=("Helvetica", 14, "bold"), bg="#F0F0F0")
        self.score_label.pack(pady=10)

        # User's choice buttons
        self.choice_frame = tk.Frame(self.game_frame, bg="#F0F0F0")
        self.choice_frame.pack(pady=20)

        for choice in self.choices:
            tk.Button(self.choice_frame, text=choice, width=10, font=("Helvetica", 12),
                      command=lambda c=choice: self.play_round(c), bg="#2196F3", fg="white", relief=tk.RAISED).pack(side=tk.LEFT, padx=10)

        # Result display
        self.result_label = tk.Label(self.game_frame, text="", font=("Helvetica", 16, "bold"), bg="#F0F0F0")
        self.result_label.pack(pady=10)

        self.user_choice_label = tk.Label(self.game_frame, text="", font=("Helvetica", 12), bg="#F0F0F0")
        self.user_choice_label.pack()

        self.computer_choice_label = tk.Label(self.game_frame, text="", font=("Helvetica", 12), bg="#F0F0F0")
        self.computer_choice_label.pack()

        # Play Again / Quit Buttons
        self.play_again_frame = tk.Frame(self.game_frame, bg="#F0F0F0")
        self.play_again_frame.pack(pady=20)
        
        tk.Button(self.play_again_frame, text="Play Again", command=self.reset_round, bg="#FFC107", fg="black", relief=tk.RAISED).pack(side=tk.LEFT, padx=10)
        tk.Button(self.play_again_frame, text="Quit", command=self.master.destroy, bg="#F44336", fg="white", relief=tk.RAISED).pack(side=tk.LEFT, padx=10)

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)
        self.user_choice_label.config(text=f"Your choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

        result = ""
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper') or \
             (user_choice == 'Paper' and computer_choice == 'Rock'):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1
        
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score: You {self.user_score} | Computer {self.computer_score}")

    def reset_round(self):
        self.result_label.config(text="")
        self.user_choice_label.config(text="")
        self.computer_choice_label.config(text="")

# Main part of the script
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()
        
        
        


