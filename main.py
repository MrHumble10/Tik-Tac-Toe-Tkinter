from tkinter import messagebox
from tkinter import *

count = 1
clicked = True
winner_1 = False
winner_2 = False

# _________________________Game_________________________>
windows = Tk()
windows.minsize(width=565, height=600)
windows.title("Tik Tak Toe Game")
windows.config(bg='#99C4C8', highlightthickness=4, highlightcolor="#68A7AD")


def game():
    global clicked, count
    clicked = True
    count = 1
    # _________________________Button selection_________________________>
    def b_click(b):
        global clicked, count
        print(count)

        if not b['text'] == " ":
            messagebox.showerror("Tic Tak Toe", "OPS!!!\nIt is already selected chose another one.")

        elif b['text'] == " " and clicked is True:
            b['text'] = "X"
            b['bg'] = "#87E5DA"
            clicked = False
            count += 1
            conditions()
        elif b['text'] == " " and clicked is False:
            b['text'] = "O"
            b['bg'] = "#87E5DA"
            clicked = True
            count += 1
            conditions()

    # _________________________Disable Buttons____________________>
    def disable_buttons():
        btn_1.config(state=DISABLED)
        btn_2.config(state=DISABLED)
        btn_3.config(state=DISABLED)
        btn_4.config(state=DISABLED)
        btn_5.config(state=DISABLED)
        btn_6.config(state=DISABLED)
        btn_7.config(state=DISABLED)
        btn_8.config(state=DISABLED)
        btn_9.config(state=DISABLED)

    def winner(b1, b2, b3, player):
        global clicked, count
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        situation_lb.config(text=f"player {player} won!!", fg="green")
        situation_lb.place(x=180, y=20)
        disable_buttons()
        clicked = True
        play_again = messagebox.askyesno("Tic Tak Toe", "Would you like to play again?")
        if not play_again:
            exit()
        else:
            situation_lb.config(text=" ")
            count = 1
            game()
        return True

    # _________________________Conditions_________________________>
    def conditions():
        global winner_1, winner_2, clicked, count
        winner_1 = False
        winner_2 = False
        # ---------------------------Player 1----------------------------------->

        if btn_1['text'] == "X" and btn_2['text'] == "X" and btn_3['text'] == "X":
            winner(btn_1, btn_2, btn_3, 1)
        elif btn_4['text'] == "X" and btn_5['text'] == "X" and btn_6['text'] == "X":
            winner(btn_4, btn_5, btn_6, 1)
        elif btn_7['text'] == "X" and btn_8['text'] == "X" and btn_9['text'] == "X":
            winner(btn_7, btn_8, btn_9, 1)
        elif btn_1['text'] == "X" and btn_5['text'] == "X" and btn_9['text'] == "X":
            winner(btn_1, btn_5, btn_9, 1)
        elif btn_3['text'] == "X" and btn_5['text'] == "X" and btn_7['text'] == "X":
            winner(btn_3, btn_5, btn_7, 2)
        elif btn_1['text'] == "X" and btn_4['text'] == "X" and btn_7['text'] == "X":
            winner(btn_1, btn_4, btn_7, 1)
        elif btn_2['text'] == "X" and btn_5['text'] == "X" and btn_8['text'] == "X":
            winner(btn_2, btn_5, btn_8, 1)
        elif btn_3['text'] == "X" and btn_6['text'] == "X" and btn_9['text'] == "X":
            winner(btn_3, btn_6, btn_9, 1)

        # ---------------------------Player 2----------------------------------->

        elif btn_1['text'] == "O" and btn_2['text'] == "O" and btn_3['text'] == "O":
            winner(btn_1, btn_2, btn_3, 2)
        elif btn_4['text'] == "O" and btn_5['text'] == "O" and btn_6['text'] == "O":
            winner(btn_4, btn_5, btn_6, 2)
        elif btn_7['text'] == "O" and btn_8['text'] == "O" and btn_9['text'] == "O":
            winner(btn_7, btn_8, btn_9, 2)
        elif btn_1['text'] == "O" and btn_5['text'] == "O" and btn_9['text'] == "O":
            winner(btn_1, btn_5, btn_9, 2)
        elif btn_3['text'] == "O" and btn_5['text'] == "O" and btn_7['text'] == "O":
            winner(btn_3, btn_5, btn_7, 2)
        elif btn_1['text'] == "O" and btn_4['text'] == "O" and btn_7['text'] == "O":
            winner(btn_1, btn_4, btn_7, 2)
        elif btn_2['text'] == "O" and btn_5['text'] == "O" and btn_8['text'] == "O":
            winner(btn_2, btn_5, btn_8, 2)
        elif btn_3['text'] == "O" and btn_6['text'] == "O" and btn_9['text'] == "O":
            winner(btn_3, btn_6, btn_9, 2)
        elif count == 10:
            messagebox.showinfo("Tic Tac Toe", "It's A Draw, maybe another time.")
            count = 1
            disable_buttons()
            clicked = True

    # _________________________Labels_________________________>
    situation_lb = Label(text="Tic Tak Toe", background="#99C4C8", fg='#424242', font=('Elephant', 20, "normal"))
    situation_lb.place(x=200, y=20)

    lets_play_lb = Label(text="Lets Play", background="#F87D42", fg='white', font=('Josefin Sans', 20, "bold"))
    # lets_play_lb.place(x=215, y=20)

    # _________________________Buttons_________________________>
    btn_1 = Button(text=' ', bg="#424242", width=12, height=6, command=lambda: b_click(btn_1))
    btn_1.place(x=100, y=80)
    btn_2 = Button(text=' ', bg="#424242", width=12, height=6, command=lambda: b_click(btn_2))
    btn_2.place(x=230, y=80)
    btn_3 = Button(text=' ', bg="#424242", width=12, height=6, command=lambda: b_click(btn_3))
    btn_3.place(x=360, y=80)

    btn_4 = Button(text=' ', bg="#424242", width=12, height=6, command=lambda: b_click(btn_4))
    btn_4.place(x=100, y=200)
    btn_5 = Button(text=' ', bg="#424242", width=12, height=6, command=lambda: b_click(btn_5))
    btn_5.place(x=230, y=200)
    btn_6 = Button(text=' ', bg="#424242", width=12, height=6, command=lambda: b_click(btn_6))
    btn_6.place(x=360, y=200)

    btn_7 = Button(text=' ', bg="#424242", width=12, height=6, command=lambda: b_click(btn_7))
    btn_7.place(x=100, y=320)
    btn_8 = Button(text=' ', bg="#424242", width=12, height=6, command=lambda: b_click(btn_8))
    btn_8.place(x=230, y=320)
    btn_9 = Button(text=' ', bg="#424242", width=12, height=6, command=lambda: b_click(btn_9))
    btn_9.place(x=360, y=320)

    play_btn = Button(text='Play again', bg="#CD3131", fg="#F6F6F6", command=game, font=('Elephant', 12, "normal"))
    play_btn.place(x=225, y=460)

    windows.mainloop()


game()
