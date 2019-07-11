import numpy as np
import glob
import re
import os

txt_files = glob.glob("../results/*.txt")
vid_path = "../videos/buffered2"
list_dir = os.listdir(vid_path)
count = 0
for file in list_dir:
    if file.endswith(".mp4"):
        count += 1

def get_results():
    ret = []
    for file in txt_files:
        with open(file, "r") as fp:
            lines = fp.readlines()
            user_list = []
            for numbers in (lines[:4]):
                nums = re.split(r'[,\n]', numbers)[:-1]
                nums_arr = np.zeros(count, dtype=int)
                for i in range(count):
                    if nums[i] != '':
                        nums_arr[i] = int(nums[i])
                user_list.append(nums_arr)
            for rest in (lines[4:]):
                if rest[-1] == '\n':
                    user_list.append(rest[:-1])
                else:
                    user_list.append(rest)
            ret.append(user_list)
    return ret

