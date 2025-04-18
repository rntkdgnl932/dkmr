import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def out_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("out_check")


        is_data = False

        full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\check\\out\\out_jangbi.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 950, 100, 1000, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("out_jangbi", imgs_)
                

            is_data = True


        if is_data == True:
            full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\clean_screen\\close_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("out_check : close_1", imgs_)
                is_data = False
            else:
                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\clean_screen\\close_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("out_check : close_2", imgs_)
                    is_data = False
                else:
                    full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\action\\menu_open\\menu_friend.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 970, 780, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("out_check : menu_friend", imgs_)
                        is_data = False

        return is_data

    except Exception as e:
        print(e)
        return 0


def tuto_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("tuto_start")

        full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\18\\18_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("18_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0
