from tkinter import *

import random

root = Tk()
root.title("Rock, Paper, Scissor Game")
width = 600
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#9b59b6")


#================================IMAGES========================================
player_rock = PhotoImage(file="assets/rock-user.png")
sm_player_rock = player_rock.subsample(3, 3)
player_paper = PhotoImage(file="assets/paper-user.png")
sm_player_paper = player_paper.subsample(3, 3)
player_scissor = PhotoImage(file="assets/scissors-user.png")
sm_player_scissor = player_scissor.subsample(3, 3)
com_rock = PhotoImage(file="assets/rock-comp.png")
com_paper = PhotoImage(file="assets/paper-comp.png")
com_scissor = PhotoImage(file="assets/scissors-comp.png")
start = PhotoImage(file="assets/start.png").subsample(4)
win = PhotoImage(file="assets/win.png").subsample(5)
lose = PhotoImage(file="assets/lose.png").subsample(5)
draw = PhotoImage(file="assets/draw.png").subsample(5)

#===============================LABEL WIDGET=========================================
player_img = Label(root, image=player_rock, bg="#9b59b6")
comp_img = Label(root, image=com_rock, bg="#9b59b6") 
player_img.grid(row=2, column=1, padx=30, pady=20)
comp_img.grid(row=2, column=3, padx=30, pady=20)

# Score
player_score = Label(root, text="0", font=("Arial", 30), bg="#9b59b6", fg="white")
breaklbl = Label(root, text="-", font=("Arial", 30), bg="#9b59b6", fg="white")
comp_score = Label(root, text="0", font=("Arial", 30), bg="#9b59b6", fg="white")
player_score.grid(row=3, column=1)
comp_score.grid(row=3, column=3)
breaklbl.grid(row=3, column=2)

# Player
lbl_player = Label(root, font=("Arial", 15), text="PLAYER", bg="#9b59b6", fg="white")
lbl_player.grid(row=1, column=1)

# Computer
lbl_computer = Label(root, font=("Arial", 15), text="COMPUTER", bg="#9b59b6", fg="white")
lbl_computer.grid(row=1, column=3)

# Messages
msg = Label(root, font=('Arial', 30), bg="#9b59b6", fg="#CC9900")
msg.grid(row=2, column=2)
msg.configure(image=start)

# Update Player Score
def updatePlayerScore():
    score = int(player_score["text"])
    score += 1
    player_score["text"] = score

# Update Computer Score
def updateComputerScore():
    score = int(comp_score["text"])
    score += 1
    comp_score["text"] = score

#===============================METHODS========================================
def Rock():
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess()
 
def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()
    
def Scissor():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissor)
    MatchProcess()

def MatchProcess():
    com_choice = random.randint(1,3)
    if com_choice == 1:
        comp_img.configure(image=com_rock)
        ComputerRock()
    elif com_choice == 2:
        comp_img.configure(image=com_paper)
        ComputerPaper()
    elif com_choice == 3:
        comp_img.configure(image=com_scissor)
        CompututerScissor()

def ComputerRock():
    if player_choice == 1:
        msg.configure(image=draw)
    elif player_choice == 2:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 3:
        msg.configure(image=lose)
        updateComputerScore()
           
def ComputerPaper():
    if player_choice == 1:
        msg.configure(image=lose)
        updateComputerScore()
    elif player_choice == 2:
        msg.configure(image=draw)
    elif player_choice == 3:
        msg.configure(image=win)
        updatePlayerScore()
    
def CompututerScissor():
    if player_choice == 1:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 2:
        msg.configure(image=lose)
        updateComputerScore()
    elif player_choice == 3:
        msg.configure(image=draw)

def ExitApp():
    root.destroy()
    exit()

#===============================BUTTON WIDGET===================================
rock = Button(root, image=sm_player_rock, command=Rock, bg="red")
paper = Button(root, image=sm_player_paper, command=Paper, bg="yellow")
scissor = Button(root, image=sm_player_scissor, command=Scissor, bg="blue")
btn_quit = Button(root, text="Quit", command=ExitApp)
rock.grid(row=4,column=1, pady=30)
paper.grid(row=4,column=2, pady=30)
scissor.grid(row=4,column=3, pady=30)
btn_quit.grid(row=5, column=2)


#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()