import numpy as np
from os import listdir
from os.path import isfile, isdir, join
import os
import json
import random
import shutil
import traceback

cwd = os.getcwd()
datadir = cwd.split('filelists')[0]
data_path = join(datadir,'Datasets/palm/images')
savedir = './'
dataset_list = ['base','val','novel']

#Reference Section 10
temp_folder_list = [f for f in listdir(data_path) if isdir(join(data_path, f))]
for i, folder in enumerate(temp_folder_list):
    folder_path = join(data_path, folder)
    file_names = [cf for cf in listdir(folder_path) if cf[0] != '.']
    for fname in file_names:
        if fname.endswith('.db'):
            os.remove(os.path.join(data_path,folder, fname))

    file_names = [cf for cf in listdir(folder_path) if cf[0] != '.']
    for fname in file_names:
        if '_r_' in fname:
            if not os.path.exists(os.path.join(data_path, folder + '_r')):
                os.mkdir(os.path.join(data_path, folder + '_r'))
            try:
                src = os.path.join(data_path,folder, fname)
                dst = os.path.join(data_path,folder + '_r',fname)
                if os.path.getsize(src) > 0:
                  shutil.move(src, dst)
            except Exception:
                print("error occured: ")
                traceback.print_exc()
