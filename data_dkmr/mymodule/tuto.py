import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from game_check import out_check
    from action import confirm_all
    from clean_screen import skip, clean_screen_go

    try:
        print("tuto_start")


        result_complete_check = complete_check(cla)
        if result_complete_check == False:
            result_out = out_check(cla)
            if result_out == True:
                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\out_quest_auto.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 100, 960, 150, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:

                    chacyong_check(cla)

                    full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\sub_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 120, 750, 200, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\move_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 80, 910, 125, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(825, 105, cla)

                    time.sleep(1)

                    result_confirm = confirm_all(cla)

                    if result_confirm == True:
                        for i in range(30):
                            full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\complete_btn_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(855, 80, 905, 200, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("complete_btn_1", imgs_)
                                break
                            else:
                                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\talk_quest.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("talk_quest", imgs_)
                                    break
                            QTest.qWait(1000)


                else:
                    click_pos_2(930, 105, cla)
            else:
                clean_screen_go(cla)

        skip(cla)

        way_click(cla)


    except Exception as e:
        print(e)
        return 0


def complete_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("complete_check")

        is_data = True

        is_data_count = 0

        while is_data is True:

            is_data_count += 1
            if is_data_count > 3:
                break

            else:
                is_data = False

                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\complete_btn_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(855, 80, 905, 200, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("complete_btn_1", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y, cla)
                    is_data = True
                    QTest.qWait(500)

                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\complete_btn_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 670, 610, 700, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("complete_btn_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_data = True
                    is_data_count = 0
                    QTest.qWait(500)

                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\complete_btn_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 380, 530, 430, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("complete_btn_3", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_data = True
                    is_data_count = 0
                    QTest.qWait(500)

            QTest.qWait(1000)

        return is_data

    except Exception as e:
        print(e)
        return 0



def way_click(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("way_click")

        is_data = True
        is_data_count = 0

        while is_data is True:

            is_data_count += 1
            if is_data_count > 3:
                break
            else:

                is_data = False

                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\way\\up_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("up_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y - 40, cla)
                    is_data = True
                    is_data_count = 0
                    QTest.qWait(500)
                else:
                    full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\way\\up_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("up_2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y - 40, cla)
                        is_data = True
                        is_data_count = 0
                        QTest.qWait(500)


                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\way\\down_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("down_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y + 35, cla)
                    QTest.qWait(500)
                    click_pos_reg(imgs_.x, imgs_.y + 45, cla)
                    is_data = True
                    is_data_count = 0
                    QTest.qWait(500)
                else:
                    full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\way\\down_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("down_2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y + 35, cla)
                        QTest.qWait(500)
                        click_pos_reg(imgs_.x, imgs_.y + 45, cla)
                        is_data = True
                        is_data_count = 0
                        QTest.qWait(500)


                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\way\\left_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("left_1", imgs_)
                    click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                    QTest.qWait(500)
                    click_pos_reg(imgs_.x - 45, imgs_.y, cla)
                    is_data = True
                    is_data_count = 0
                    QTest.qWait(500)
                else:
                    full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\way\\left_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("left_1", imgs_)
                        click_pos_reg(imgs_.x - 30, imgs_.y, cla)
                        QTest.qWait(500)
                        click_pos_reg(imgs_.x - 45, imgs_.y, cla)
                        is_data = True
                        is_data_count = 0
                        QTest.qWait(500)



                full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\way\\right_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("right_1", imgs_)
                    click_pos_reg(imgs_.x + 45, imgs_.y, cla)
                    is_data = True
                    is_data_count = 0
                    QTest.qWait(500)
                else:
                    full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\way\\right_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("right_2", imgs_)
                        click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                        QTest.qWait(500)
                        click_pos_reg(imgs_.x + 100, imgs_.y, cla)
                        is_data = True
                        is_data_count = 0
                        QTest.qWait(500)

            QTest.qWait(1000)

        return is_data

    except Exception as e:
        print(e)
        return 0


def chacyong_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("chacyong_check")

        full_path = "c:\\my_games\\dkmr\\data_dkmr\\imgs\\tuto\\chacyong_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("chacyong_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            QTest.qWait(500)

    except Exception as e:
        print(e)
        return 0


