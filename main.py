'''
This is the main file of the text adventure game.
'''
import tkinter as tk
from game import Game
def start_game():
    # Create a new instance of the Game class
    game = Game(window)
    # Start the game
    game.start()
# Create the main window
window = tk.Tk()
window.title("Bank Robbery Adventure")
# Create a start button
start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()
# Run the main event loop
window.mainloop()