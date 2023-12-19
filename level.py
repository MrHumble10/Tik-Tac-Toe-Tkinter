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
    elif levels and btn_1["text"] == item and btn_3["text"] == item and btn_2["text"] == ' ':
        random_btn = btn_list[1]
        level()
        conditions()
    elif levels and btn_1["text"] == item and btn_2["text"] == item and btn_3["text"] == ' ':
        random_btn = btn_list[2]
        level()
        conditions()
    # ------------------------Row two-------------------------->
    elif levels and btn_6["text"] == item and btn_5["text"] == item and btn_4["text"] == ' ':
        random_btn = btn_list[3]
        level()
        conditions()
    elif levels and btn_6["text"] == item and btn_4["text"] == item and btn_5["text"] == ' ':
        random_btn = btn_list[4]
        level()
        conditions()
    elif levels and btn_4["text"] == item and btn_5["text"] == item and btn_6["text"] == ' ':
        random_btn = btn_list[5]
        level()
        conditions()
    # ------------------------Row Three-------------------------->
    elif levels and btn_9["text"] == item and btn_8["text"] == item and btn_7["text"] == ' ':
        random_btn = btn_list[6]
        level()
        conditions()
    elif levels and btn_9["text"] == item and btn_7["text"] == item and btn_8["text"] == ' ':
        random_btn = btn_list[7]
        level()
        conditions()
    elif levels and btn_8["text"] == item and btn_7["text"] == item and btn_9["text"] == ' ':
        random_btn = btn_list[8]
        level()
        conditions()
    # ------------------------Column One-------------------------->
    elif levels and btn_1["text"] == item and btn_4["text"] == item and btn_7["text"] == ' ':
        random_btn = btn_list[6]
        level()
        conditions()
    elif levels and btn_1["text"] == 'O' and btn_7["text"] == item and btn_4["text"] == ' ':
        random_btn = btn_list[3]
        level()
        conditions()
    elif levels and btn_4["text"] == item and btn_7["text"] == item and btn_1["text"] == ' ':
        random_btn = btn_list[0]
        level()
        conditions()
    # ------------------------Column Two-------------------------->
    elif levels and btn_2["text"] == item and btn_5["text"] == item and btn_8["text"] == ' ':
        random_btn = btn_list[7]
        level()
        conditions()
    elif levels and btn_2["text"] == item and btn_8["text"] == item and btn_5["text"] == ' ':
        random_btn = btn_list[4]
        level()
        conditions()
    elif levels and btn_5["text"] == item and btn_8["text"] == item and btn_2["text"] == ' ':
        random_btn = btn_list[1]
        level()
        conditions()
    # ------------------------Column Three-------------------------->
    elif levels and btn_3["text"] == item and btn_6["text"] == item and btn_9["text"] == ' ':
        random_btn = btn_list[8]
        level()
        conditions()
    elif levels and btn_3["text"] == item and btn_9["text"] == item and btn_6["text"] == ' ':
        random_btn = btn_list[5]
        level()
        conditions()
    elif levels and btn_9["text"] == item and btn_6["text"] == item and btn_3["text"] == ' ':
        random_btn = btn_list[2]
        level()
        conditions()
    # ------------------------Column -------------------------->
    elif levels and btn_1["text"] == item and btn_5["text"] == item and btn_9["text"] == ' ':
        random_btn = btn_list[8]
        level()
        conditions()
    elif levels and btn_1["text"] == item and btn_9["text"] == item and btn_5["text"] == ' ':
        random_btn = btn_list[4]
        level()
        conditions()
    elif levels and btn_9["text"] == item and btn_5["text"] == item and btn_1["text"] == ' ':
        random_btn = btn_list[0]
        level()
        conditions()
    # ------------------------Column -------------------------->
    elif levels and btn_3["text"] == item and btn_5["text"] == item and btn_7["text"] == ' ':
        random_btn = btn_list[6]
        level()
        conditions()
    elif levels and btn_3["text"] == item and btn_7["text"] == item and btn_5["text"] == ' ':
        random_btn = btn_list[4]
        level()
        conditions()
    elif levels and btn_7["text"] == item and btn_5["text"] == item and btn_3["text"] == ' ':
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