import csv
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
def play_game():
    global required
    parameters=['V1','V2','V3','V4','V5','V6','V7','V8','V9']
    # Tic Tac Toe
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # Create the board
    board = [' ' for _ in range(9)]

    # Create the GUI
    root = tk.Tk()
    root.title("Tic Tac Toe")
    #changing the icon of GUI
    root.iconbitmap(r"C:\Users\nayak\Downloads\tic-tac-toe_39453.ico")
    # Function to check if the board is full
    def is_board_full():
        return ' ' not in board

    # Function to check if there's a winner
    def is_winner(player):
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True
        return False

    # Function to make a move
    def make_move(player, position):
        global required
        board[position] = 'X'
        buttons[position].config(text=player)
        buttons[position].config(state=tk.DISABLED)
        temp=[]
        for i in required:
            if i[position] == 'x':
                temp.append(i)
        required = temp
        #print(required)

    # Function for the computer player to make a move
    def computer_move():
        quantities=[]
        global required
        value = 0
        maxi = 0
        temp = []
        for i in range(9):
            count = 0
            for j in required:
                if j[i] == 'o':
                    count += 1
            if count >= maxi and board[i] == ' ':
                maxi = count
                value = i
        for i in winning_combinations:
            if board[i[0]] == board[i[1]] == 'X' and board[i[2]] == ' ':
                value = i[2]
            elif board[i[1]] == board[i[2]] == 'X' and board[i[0]] == ' ':
                value = i[0]
            elif board[i[0]] == board[i[2]] == 'X' and board[i[1]] == ' ':
                value = i[1]
            elif board[i[0]] == board[i[1]] == 'O' and board[i[2]] == ' ':
                value = i[2]
            elif board[i[1]] == board[i[2]] == 'O' and board[i[0]] == ' ':
                value = i[0]
            elif board[i[0]] == board[i[2]] == 'O' and board[i[1]] == ' ':
                value = i[1]
        for i in required:
            if i[value] == 'o':
                temp.append(i)
        #print(len(temp))
        required = temp
        for i in range(9):
            accum=0
            for j in temp:
                if j[i]=='o' and board[i]==' ':
                    accum+=1
            quantities.append(accum)
        board[value] = 'O'
        buttons[value].config(text='O')
        buttons[value].config(state=tk.DISABLED)
        #print(quantities)
        if graphs=='yes':
            plt.bar(parameters,quantities,label='most probable steps made by computer',color='g')
            plt.title('computer probable steps')
            plt.grid(True,color='k')
            plt.legend()
            plt.show()
    # Function to handle button clicks
    def button_click(position):
        if board[position] != ' ':
            return

        make_move('X', position)

        if is_winner('X'):
            messagebox.showinfo("Game Over", "Player X wins!")
            return

        if is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            return

        computer_move()

        if is_winner('O'):
            messagebox.showinfo("Game Over", "Computer wins!")
            return

        if is_board_full():
            messagebox.showinfo("Game Over", "It's a tie!")

    # Create the buttons
    buttons = []
    for i in range(9):
        button = tk.Button(root, text=' ', font=('Arial', 24), width=4, height=2,
                           command=lambda pos=i: button_click(pos))
        button.grid(row=i // 3, column=i % 3)
        buttons.append(button)

    # Read the required moves from the CSV file
    with open('C:\\Users\\nayak\\Desktop\\cad abhi\\tic-tac-toe-endgame.csv', 'r') as file:
        reader = csv.reader(file)
        required = []
        for i in reader:
            if i[9] != 'positive':
                required.append(i)
    # Start the game
    root.mainloop()
while True:
    msg= messagebox.askquestion('Tic-Tac-Toe','do you want to play the game?',icon='question')
    if msg=='yes':
        graphs=messagebox.askquestion('graphs','do you want graphs for most probable steps taken by the computer?',icon='question')
        play_game()
    else:
        break