import cv2
import numpy as np
import os
from glob import glob

def proc_img(img_path):
    img = cv2.imread(img_path)
    truncated = img[:690]
    ## save img
    dirname = os.path.dirname(img_path)
    filename = os.path.basename(img_path)
    filename = filename.split('.')[0] + '_trunc.png'
    cv2.imwrite(os.path.join(dirname, filename), truncated)
    print('saved in ', os.path.join(dirname, filename))

if __name__ == '__main__':
    # img_path = 'data/main_p0/music/idx_0/impmap_levels.png'
    # proc_img(img_path)
    img_path_list = glob('data/**/impmap_levels.png', recursive=True)
    for img_path in img_path_list:
        proc_img(img_path)