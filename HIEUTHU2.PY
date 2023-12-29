import os
import shutil
from TOAN import Test
import concurrent.futures
from glob import glob
from tkinter.tix import Tree
import os, cv2, torch, time, datetime, shutil
import numpy as np 
import PySimpleGUI as sg
from PIL import Image, ImageTk
import traceback
import sqlite3  
from TOAN import Test

def time_to_name():
    current_time = datetime.datetime.now() 
    name_folder = str(current_time)
    name_folder = list(name_folder)
    for i in range(len(name_folder)):
        if name_folder[i] == ':':
            name_folder[i] = '-'
        if name_folder[i] == ' ':
            name_folder[i] ='_'
        if name_folder[i] == '.':
            name_folder[i] ='-'
    name_folder = ''.join(name_folder)
    return name_folder
source_folder_copy_folder = Test.getPath1()

def HIEU(source_folder_copy_folder):
    src_folder_MAHANG = source_folder_copy_folder
    try:
        os.mkdir(src_folder_MAHANG + 'CAM1')
        os.mkdir(src_folder_MAHANG + 'CAM2') 
        os.mkdir(src_folder_MAHANG + 'CAM3')
        # os.mkdir(src_folder_MAHANG + 'CAM4')
        os.mkdir(src_folder_MAHANG + 'CAM5') 
        os.mkdir(src_folder_MAHANG + 'CAM6')
        os.mkdir(src_folder_MAHANG + 'CAM7')
    except:
        pass
    dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
    dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
    dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/' 
    # dest_folder_CAM4 = src_folder_MAHANG + 'CAM4/' 
    dest_folder_CAM5 = src_folder_MAHANG + 'CAM5/' 
    dest_folder_CAM6 = src_folder_MAHANG + 'CAM6/' 
    dest_folder_CAM7 = src_folder_MAHANG + 'CAM7/' 
    target_folder_name_CAM1 = "CAM1"
    target_folder_name_CAM2 = "CAM2"
    target_folder_name_CAM3 = "CAM3"
    # target_folder_name_CAM4 = "CAM4"
    target_folder_name_CAM5 = "CAM5"
    target_folder_name_CAM6 = "CAM6"
    target_folder_name_CAM7 = "CAM7"
    for root, dirs, files in os.walk(src_folder_MAHANG):
        if target_folder_name_CAM1 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") :
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.copy(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1-AB8AA.jpg')
                    except:
                        pass
        if target_folder_name_CAM2 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.copy(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2-AB8AA.jpg')
                    except:
                        pass
        if target_folder_name_CAM3 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.copy(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3-AB8AA.jpg')
                    except:
                        pass
        # if target_folder_name_CAM4 in root:
        #     for file_name in files:
        #         if file_name.lower().endswith(".jpg") :
        #             src_path = os.path.join(root, file_name)
        #             name_folder_ng = time_to_name()
        #             try:
        #                 shutil.copy(src_path, dest_folder_CAM4+ str(name_folder_ng)+'-C4-AB8AA.jpg')
        #             except:
        #                 pass
        if target_folder_name_CAM5 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.copy(src_path, dest_folder_CAM5+ str(name_folder_ng)+'-C5-AB8AA.jpg')
                    except:
                        pass
        if target_folder_name_CAM6 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.copy(src_path, dest_folder_CAM6+ str(name_folder_ng)+'-C6-AB8AA.jpg')
                    except:
                        pass
        if target_folder_name_CAM7 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.copy(src_path, dest_folder_CAM7+ str(name_folder_ng)+'-C7-AB8AA.jpg')
                    except:
                        pass
        
HIEU(source_folder_copy_folder)