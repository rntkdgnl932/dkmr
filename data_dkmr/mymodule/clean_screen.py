import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def clean_screen_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from game_check import out_check

    try:
        print("clean_screen_start")


        result_out = out_check(cla)

        if result_out == False:

            result_out = False
            is_data_count = 0

            while result_out is False:


                result_out = out_check(cla)

                if result_out == False:
                    clean_screen_go(cla)

                    is_data_count += 1
                    if is_data_count > 7:
                        result_out = True


                QTest.qWait(1000)




    except Exception as e:
        print(e)
        return 0


def clean_screen_go(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from game_check import out_check

    try:
        print("clean_screen_go")

        full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\clean_screen\\close_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_for(0, 0, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("clean_screen close_1 : ", imgs_)
            if len(imgs_) > 0:
                for i in range(len(imgs_)):
                    click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                    time.sleep(0.5)

        full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\clean_screen\\close_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_for(0, 0, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("clean_screen close_1 : ", imgs_)
            if len(imgs_) > 0:
                for i in range(len(imgs_)):
                    click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                    time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0



def skip(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from game_check import out_check

    try:
        print("skip")

        is_data = True

        while is_data is True:

            is_data = False

            full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\clean_screen\\skip\\space_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("space_btn", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_data = True
                QTest.qWait(500)

            full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\clean_screen\\skip\\skip_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("skip_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_data = True
                QTest.qWait(500)

            QTest.qWait(1000)

        return is_data

    except Exception as e:
        print(e)
        return 0






