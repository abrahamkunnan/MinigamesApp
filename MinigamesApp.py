import tkinter as tk
import random

# Global variables to track scores
tic_tac_toe_score = {'Player': 0, 'Computer': 0}
rps_score = {'Player': 0, 'Computer': 0}
pong_score = {'Player1': 0, 'Player2': 0}
settings = {'sound': True, 'font_size': 12, 'high_contrast': False}

# Helper function to clear the window
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

# Main menu
def main_menu(window):
    clear_window(window)
    window.title("Minigames App")

    title_label = tk.Label(window, text="Minigames App", font=("Helvetica", 24))
    title_label.pack(pady=20)

    tic_tac_toe_btn = tk.Button(window, text="Tic Tac Toe", command=lambda: tic_tac_toe_game(window), width=20)
    pong_btn = tk.Button(window, text="Pong", command=lambda: pong_game(window), width=20)
    rps_btn = tk.Button(window, text="Rock Paper Scissors", command=lambda: rps_game(window), width=20)
    settings_btn = tk.Button(window, text="Settings", command=lambda: settings_page(window), width=20)

    tic_tac_toe_btn.pack(pady=5)
    pong_btn.pack(pady=5)
    rps_btn.pack(pady=5)
    settings_btn.pack(pady=5)

# Tic Tac Toe Game
def tic_tac_toe_game(window):
    clear_window(window)
    
    board = ["" for _ in range(9)]
    current_player = ["X"]

    def make_move(button, index):
        if board[index] == "":
            board[index] = current_player[0]
            button.config(text=current_player[0])
            if check_winner():
                result_label.config(text=f"Player {current_player[0]} wins!")
            elif "" not in board:
                result_label.config(text="It's a draw!")
            else:
                current_player[0] = "O" if current_player[0] == "X" else "X"

    def check_winner():
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in winning_combinations:
            if board[a] == board[b] == board[c] != "":
                return True
        return False

    buttons = []
    for i in range(9):
        button = tk.Button(window, text="", font=("Helvetica", 20), width=5, height=2,
                            command=lambda i=i: make_move(buttons[i], i))
        buttons.append(button)
        button.grid(row=i // 3, column=i % 3)

    result_label = tk.Label(window, text="")
    result_label.grid(row=3, column=0, columnspan=3)

    tk.Button(window, text="Back to Menu", command=lambda: main_menu(window)).grid(row=4, column=0, columnspan=3)

# Pong Game
def pong_game(window):
    clear_window(window)

    canvas = tk.Canvas(window, width=400, height=300, bg="black")
    canvas.pack()

    paddle1 = canvas.create_rectangle(10, 130, 20, 170, fill="white")
    paddle2 = canvas.create_rectangle(380, 130, 390, 170, fill="white")
    ball = canvas.create_oval(190, 140, 210, 160, fill="white")

    ball_dx, ball_dy = 3, 3
    paddle1_dy, paddle2_dy = 0, 0

    def move_paddles():
        canvas.move(paddle1, 0, paddle1_dy)
        canvas.move(paddle2, 0, paddle2_dy)
        window.after(20, move_paddles)

    def move_ball():
        nonlocal ball_dx, ball_dy
        canvas.move(ball, ball_dx, ball_dy)
        ball_coords = canvas.coords(ball)
        paddle1_coords = canvas.coords(paddle1)
        paddle2_coords = canvas.coords(paddle2)

        # Bounce on top and bottom walls
        if ball_coords[1] <= 0 or ball_coords[3] >= 300:
            ball_dy *= -1

        # Bounce on paddles
        if (ball_coords[0] <= paddle1_coords[2] and paddle1_coords[1] <= ball_coords[1] <= paddle1_coords[3]) or \
           (ball_coords[2] >= paddle2_coords[0] and paddle2_coords[1] <= ball_coords[1] <= paddle2_coords[3]):
            ball_dx *= -1

        # Reset ball if it goes out of bounds
        if ball_coords[0] <= 0 or ball_coords[2] >= 400:
            canvas.coords(ball, 190, 140, 210, 160)
            ball_dx = 3 if ball_coords[0] <= 0 else -3

        window.after(20, move_ball)

    def paddle1_up(event):
        nonlocal paddle1_dy
        paddle1_dy = -5

    def paddle1_down(event):
        nonlocal paddle1_dy
        paddle1_dy = 5

    def paddle2_up(event):
        nonlocal paddle2_dy
        paddle2_dy = -5

    def paddle2_down(event):
        nonlocal paddle2_dy
        paddle2_dy = 5

    def stop_paddles(event):
        nonlocal paddle1_dy, paddle2_dy
        paddle1_dy = 0
        paddle2_dy = 0

    window.bind("w", paddle1_up)
    window.bind("s", paddle1_down)
    window.bind("<Up>", paddle2_up)
    window.bind("<Down>", paddle2_down)
    window.bind("<KeyRelease>", stop_paddles)

    move_paddles()
    move_ball()

    tk.Button(window, text="Back to Menu", command=lambda: main_menu(window)).pack(pady=20)

# Rock Paper Scissors Game
def rps_game(window):
    clear_window(window)
    tk.Label(window, text="Rock Paper Scissors Game").pack()

    def play_rps(player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        result_label.config(text=f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            result = "Draw!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            rps_score['Player'] += 1
        else:
            result = "You Lose!"
            rps_score['Computer'] += 1

        score_label.config(text=f"Player: {rps_score['Player']} - Computer: {rps_score['Computer']}")
        outcome_label.config(text=result)

    tk.Button(window, text="Rock", command=lambda: play_rps("Rock")).pack(pady=5)
    tk.Button(window, text="Paper", command=lambda: play_rps("Paper")).pack(pady=5)
    tk.Button(window, text="Scissors", command=lambda: play_rps("Scissors")).pack(pady=5)

    result_label = tk.Label(window, text="")
    result_label.pack()
    outcome_label = tk.Label(window, text="")
    outcome_label.pack()
    score_label = tk.Label(window, text=f"Player: {rps_score['Player']} - Computer: {rps_score['Computer']}")
    score_label.pack()

    tk.Button(window, text="Back to Menu", command=lambda: main_menu(window)).pack(pady=20)

# Settings Page
def settings_page(window):
    clear_window(window)

    def toggle_sound():
        settings['sound'] = not settings['sound']
        sound_button.config(text=f"Sound: {'ON' if settings['sound'] else 'OFF'}")

    def toggle_high_contrast():
        settings['high_contrast'] = not settings['high_contrast']
        high_contrast_button.config(text=f"High Contrast: {'ON' if settings['high_contrast'] else 'OFF'}")
        if settings['high_contrast']:
            window.configure(bg='black')
        else:
            window.configure(bg='SystemButtonFace')

    def update_font_size():
        try:
            new_size = int(font_size_entry.get())
            settings['font_size'] = new_size
            font_size_label.config(text=f"Font Size: {settings['font_size']}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    tk.Label(window, text="Settings Page", font=("Helvetica", 16)).pack(pady=10)

    sound_button = tk.Button(window, text=f"Sound: {'ON' if settings['sound'] else 'OFF'}", command=toggle_sound)
    sound_button.pack(pady=5)

    high_contrast_button = tk.Button(window, text=f"High Contrast: {'ON' if settings['high_contrast'] else 'OFF'}", command=toggle_high_contrast)
    high_contrast_button.pack(pady=5)

    font_size_label = tk.Label(window, text=f"Font Size: {settings['font_size']}")
    font_size_label.pack(pady=5)

    font_size_entry = tk.Entry(window)
    font_size_entry.pack(pady=5)

    tk.Button(window, text="Update Font Size", command=update_font_size).pack(pady=5)

    tk.Button(window, text="Back to Menu", command=lambda: main_menu(window)).pack(pady=20)

# Initialize Tkinter window
window = tk.Tk()
window.geometry("400x400")
main_menu(window)
window.mainloop()
