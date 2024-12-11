#Project of Rock-Paper-Scissor Game

from tkinter import *
import tkinter.font as font 
import random

root = Tk()
root.title("Rock Paper Scissor Game")
app_font = font.Font(size = 15)
root.config(bg = "#ADD8E6")
root.geometry("700x300")

player_score = 0
computer_score = 0
options = [("rock", 0), ("paper", 1), ("scissor", 2)]

Label(text = "Rock Paper Scissor Game", font = font.Font(size = 30), bg = "#ADD8E6").pack()

def player_choice(player_input):
    global player_score, computer_score
    
    computer_input = get_computer_choice()
    
    player_choice_label.config(text = "You Selected : " + player_input[0])
    computer_choice_label.config(text = "Computer Selected : " + computer_input[0])
    
    if player_input == computer_input:
        winner_label.config(text = "It's tie!!")
    elif (player_input[1]-computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text = "Yehhh You Won!!")
        player_score_label.config(text = "Your Score : " + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text = "Computer Won!!")
        computer_score_label.config(text = "Computer Score : " + str(computer_score))
        
def get_computer_choice():
    return random.choice(options)

winner_label = Label(text = "Let's start the game..", fg = "green", bg = "#ADD8E6", font = font.Font(size = 20), pady = 8)
winner_label.pack()

input_frame = Frame(root, bg = "#ADD8E6")
input_frame.pack()

player_options = Label(input_frame, text = "Your Option : ", font = app_font, fg = "blue", bg = "#ADD8E6")
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = "Rock", width = 20, bd = 0, bg = "brown", pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1,  padx = 8, pady = 5)

paper_btn = Button(input_frame, text = "Paper", width = 20, bd = 0, bg = "silver", pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2,  padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = "Scissor", width = 20, bd = 0, bg = "yellow", pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3,  padx = 8, pady = 5)

score_label = Label(input_frame, text = "Score : ", font = app_font, fg = "blue", bg = "#ADD8E6")
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = "You Selected : --", font = app_font, bg = "#ADD8E6")
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = "Your Score : 0", font = app_font, bg = "#ADD8E6")
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = "Computer Selected : --", font = app_font, fg = "black", bg = "#ADD8E6")
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = "Computer Score : 0", font = app_font, fg = "black", bg = "#ADD8E6")
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

root.mainloop()