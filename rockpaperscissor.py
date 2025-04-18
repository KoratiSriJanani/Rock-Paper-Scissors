from tkinter import *
import random
game=Tk()
game.title(" ROCK PAPER SCISSOR")
game.geometry("500x500+100+100")
com_score=0
user_score=0

def play(user):
    global com_score
    global user_score
    user=user.lower()
    options = ['rock', 'paper', 'scissor']
    chosen = random.choice(options)
    label1=Label(game,font=('arial',10,'bold'),text=f"the computer choice is {chosen} ",bd=5,fg='black',bg='white').pack()
    if chosen=='rock' and user=='paper':
            user_score+=1
            label2=Label(game,font=('arial',10,'bold'),text="congrats you got one point",bd=5,fg='black',bg='white').pack()
    elif chosen=='rock' and user=='scissor':
            com_score+=1
            label3=Label(game,font=('arial',10,'bold'),text="Oops! Computer got one point",bd=5,fg='black',bg='white').pack()
    elif chosen=='paper' and user=='scissor':
        user_score+=1
        label4=Label(game,font=('arial',10,'bold'),text="congrats you got one point",bd=5,fg='black',bg='white').pack()
    elif chosen=='paper' and user=='rock':
        com_score+=1
        label5=Label(game,font=('arial',10,'bold'),text="Oops! Computer got one point",bd=5,fg='black',bg='white').pack()
    elif chosen=='scissor' and user=='rock':
        user_score+=1
        label6=Label(game,font=('arial',10,'bold'),text="congrats you got one point",bd=5,fg='black',bg='white').pack()
    elif chosen=='scissor' and user=='paper':
        com_score+=1
        label7=Label(game,font=('arial',10,'bold'),text="Oops! Computer got one point",bd=5,fg='black',bg='white').pack()
    elif chosen==user:
        com_score+=1
        user_score+=1
        label8=Label(game,font=('arial',10,'bold'),text="Ohh! it  is a tie..both of you got on point",bd=5,fg='black',bg='white').pack()


def final():
    global com_score
    global user_score
    label9=Label(game,font=('arial',10,'bold'),text=f"THE COMPUTER'S SCORE IS {com_score}",bd=5,fg='black',bg='yellow').pack()
    label10=Label(game,font=('arial',10,'bold'),text=f"YOUR SCORE IS {user_score}",bd=5,fg='black',bg='yellow').pack()
    if com_score>user_score:
        label11=Label(game,font=('arial',10,'bold'),text='COMPUTER WON !!!',bd=5,fg='black',bg='yellow').pack()
    elif com_score==user_score:
        label12=Label(game,font=('arial',10,'bold'),text='OHH!  IT IS TIE ',bd=5,fg='black',bg='yellow').pack()
    else:
        label13=Label(game,font=('arial',10,'bold'),text='YOU WON THE ROUND!',bd=5,fg='black',bg='yellow').pack()

button1=Button(game,font=('arial',15,'bold'),text='ROCK',bd=15,fg='black',bg='brown',command=lambda:play('ROCK')).pack()
button2=Button(game,font=('arial',15,'bold'),text='PAPER',bd=15,fg='black',bg='brown',command=lambda:play('PAPER')).pack()
button3=Button(game,font=('arial',15,'bold'),text='SCISSOR',bd=15,fg='black',bg='brown',command=lambda:play('SCISSOR')).pack()

button3=Button(game,font=('arial',15,'bold'),text='END',bd=15,fg='black',bg='brown',command=lambda:final()).pack()

