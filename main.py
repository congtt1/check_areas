import cv2
import numpy as np
from libs.task.read_data import DataTask
from libs.task.check_area import InstrusionTask
import csv
if __name__ == '__main__':

    list_cam = ['cam01', 'cam02']
    data_task1 = DataTask('cam01')
    data_task2 = DataTask('cam02')

    instrusion_task1 = InstrusionTask('cam01')
    instrusion_task2 = InstrusionTask('cam02')
    is_runing = True

    while(is_runing):
        ret1 , frame1 = data_task1.read_frame()
        ret2, frame2 = data_task2.read_frame()
        if not (ret1 or ret2):
            is_runing = False
        print(frame1.shape,'aaaaaaaa')
        print(frame2.shape,'bbbbbbbb')
