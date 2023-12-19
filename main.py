import random
import tkinter
from tkinter import messagebox
from tkinter import *
import pandas as pd
import os

count = 1
clicked = True
winner_1 = False
winner_2 = False
computer_player = False
random_btn = 0
level_three = False
level_two = False
level_one = False


def level():
    global random_btn, count, clicked
    random_btn['text'] = "O"
    random_btn['bg'] = "#87E5DA"
    count += 1
    clicked = True


if not os.path.isfile("points.csv"):
    dic = [{'player1': 0, "player2": 0}]
    df = pd.DataFrame(dic)
    df.to_csv("points.csv")

df = pd.read_csv("points.csv")
player1_points = df["player1"].item()
player2_points = df["player2"].item()


# _________________________Reset Points_________________________>

def reset_points():
    global player1_points, player2_points, level_one, level_two, level_three
    level_one = False
    level_two = False
    level_three = False
    dataf = pd.read_csv("points.csv")
    point = dataf["player1"].item()
    point2 = dataf["player2"].item()

    if point == 0 and point2 == 0:
        messagebox.showinfo('Tic Tak Toe', "The game is already resat")
        return

    elif messagebox.askyesno('Tic Tak Toe', "Do you really want to reset the points?"):
        data = [{'player1': 0, "player2": 0}]
        csv_df = pd.DataFrame(data)
        csv_df.to_csv("points.csv")
        player1_points = 0
        player2_points = 0
        p1_point_lb.config(text="0")
        p2_point_lb.config(text="0")
        game(False)
    else:
        return


# _________________________Game_________________________>
windows = Tk()
windows.minsize(width=565, height=600)
windows.title("Tik Tak Toe Game")
windows.iconbitmap("icon.ico")
windows.config(bg='#99C4C8', highlightthickness=4, highlightcolor="#68A7AD")
canvas = Canvas(width=90, height=90, highlightthickness=0, bg='#99C4C8')
canvas2 = Canvas(width=90, height=90, highlightthickness=0, bg='#99C4C8')

image = tkinter.PhotoImage(file="user_img.jpg")
canvas.create_image(43, 40, image=image)
canvas.place(x=76, y=440)
user_lb = Label(text="Player X", bg="#99C4C8", fg="white", font=('Elephant', 10, "normal"))
user_lb.place(x=138, y=470)

p1_point_lb = Label(text=f"{player1_points}", bg="#99C4C8", fg="white", font=('Elephant', 30, "normal"))
p1_point_lb.place(x=138, y=500)

canvas2.create_image(43, 40, image=image)
canvas2.place(x=340, y=440)
user_lb = Label(text="Player O", bg="#99C4C8", fg="white", font=('Elephant', 10, "normal"))
user_lb.place(x=403, y=470)

p2_point_lb = Label(text=f"{player2_points}", bg="#99C4C8", fg="white", font=('Elephant', 30, "normal"))
p2_point_lb.place(x=403, y=500)


