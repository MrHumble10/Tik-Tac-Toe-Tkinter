from main import *

def level_one():
    global random_btn
    btn_list = [btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]
    # ------------------------Row One-------------------------->
    if btn_3["text"] == 'X' and btn_2["text"] == 'X' and btn_1["text"] == ' ':
        random_btn = btn_list[0]
        level(1)
        conditions()
    elif btn_1["text"] == 'X' and btn_3["text"] == 'X' and btn_2["text"] == ' ':
        random_btn = btn_list[1]
        level(2)
        conditions()
    elif btn_1["text"] == 'X' and btn_2["text"] == 'X' and btn_3["text"] == ' ':
        random_btn = btn_list[2]
        level(3)
        conditions()
    # ------------------------Row two-------------------------->
    elif btn_6["text"] == 'X' and btn_5["text"] == 'X' and btn_4["text"] == ' ':
        random_btn = btn_list[3]
        level(4)
        conditions()
    elif btn_6["text"] == 'X' and btn_4["text"] == 'X' and btn_5["text"] == ' ':
        random_btn = btn_list[4]
        level(5)
        conditions()
    elif btn_4["text"] == 'X' and btn_5["text"] == 'X' and btn_6["text"] == ' ':
        random_btn = btn_list[5]
        level(6)
        conditions()
    # ------------------------Row Three-------------------------->
    elif btn_9["text"] == 'X' and btn_8["text"] == 'X' and btn_7["text"] == ' ':
        random_btn = btn_list[6]
        level(7)
        conditions()
    elif btn_9["text"] == 'X' and btn_7["text"] == 'X' and btn_8["text"] == ' ':
        random_btn = btn_list[7]
        level(8)
        conditions()
    elif btn_8["text"] == 'X' and btn_7["text"] == 'X' and btn_9["text"] == ' ':
        random_btn = btn_list[8]
        level(9)
        conditions()
    # ------------------------Column One-------------------------->
    elif btn_1["text"] == 'X' and btn_4["text"] == 'X' and btn_7["text"] == ' ':
        random_btn = btn_list[6]
        level(10)
        conditions()
    elif btn_1["text"] == 'X' and btn_7["text"] == 'X' and btn_4["text"] == ' ':
        random_btn = btn_list[3]
        level(11)
        conditions()
    elif btn_4["text"] == 'X' and btn_7["text"] == 'X' and btn_1["text"] == ' ':
        random_btn = btn_list[0]
        level(12)
        conditions()
    # ------------------------Column Two-------------------------->
    elif btn_2["text"] == 'X' and btn_5["text"] == 'X' and btn_8["text"] == ' ':
        random_btn = btn_list[7]
        level(13)
        conditions()
    elif btn_2["text"] == 'X' and btn_8["text"] == 'X' and btn_5["text"] == ' ':
        random_btn = btn_list[4]
        level(14)
        conditions()
    elif btn_5["text"] == 'X' and btn_8["text"] == 'X' and btn_2["text"] == ' ':
        random_btn = btn_list[1]
        level(15)
        conditions()
    # ------------------------Column Three-------------------------->
    elif btn_3["text"] == 'X' and btn_6["text"] == 'X' and btn_9["text"] == ' ':
        random_btn = btn_list[8]
        level(16)
        conditions()
    elif btn_3["text"] == 'X' and btn_9["text"] == 'X' and btn_6["text"] == ' ':
        random_btn = btn_list[5]
        level(17)
        conditions()
    elif btn_9["text"] == 'X' and btn_6["text"] == 'X' and btn_3["text"] == ' ':
        random_btn = btn_list[1]
        level(18)
        conditions()
    # ------------------------Column Three-------------------------->
    elif btn_1["text"] == 'X' and btn_5["text"] == 'X' and btn_9["text"] == ' ':
        random_btn = btn_list[8]
        level(19)
        conditions()
    elif btn_1["text"] == 'X' and btn_9["text"] == 'X' and btn_5["text"] == ' ':
        random_btn = btn_list[4]
        level(17)
        conditions()
    elif btn_9["text"] == 'X' and btn_5["text"] == 'X' and btn_1["text"] == ' ':
        random_btn = btn_list[0]
        level(18)
        conditions()
    random_btn = btn_list[random.randint(0, 8)]
    while not random_btn['text'] == " ":
        random_btn = btn_list[random.randint(0, 8)]
        print(f"first{btn_list[0]}")
