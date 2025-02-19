import tkinter as tk
from tkinter import messagebox
import random

# Global variables for settings
font_size = 10
high_contrast_mode = False
sound_effects = True

# Global variables for scores
tic_tac_toe_wins = 0
tic_tac_toe_losses = 0
rock_paper_scissors_wins = 0
rock_paper_scissors_losses = 0
pong_high_score = 0

# Global variables for game states
current_player = "X"
board = [""] * 9
pong_difficulty = 1

# Function to clear the current page
def clear_page():
    for widget in root.winfo_children():
        widget.destroy()

# Function to go back to the home page
def go_home():
    clear_page()
    create_main_menu()

# Function to create the main menu
def create_main_menu():
    clear_page()
    title_label = tk.Label(root, text="Minigames App", font=("Arial", 24))
    title_label.pack(pady=20)

    tic_tac_toe_button = tk.Button(root, text="Tic Tac Toe", command=open_tic_tac_toe, font=("Arial", 18))
    tic_tac_toe_button.pack(pady=10)

    rock_paper_scissors_button = tk.Button(root, text="Rock Paper Scissors", command=open_rock_paper_scissors, font=("Arial", 18))
    rock_paper_scissors_button.pack(pady=10)

    pong_button = tk.Button(root, text="Pong", command=open_pong_player_select, font=("Arial", 18))
    pong_button.pack(pady=10)

    settings_button = tk.Button(root, text="Settings", command=open_settings, font=("Arial", 18))
    settings_button.pack(pady=10)

# Function to open the Tic Tac Toe game
def open_tic_tac_toe():
    clear_page()
    global current_player, board

    title_label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24))
    title_label.pack(pady=20)

    board_frame = tk.Frame(root)
    board_frame.pack()

    buttons = []
    for i in range(9):
        button = tk.Button(board_frame, text="", font=("Arial", 24), width=5, height=2, command=lambda i=i: make_move(i))
        button.grid(row=i // 3, column=i % 3)
        buttons.append(button)

    score_label = tk.Label(root, text=f"Wins: {tic_tac_toe_wins} Losses: {tic_tac_toe_losses}", font=("Arial", 18))
    score_label.pack(pady=20)

    back_button = tk.Button(root, text="Back to Home", command=go_home, font=("Arial", 18))
    back_button.pack(pady=10)

    def make_move(position):
        global current_player, board
        if board[position] == "":
            board[position] = current_player
            buttons[position].config(text=current_player)
            if check_winner():
                messagebox.showinfo("Game Over", f"{current_player} wins!")
                update_score(current_player)
                reset_board()
            elif "" not in board:
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_board()
            else:
                current_player = "O" if current_player == "X" else "X"
                if current_player == "O":
                    computer_move()

    def check_winner():
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
                return True
        return False

    def computer_move():
        available_moves = [i for i, spot in enumerate(board) if spot == ""]
        if available_moves:
            move = random.choice(available_moves)
            board[move] = "O"
            buttons[move].config(text="O")
            if check_winner():
                messagebox.showinfo("Game Over", "Computer wins!")
                update_score("O")
                reset_board()
            elif "" not in board:
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_board()
            else:
                current_player = "X"

    def update_score(winner):
        global tic_tac_toe_wins, tic_tac_toe_losses
        if winner == "X":
            tic_tac_toe_wins += 1
        elif winner == "O":
            tic_tac_toe_losses += 1
        score_label.config(text=f"Wins: {tic_tac_toe_wins} Losses: {tic_tac_toe_losses}")

    def reset_board():
        global board, current_player
        board = [""] * 9
        current_player = "X"
        for button in buttons:
            button.config(text="")

# Function to open the Rock Paper Scissors game
def open_rock_paper_scissors():
    clear_page()
    global rock_paper_scissors_wins, rock_paper_scissors_losses

    title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24))
    title_label.pack(pady=20)

    def play_game(player_choice):
        global rock_paper_scissors_wins, rock_paper_scissors_losses
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        result_label.config(text=f"Computer plays: {computer_choice}")

        if player_choice == computer_choice:
            result = "It's a draw!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            rock_paper_scissors_wins += 1
        else:
            result = "You lose!"
            rock_paper_scissors_losses += 1

        result_label.config(text=f"Computer plays: {computer_choice}\n{result}")
        score_label.config(text=f"Wins: {rock_paper_scissors_wins} Losses: {rock_paper_scissors_losses}")

    rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"), font=("Arial", 18))
    rock_button.pack(pady=10)

    paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"), font=("Arial", 18))
    paper_button.pack(pady=10)

    scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"), font=("Arial", 18))
    scissors_button.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 18))
    result_label.pack(pady=20)

    score_label = tk.Label(root, text=f"Wins: {rock_paper_scissors_wins} Losses: {rock_paper_scissors_losses}", font=("Arial", 18))
    score_label.pack(pady=20)

    back_button = tk.Button(root, text="Back to Home", command=go_home, font=("Arial", 18))
    back_button.pack(pady=10)

