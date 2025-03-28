import tkinter as tk
from tkinter import messagebox
import time

def check_winner():
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != "":    
            highlight_winner(board[row][0], board[row][1], board[row][2])
            return True
    
    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != "":
            highlight_winner(board[0][col], board[1][col], board[2][col])
            return True
    
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        highlight_winner(board[0][0], board[1][1], board[2][2])
        return True
    
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        highlight_winner(board[0][2], board[1][1], board[2][0])
        return True
    
    return False

def highlight_winner(*cells):
    for _ in range(5):
        for cell in cells:
            cell.config(bg='lightgreen')
        root.update()
        time.sleep(0.2)
        for cell in cells:
            cell.config(bg='white')
        root.update()
        time.sleep(0.2)
    for cell in cells:
        cell.config(bg='lightgreen')
    messagebox.showinfo("Tic Tac Toe", f"Player {turn} wins!")
    root.quit()

def on_click(row, col):
    global turn
    if board[row][col]['text'] == "" and not check_winner():
        board[row][col]['text'] = turn
        board[row][col].config(fg="blue" if turn == "X" else "red")
        animate_button(board[row][col])
        if check_winner():
            return
        turn = "O" if turn == "X" else "X"
        
def animate_button(button):
    for _ in range(5):
        button.config(bg='yellow')
        root.update()
        time.sleep(0.1)
        button.config(bg='white')
        root.update()
        time.sleep(0.1)

def create_board():
    for r in range(3):
        row = []
        for c in range(3):
            button = tk.Button(root, text="", font=('Arial', 24), height=2, width=5,
                               command=lambda r=r, c=c: on_click(r, c))
            button.grid(row=r, column=c)
            row.append(button)
        board.append(row)

root = tk.Tk()
root.title("Tic Tac Toe")
turn = "X"
board = []
create_board()
root.mainloop()
