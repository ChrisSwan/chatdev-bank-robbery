'''
This file contains the Game class which represents the text adventure game.
'''
import tkinter as tk
class Game:
    def __init__(self, window):
        # Initialize game variables
        self.player_name = ""
        self.bank_vault_code = ""
        self.window = window
        self.create_widgets()
    def create_widgets(self):
        # Create a label for player name input
        name_label = tk.Label(self.window, text="Enter your name:")
        name_label.pack()
        # Create an entry field for player name input
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()
        # Create a button to start the game
        start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        start_button.pack()
        # Create a text area for displaying game messages
        self.message_text = tk.Text(self.window, height=10, width=50)
        self.message_text.pack()
        # Create a label for action input
        action_label = tk.Label(self.window, text="Enter your action:")
        action_label.pack()
        # Create an entry field for action input
        self.action_entry = tk.Entry(self.window)
        self.action_entry.pack()
        # Create a button to submit the action
        submit_button = tk.Button(self.window, text="Submit", command=self.submit_action)
        submit_button.pack()
    def start_game(self):
        # Get player name from the entry field
        self.player_name = self.name_entry.get()
        # Clear the entry field
        self.name_entry.delete(0, tk.END)
        # Display game introduction in the message text
        self.message_text.insert(tk.END, f"Welcome, {self.player_name}! You are about to embark on a bank robbery adventure.\n")
        self.message_text.insert(tk.END, "Your mission is to successfully rob the bank vault and escape without getting caught.\n")
        # Get bank vault code from the entry field
        self.bank_vault_code = self.action_entry.get()
        # Clear the entry field
        self.action_entry.delete(0, tk.END)
        # Start the bank robbery
        self.rob_bank()
    def submit_action(self):
        # Get action from the entry field
        action = self.action_entry.get()
        # Clear the entry field
        self.action_entry.delete(0, tk.END)
        # Perform the action and display the result in the message text
        result = self.perform_action(action)
        self.message_text.insert(tk.END, result + "\n")
        # Scroll to the bottom of the message text
        self.message_text.see(tk.END)
    def rob_bank(self):
        # Perform bank robbery actions
        self.message_text.insert(tk.END, "You are inside the bank. What would you like to do?\n")
    def perform_action(self, action):
        if action == "look around":
            return "You see a security guard, a locked door, and a safe."
        elif action == "open door":
            return "The door is locked. You need to find a key."
        elif action == "check safe":
            return "The safe requires a 4-digit code. You need to find the code."
        elif action == "quit":
            self.end_game()
            return "Game over. Thank you for playing!"
        else:
            return "Invalid action. Please try again."
    def end_game(self):
        # Destroy the window to exit the game
        self.window.destroy()