# Function to open the Pong player select page
def open_pong_player_select():
    clear_page()
    title_label = tk.Label(root, text="Pong", font=("Arial", 24))
    title_label.pack(pady=20)

    player_select_label = tk.Label(root, text="How many players will be playing?", font=("Arial", 18))
    player_select_label.pack(pady=20)

    one_player_button = tk.Button(root, text="1 Player", command=lambda: open_pong_game(1), font=("Arial", 18))
    one_player_button.pack(pady=10)

    two_player_button = tk.Button(root, text="2 Players", command=lambda: open_pong_game(2), font=("Arial", 18))
    two_player_button.pack(pady=10)

    back_button = tk.Button(root, text="Back to Home", command=go_home, font=("Arial", 18))
    back_button.pack(pady=10)

# Function to open the Pong game
def open_pong_game(players):
    clear_page()
    global pong_high_score, pong_difficulty

    title_label = tk.Label(root, text="Pong", font=("Arial", 24))
    title_label.pack(pady=20)

    canvas = tk.Canvas(root, width=600, height=400, bg="black")
    canvas.pack()

    paddle_1 = canvas.create_rectangle(50, 150, 60, 250, fill="white")
    paddle_2 = canvas.create_rectangle(540, 150, 550, 250, fill="white")
    ball = canvas.create_oval(295, 195, 305, 205, fill="white")

    score_1 = 0
    score_2 = 0

    score_label = tk.Label(root, text=f"Player 1: {score_1}  Player 2: {score_2}", font=("Arial", 18))
    score_label.pack(pady=20)

    def update_scores():
        score_label.config(text=f"Player 1: {score_1}  Player 2: {score_2}")

    def move_paddle_1(event):
        if event.keysym == "w":
            canvas.move(paddle_1, 0, -20)
        elif event.keysym == "s":
            canvas.move(paddle_1, 0, 20)

    def move_paddle_2(event):
        if event.keysym == "Up":
            canvas.move(paddle_2, 0, -20)
        elif event.keysym == "Down":
            canvas.move(paddle_2, 0, 20)

    root.bind("<KeyPress>", move_paddle_1)
    if players == 2:
        root.bind("<KeyPress>", move_paddle_2)

    back_button = tk.Button(root, text="Back to Home", command=go_home, font=("Arial", 18))
    back_button.pack(pady=10)

# Function to open the settings page
def open_settings():
    clear_page()
    title_label = tk.Label(root, text="Settings", font=("Arial", 24))
    title_label.pack(pady=20)

    font_size_label = tk.Label(root, text="Font Size:", font=("Arial", 18))
    font_size_label.pack(pady=10)

    font_size_entry = tk.Entry(root, font=("Arial", 18))
    font_size_entry.insert(0, str(font_size))
    font_size_entry.pack(pady=10)

    def update_font_size():
        global font_size
        try:
            font_size = int(font_size_entry.get())
            messagebox.showinfo("Success", "Font size updated!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    font_size_button = tk.Button(root, text="Update Font Size", command=update_font_size, font=("Arial", 18))
    font_size_button.pack(pady=10)

    high_contrast_label = tk.Label(root, text="High Contrast Mode:", font=("Arial", 18))
    high_contrast_label.pack(pady=10)

    def toggle_high_contrast():
        global high_contrast_mode
        high_contrast_mode = not high_contrast_mode
        messagebox.showinfo("Success", f"High contrast mode {'enabled' if high_contrast_mode else 'disabled'}.")

    high_contrast_button = tk.Button(root, text="Toggle High Contrast", command=toggle_high_contrast, font=("Arial", 18))
    high_contrast_button.pack(pady=10)

    sound_effects_label = tk.Label(root, text="Sound Effects:", font=("Arial", 18))
    sound_effects_label.pack(pady=10)

    def toggle_sound_effects():
        global sound_effects
        sound_effects = not sound_effects
        messagebox.showinfo("Success", f"Sound effects {'enabled' if sound_effects else 'disabled'}.")

    sound_effects_button = tk.Button(root, text="Toggle Sound Effects", command=toggle_sound_effects, font=("Arial", 18))
    sound_effects_button.pack(pady=10)

    back_button = tk.Button(root, text="Back to Home", command=go_home, font=("Arial", 18))
    back_button.pack(pady=10)

# Main application window
root = tk.Tk()
root.title("Minigames App")
root.geometry("800x600")

# Start the application with the main menu
create_main_menu()

# Run the application
root.mainloop()
