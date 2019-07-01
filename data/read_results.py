import numpy as np
import glob
import re

indices = [0, 1, 2, 3, 4]

txt_files = glob.glob("../results/*.txt")


def get_results():
    ret = []
    for file in txt_files:
        with open(file, "r") as fp:
            lines = fp.readlines()
            user_list = []
            for numbers in (lines[:4]):
                nums = re.split(r'[,\n]', numbers)[:-1]
                nums_arr = np.zeros(5, dtype=int)
                for i in indices:
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

