import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def menu_open(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from game_check import out_check

    try:
        print("menu_open")


        is_data = False
        is_data_count = 0

        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True

            full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\action\\menu_open\\menu_friend.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 970, 780, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("menu_friend", imgs_)
                # click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(930, 60, cla)
                else:
                    print("clean")

            QTest.qWait(1000)



    except Exception as e:
        print(e)
        return 0


def confirm_all(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from game_check import out_check

    try:
        print("confirm_all")

        is_data = False

        full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\soolock_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 670, 610, 700, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("soolock_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_data = True
            QTest.qWait(500)

        full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 580, 610, 700, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_data = True
            QTest.qWait(500)

        return is_data

    except Exception as e:
        print(e)
        return 0



def cancle_all(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from game_check import out_check

    try:
        print("cancle_all")

        full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\action\\cancle\\cancle_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 570, 480, 700, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("cancle_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            QTest.qWait(500)

    except Exception as e:
        print(e)
        return 0