def game(again):
    global clicked, count, level_three, level_two, level_one

    if count == 1:
        pass

    elif again is True:
        if not messagebox.askyesno("Tik Tak Toe", "Do you really want to start over?"):
            return

    clicked = True
    count = 1

    # _________________________Button selection_________________________>
    def b_click(b):
        global clicked, count, computer_player, random_btn, level_three, level_two, level_one

        if not b['text'] == " ":
            messagebox.showerror("Tic Tak Toe", "OPS!!!\nIt is already selected chose another one.")

        elif b['text'] == " " and clicked is True:
            b['text'] = "X"
            b['bg'] = "#87E5DA"
            clicked = False
            count += 1
            conditions()

            if checkbutton_used() and clicked is False:
                btn_list = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]

                # -----------------------Level Three---------------------------->
                # def level_3():
                #
                #     global clicked, count, computer_player, random_btn, level_three, level_two, level_one
                #     if level_three and btn_5['text'] == "X":
                #         random_btn = btn_list[0]
                #         level(1)
                #         conditions()
                #         level_three = False
                #         level_two = True
                #         level_one = True

                # -----------------------Level Two---------------------------->
                def level_3_condition(levels, item):
                    global clicked, count, computer_player, random_btn, level_three, level_two, level_one
                    if levels and btn_5['text'] == "X" and btn_2["text"] == " " and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    elif levels and btn_5['text'] == " " and btn_5["text"] == " " and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and btn_3["text"] == item and btn_2["text"] == item and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    elif btn_5["text"] == 'X' and btn_9["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    elif levels and  btn_1["text"] == item and btn_3["text"] == item and btn_2["text"] == ' ':
                        random_btn = btn_list[1]
                        level()
                        conditions()
                    elif levels and  btn_1["text"] == item and btn_2["text"] == item and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    # ------------------------Row two-------------------------->
                    elif levels and  btn_6["text"] == item and btn_5["text"] == item and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif levels and  btn_6["text"] == item and btn_4["text"] == item and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and  btn_4["text"] == item and btn_5["text"] == item and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    # ------------------------Row Three-------------------------->
                    elif levels and  btn_9["text"] == item and btn_8["text"] == item and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif levels and  btn_9["text"] == item and btn_7["text"] == item and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif levels and  btn_8["text"] == item and btn_7["text"] == item and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    # ------------------------Column One-------------------------->
                    elif levels and  btn_1["text"] == item and btn_4["text"] == item and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif levels and  btn_1["text"] == 'O' and btn_7["text"] == item and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif levels and  btn_4["text"] == item and btn_7["text"] == item and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column Two-------------------------->
                    elif levels and  btn_2["text"] == item and btn_5["text"] == item and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif levels and  btn_2["text"] == item and btn_8["text"] == item and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and  btn_5["text"] == item and btn_8["text"] == item and btn_2["text"] == ' ':
                        random_btn = btn_list[1]
                        level()
                        conditions()
                    # ------------------------Column Three-------------------------->
                    elif levels and  btn_3["text"] == item and btn_6["text"] == item and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif levels and  btn_3["text"] == item and btn_9["text"] == item and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    elif levels and  btn_9["text"] == item and btn_6["text"] == item and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif levels and  btn_1["text"] == item and btn_5["text"] == item and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif levels and  btn_1["text"] == item and btn_9["text"] == item and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and  btn_9["text"] == item and btn_5["text"] == item and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif levels and  btn_3["text"] == item and btn_5["text"] == item and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif levels and  btn_3["text"] == item and btn_7["text"] == item and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and  btn_7["text"] == item and btn_5["text"] == item and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    elif btn_3["text"] == 'X' and btn_2["text"] == 'X' and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_3["text"] == 'X' and btn_2["text"] == ' ':
                        random_btn = btn_list[1]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_2["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    # ------------------------Row two-------------------------->
                    elif btn_6["text"] == 'X' and btn_5["text"] == 'X' and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif btn_6["text"] == 'X' and btn_4["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_4["text"] == 'X' and btn_5["text"] == 'X' and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    # ------------------------Row Three-------------------------->
                    elif btn_9["text"] == 'X' and btn_8["text"] == 'X' and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif btn_9["text"] == 'X' and btn_7["text"] == 'X' and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif btn_8["text"] == 'X' and btn_7["text"] == 'X' and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    # ------------------------Column One-------------------------->
                    elif btn_1["text"] == 'X' and btn_4["text"] == 'X' and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_7["text"] == 'X' and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif btn_4["text"] == 'X' and btn_7["text"] == 'X' and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column Two-------------------------->
                    elif btn_2["text"] == 'X' and btn_5["text"] == 'X' and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif btn_2["text"] == 'X' and btn_8["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_5["text"] == 'X' and btn_8["text"] == 'X' and btn_2["text"] == ' ':
                        random_btn = btn_list[1]
                        level()
                        conditions()
                    # ------------------------Column Three-------------------------->
                    elif btn_3["text"] == 'X' and btn_6["text"] == 'X' and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif btn_3["text"] == 'X' and btn_9["text"] == 'X' and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    elif btn_9["text"] == 'X' and btn_6["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif btn_1["text"] == 'X' and btn_5["text"] == 'X' and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_9["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_9["text"] == 'X' and btn_5["text"] == 'X' and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif btn_3["text"] == 'X' and btn_5["text"] == 'X' and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif btn_3["text"] == 'X' and btn_7["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_7["text"] == 'X' and btn_5["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                def level_2_conditions(levels, item):
                    global clicked, count, computer_player, random_btn, level_three, level_two, level_one
                    if levels and btn_5['text'] == "X" and btn_2["text"] == " " and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    elif levels and btn_5['text'] == " " and btn_5["text"] == " " and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and btn_3["text"] == item and btn_2["text"] == item and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    elif levels and  btn_6["text"] == item and btn_5["text"] == item and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif levels and  btn_6["text"] == item and btn_4["text"] == item and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and  btn_4["text"] == item and btn_5["text"] == item and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    # ------------------------Row Three-------------------------->
                    elif levels and  btn_9["text"] == item and btn_8["text"] == item and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif levels and  btn_9["text"] == item and btn_7["text"] == item and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif levels and  btn_8["text"] == item and btn_7["text"] == item and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    # ------------------------Column One-------------------------->
                    elif levels and  btn_1["text"] == item and btn_4["text"] == item and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif levels and  btn_1["text"] == 'O' and btn_7["text"] == item and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif levels and  btn_4["text"] == item and btn_7["text"] == item and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column Two-------------------------->
                    elif levels and  btn_2["text"] == item and btn_5["text"] == item and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif levels and  btn_2["text"] == item and btn_8["text"] == item and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and  btn_5["text"] == item and btn_8["text"] == item and btn_2["text"] == ' ':
                        random_btn = btn_list[1]
                        level()
                        conditions()
                    # ------------------------Column Three-------------------------->
                    elif levels and  btn_3["text"] == item and btn_6["text"] == item and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif levels and  btn_3["text"] == item and btn_9["text"] == item and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    elif levels and  btn_9["text"] == item and btn_6["text"] == item and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif levels and  btn_1["text"] == item and btn_5["text"] == item and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif levels and  btn_1["text"] == item and btn_9["text"] == item and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and  btn_9["text"] == item and btn_5["text"] == item and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif levels and  btn_3["text"] == item and btn_5["text"] == item and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif levels and  btn_3["text"] == item and btn_7["text"] == item and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif levels and  btn_7["text"] == item and btn_5["text"] == item and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    elif btn_3["text"] == 'X' and btn_2["text"] == 'X' and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_3["text"] == 'X' and btn_2["text"] == ' ':
                        random_btn = btn_list[1]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_2["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    # ------------------------Row two-------------------------->
                    elif btn_6["text"] == 'X' and btn_5["text"] == 'X' and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif btn_6["text"] == 'X' and btn_4["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_4["text"] == 'X' and btn_5["text"] == 'X' and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    # ------------------------Row Three-------------------------->
                    elif btn_9["text"] == 'X' and btn_8["text"] == 'X' and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif btn_9["text"] == 'X' and btn_7["text"] == 'X' and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif btn_8["text"] == 'X' and btn_7["text"] == 'X' and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    # ------------------------Column One-------------------------->
                    elif btn_1["text"] == 'X' and btn_4["text"] == 'X' and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_7["text"] == 'X' and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif btn_4["text"] == 'X' and btn_7["text"] == 'X' and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column Two-------------------------->
                    elif btn_2["text"] == 'X' and btn_5["text"] == 'X' and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif btn_2["text"] == 'X' and btn_8["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_5["text"] == 'X' and btn_8["text"] == 'X' and btn_2["text"] == ' ':
                        random_btn = btn_list[1]
                        level()
                        conditions()
                    # ------------------------Column Three-------------------------->
                    elif btn_3["text"] == 'X' and btn_6["text"] == 'X' and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif btn_3["text"] == 'X' and btn_9["text"] == 'X' and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    elif btn_9["text"] == 'X' and btn_6["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif btn_1["text"] == 'X' and btn_5["text"] == 'X' and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_9["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_9["text"] == 'X' and btn_5["text"] == 'X' and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif btn_3["text"] == 'X' and btn_5["text"] == 'X' and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif btn_3["text"] == 'X' and btn_7["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_7["text"] == 'X' and btn_5["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                def level_1_condition():
                    global clicked, count, computer_player, random_btn, level_three, level_two, level_one
                    if btn_3["text"] == 'X' and btn_2["text"] == 'X' and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_3["text"] == 'X' and btn_2["text"] == ' ':
                        random_btn = btn_list[1]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_2["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    # ------------------------Row two-------------------------->
                    elif btn_6["text"] == 'X' and btn_5["text"] == 'X' and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif btn_6["text"] == 'X' and btn_4["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_4["text"] == 'X' and btn_5["text"] == 'X' and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    # ------------------------Row Three-------------------------->
                    elif btn_9["text"] == 'X' and btn_8["text"] == 'X' and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif btn_9["text"] == 'X' and btn_7["text"] == 'X' and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif btn_8["text"] == 'X' and btn_7["text"] == 'X' and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    # ------------------------Column One-------------------------->
                    elif btn_1["text"] == 'X' and btn_4["text"] == 'X' and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_7["text"] == 'X' and btn_4["text"] == ' ':
                        random_btn = btn_list[3]
                        level()
                        conditions()
                    elif btn_4["text"] == 'X' and btn_7["text"] == 'X' and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column Two-------------------------->
                    elif btn_2["text"] == 'X' and btn_5["text"] == 'X' and btn_8["text"] == ' ':
                        random_btn = btn_list[7]
                        level()
                        conditions()
                    elif btn_2["text"] == 'X' and btn_8["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_5["text"] == 'X' and btn_8["text"] == 'X' and btn_2["text"] == ' ':
                        random_btn = btn_list[1]
                        level()
                        conditions()
                    # ------------------------Column Three-------------------------->
                    elif btn_3["text"] == 'X' and btn_6["text"] == 'X' and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif btn_3["text"] == 'X' and btn_9["text"] == 'X' and btn_6["text"] == ' ':
                        random_btn = btn_list[5]
                        level()
                        conditions()
                    elif btn_9["text"] == 'X' and btn_6["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif btn_1["text"] == 'X' and btn_5["text"] == 'X' and btn_9["text"] == ' ':
                        random_btn = btn_list[8]
                        level()
                        conditions()
                    elif btn_1["text"] == 'X' and btn_9["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_9["text"] == 'X' and btn_5["text"] == 'X' and btn_1["text"] == ' ':
                        random_btn = btn_list[0]
                        level()
                        conditions()
                    # ------------------------Column -------------------------->
                    elif btn_3["text"] == 'X' and btn_5["text"] == 'X' and btn_7["text"] == ' ':
                        random_btn = btn_list[6]
                        level()
                        conditions()
                    elif btn_3["text"] == 'X' and btn_7["text"] == 'X' and btn_5["text"] == ' ':
                        random_btn = btn_list[4]
                        level()
                        conditions()
                    elif btn_7["text"] == 'X' and btn_5["text"] == 'X' and btn_3["text"] == ' ':
                        random_btn = btn_list[2]
                        level()
                        conditions()

                if level_three:
                    level_3_condition(level_three, "O")

                elif level_two:
                    level_2_conditions(level_two, "O")
                elif level_one:
                    level_1_condition()

                # ------------------------Row One-------------------------->
                # elif btn_3["text"] == 'X' and btn_2["text"] == 'X' and btn_1["text"] == ' ':
                #     random_btn = btn_list[0]
                #     level(1)
                #     conditions()
                # elif btn_1["text"] == 'X' and btn_3["text"] == 'X' and btn_2["text"] == ' ':
                #     random_btn = btn_list[1]
                #     level(2)
                #     conditions()
                # elif btn_1["text"] == 'X' and btn_2["text"] == 'X' and btn_3["text"] == ' ':
                #     random_btn = btn_list[2]
                #     level(3)
                #     conditions()
                # # ------------------------Row two-------------------------->
                # elif btn_6["text"] == 'X' and btn_5["text"] == 'X' and btn_4["text"] == ' ':
                #     random_btn = btn_list[3]
                #     level(4)
                #     conditions()
                # elif btn_6["text"] == 'X' and btn_4["text"] == 'X' and btn_5["text"] == ' ':
                #     random_btn = btn_list[4]
                #     level(5)
                #     conditions()
                # elif btn_4["text"] == 'X' and btn_5["text"] == 'X' and btn_6["text"] == ' ':
                #     random_btn = btn_list[5]
                #     level(6)
                #     conditions()
                # # ------------------------Row Three-------------------------->
                # elif btn_9["text"] == 'X' and btn_8["text"] == 'X' and btn_7["text"] == ' ':
                #     random_btn = btn_list[6]
                #     level(7)
                #     conditions()
                # elif btn_9["text"] == 'X' and btn_7["text"] == 'X' and btn_8["text"] == ' ':
                #     random_btn = btn_list[7]
                #     level(8)
                #     conditions()
                # elif btn_8["text"] == 'X' and btn_7["text"] == 'X' and btn_9["text"] == ' ':
                #     random_btn = btn_list[8]
                #     level(9)
                #     conditions()
                # # ------------------------Column One-------------------------->
                # elif btn_1["text"] == 'X' and btn_4["text"] == 'X' and btn_7["text"] == ' ':
                #     random_btn = btn_list[6]
                #     level(10)
                #     conditions()
                # elif btn_1["text"] == 'X' and btn_7["text"] == 'X' and btn_4["text"] == ' ':
                #     random_btn = btn_list[3]
                #     level(11)
                #     conditions()
                # elif btn_4["text"] == 'X' and btn_7["text"] == 'X' and btn_1["text"] == ' ':
                #     random_btn = btn_list[0]
                #     level(12)
                #     conditions()
                # # ------------------------Column Two-------------------------->
                # elif btn_2["text"] == 'X' and btn_5["text"] == 'X' and btn_8["text"] == ' ':
                #     random_btn = btn_list[7]
                #     level(13)
                #     conditions()
                # elif btn_2["text"] == 'X' and btn_8["text"] == 'X' and btn_5["text"] == ' ':
                #     random_btn = btn_list[4]
                #     level(14)
                #     conditions()
                # elif btn_5["text"] == 'X' and btn_8["text"] == 'X' and btn_2["text"] == ' ':
                #     random_btn = btn_list[1]
                #     level(15)
                #     conditions()
                # # ------------------------Column Three-------------------------->
                # elif btn_3["text"] == 'X' and btn_6["text"] == 'X' and btn_9["text"] == ' ':
                #     random_btn = btn_list[8]
                #     level(16)
                #     conditions()
                # elif btn_3["text"] == 'X' and btn_9["text"] == 'X' and btn_6["text"] == ' ':
                #     random_btn = btn_list[5]
                #     level(17)
                #     conditions()
                # elif btn_9["text"] == 'X' and btn_6["text"] == 'X' and btn_3["text"] == ' ':
                #     random_btn = btn_list[2]
                #     level(18)
                #     conditions()
                # # ------------------------Column -------------------------->
                # elif btn_1["text"] == 'X' and btn_5["text"] == 'X' and btn_9["text"] == ' ':
                #     random_btn = btn_list[8]
                #     level(19)
                #     conditions()
                # elif btn_1["text"] == 'X' and btn_9["text"] == 'X' and btn_5["text"] == ' ':
                #     random_btn = btn_list[4]
                #     level(20)
                #     conditions()
                # elif btn_9["text"] == 'X' and btn_5["text"] == 'X' and btn_1["text"] == ' ':
                #     random_btn = btn_list[0]
                #     level(21)
                #     conditions()
                # # ------------------------Column -------------------------->
                # elif btn_3["text"] == 'X' and btn_5["text"] == 'X' and btn_7["text"] == ' ':
                #     random_btn = btn_list[6]
                #     level(22)
                #     conditions()
                # elif btn_3["text"] == 'X' and btn_7["text"] == 'X' and btn_5["text"] == ' ':
                #     random_btn = btn_list[4]
                #     level(23)
                #     conditions()
                # elif btn_7["text"] == 'X' and btn_5["text"] == 'X' and btn_3["text"] == ' ':
                #     random_btn = btn_list[2]
                #     level(24)
                #     conditions()

                random_btn = btn_list[random.randint(0, 8)]
                while not random_btn['text'] == " ":
                    random_btn = btn_list[random.randint(0, 8)]
                    print(f"first{btn_list[0]}")
                # ----------------------Game Level-------------------------------->

                if random_btn['text'] == " " and clicked is False:
                    random_btn['text'] = "O"
                    random_btn['bg'] = "#87E5DA"
                    clicked = True
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
        global clicked, count, player1_points, player2_points
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        situation_lb.config(text=f"player {player} won!!", fg="green")
        if player == "X":
            player1_points += 1
            p1_point_lb.config(text=f"{player1_points}")

        elif player == "O":
            player2_points += 1
            p2_point_lb.config(text=f"{player2_points}")

        file_dict = [{'player1': player1_points, "player2": player2_points}]
        file_df = pd.DataFrame(file_dict)
        file_df.to_csv("points.csv")

        situation_lb.place(x=180, y=20)
        disable_buttons()
        clicked = True
        play_again = messagebox.askyesno("Tic Tak Toe", "Would you like to play again?")
        if not play_again:
            exit()
        else:
            situation_lb.config(text=" ")
            count = 1
            game(False)
        return True

    # _________________________Conditions_________________________>
    def conditions():
        global winner_1, winner_2, clicked, count
        winner_1 = False
        winner_2 = False
        # ---------------------------Player 1----------------------------------->

        if btn_1['text'] == "X" and btn_2['text'] == "X" and btn_3['text'] == "X":
            winner(btn_1, btn_2, btn_3, "X")
        elif btn_4['text'] == "X" and btn_5['text'] == "X" and btn_6['text'] == "X":
            winner(btn_4, btn_5, btn_6, "X")
        elif btn_7['text'] == "X" and btn_8['text'] == "X" and btn_9['text'] == "X":
            winner(btn_7, btn_8, btn_9, "X")
        elif btn_1['text'] == "X" and btn_5['text'] == "X" and btn_9['text'] == "X":
            winner(btn_1, btn_5, btn_9, "X")
        elif btn_3['text'] == "X" and btn_5['text'] == "X" and btn_7['text'] == "X":
            winner(btn_3, btn_5, btn_7, "X")
        elif btn_1['text'] == "X" and btn_4['text'] == "X" and btn_7['text'] == "X":
            winner(btn_1, btn_4, btn_7, "X")
        elif btn_2['text'] == "X" and btn_5['text'] == "X" and btn_8['text'] == "X":
            winner(btn_2, btn_5, btn_8, "X")
        elif btn_3['text'] == "X" and btn_6['text'] == "X" and btn_9['text'] == "X":
            winner(btn_3, btn_6, btn_9, "X")

        # ---------------------------Player 2----------------------------------->

        elif btn_1['text'] == "O" and btn_2['text'] == "O" and btn_3['text'] == "O":
            winner(btn_1, btn_2, btn_3, "O")
        elif btn_4['text'] == "O" and btn_5['text'] == "O" and btn_6['text'] == "O":
            winner(btn_4, btn_5, btn_6, "O")
        elif btn_7['text'] == "O" and btn_8['text'] == "O" and btn_9['text'] == "O":
            winner(btn_7, btn_8, btn_9, "O")
        elif btn_1['text'] == "O" and btn_5['text'] == "O" and btn_9['text'] == "O":
            winner(btn_1, btn_5, btn_9, "O")
        elif btn_3['text'] == "O" and btn_5['text'] == "O" and btn_7['text'] == "O":
            winner(btn_3, btn_5, btn_7, "O")
        elif btn_1['text'] == "O" and btn_4['text'] == "O" and btn_7['text'] == "O":
            winner(btn_1, btn_4, btn_7, "O")
        elif btn_2['text'] == "O" and btn_5['text'] == "O" and btn_8['text'] == "O":
            winner(btn_2, btn_5, btn_8, "O")
        elif btn_3['text'] == "O" and btn_6['text'] == "O" and btn_9['text'] == "O":
            winner(btn_3, btn_6, btn_9, "O")
        elif count == 10:
            messagebox.showinfo("Tic Tac Toe", "It's A Draw, maybe another time.")
            count = 1
            disable_buttons()
            clicked = True
            game(False)

    # _________________________Labels_________________________>
    situation_lb = Label(text="Tic Tak Toe", background="#99C4C8", fg='#424242', font=('Elephant', 20, "normal"))
    situation_lb.place(x=200, y=20)

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

    play_btn = Button(text='Play again', bg="#CD3131", fg="#F6F6F6", command=lambda: game(again=True),
                      font=('Elephant', 12, "normal"), padx=15)
    play_btn.place(x=215, y=480)

    reset_btn = Button(text='Reset', bg="#CD3131", fg="#F6F6F6", command=reset_points, font=('Elephant', 8, "normal"))
    reset_btn.place(x=255, y=530)

    # Checkbutton
    def checkbutton_used():
        # Prints 1 if On button checked, otherwise 0.
        if checked_state.get() == 1:
            return True
        else:
            return False

    checked_state = IntVar()
    # variable to hold on to checked state, 0 is off, 1 is on.
    checkbutton = Checkbutton(text="Computer", bg='#99C4C8', fg="#CD3131", variable=checked_state,
                              command=checkbutton_used, font=('Elephant', 14, "normal"))
    checked_state.get()
    checkbutton.place(x=215, y=440)

    def radio_used():
        global level_one, level_two, level_three
        if radio_state.get() == 1:
            level_one = True
            level_two = False
            level_three = False
        elif radio_state.get() == 2:
            level_two = True
            level_one = False
            level_three = False
        elif radio_state.get() == 3:
            level_three = True
            level_two = False
            level_one = False
    # Variable to hold on to which radio button value is checked.
    radio_state = IntVar()

    radiobutton1 = Radiobutton(text="Level 1", value=1, variable=radio_state, command=radio_used,
                               bg='#99C4C8', fg="#424242")
    radiobutton2 = Radiobutton(text="Level 2", value=2, variable=radio_state, command=radio_used,
                               bg='#99C4C8', fg="#424242")
    radiobutton3 = Radiobutton(text="Level 3", value=3, variable=radio_state, command=radio_used,
                               bg='#99C4C8', fg="#424242")
    print(type(radiobutton3['variable']))
    radiobutton1.place(x=380, y=10)
    radiobutton2.place(x=380, y=30)
    radiobutton3.place(x=380, y=50)
    windows.mainloop()


game(again=False)
