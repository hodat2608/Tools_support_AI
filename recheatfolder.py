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


source_folder_copy_folder = Test.getPath1()

def check_and_rename(destination_folder):
    original_name = destination_folder
    copy_count = 1
    while os.path.exists(destination_folder):
        destination_folder = f"{original_name}_copy_{copy_count}"
        copy_count += 1
    return destination_folder

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

def mode_folder_AAHAA(source_folder_copy_folder):
    os.mkdir(source_folder_copy_folder + 'AAHAA-H')
    dest_folder = source_folder_copy_folder+ 'AAHAA-H/'
    name = "AAHAA"
    for root, dirs, files in os.walk(source_folder_copy_folder):
        for folder_name in dirs:
            if name in folder_name:
                src_path = os.path.join(root, folder_name)
                dst_path = os.path.join(dest_folder, folder_name)
                dst_path = check_and_rename(dst_path)
                try:
                    shutil.move(src_path, dst_path)
                    print(f"Sao di chuyển thành công từ '{src_path}' tới '{dst_path}'.")
                except:
                    pass

def mode_folder_AAXAA(source_folder_copy_folder):
    os.mkdir(source_folder_copy_folder + 'AAXAA-H')
    dest_folder = source_folder_copy_folder+ 'AAXAA-H/'
    name = "AAXAA"
    for root, dirs, files in os.walk(source_folder_copy_folder):
        for folder_name in dirs:
            if name in folder_name:
                src_path = os.path.join(root, folder_name)
                dst_path = os.path.join(dest_folder, folder_name)
                dst_path = check_and_rename(dst_path)
                shutil.move(src_path, dst_path)
                print(f"Sao di chuyển thành công từ '{src_path}' tới '{dst_path}'.")

def mode_folder_ABNAA(source_folder_copy_folder):
    os.mkdir(source_folder_copy_folder + 'ABNAA-H')
    dest_folder = source_folder_copy_folder+ 'ABNAA-H/'
    name = "ABNAA"
    for root, dirs, files in os.walk(source_folder_copy_folder):
        for folder_name in dirs:
            if name in folder_name:
                src_path = os.path.join(root, folder_name)
                dst_path = os.path.join(dest_folder, folder_name)
                dst_path = check_and_rename(dst_path)
                try:
                    shutil.move(src_path, dst_path)
                    print(f"Sao di chuyển thành công từ '{src_path}' tới '{dst_path}'.")
                except:
                    pass

def mode_folder_AEPAA(source_folder_copy_folder):
    os.mkdir(source_folder_copy_folder + 'AEPAA-H')
    dest_folder = source_folder_copy_folder+ 'AEPAA-H/'
    name = "AEPAA"
    for root, dirs, files in os.walk(source_folder_copy_folder):
        for folder_name in dirs:
            if name in folder_name:
                src_path = os.path.join(root, folder_name)
                dst_path = os.path.join(dest_folder, folder_name)
                dst_path = check_and_rename(dst_path)
                try:
                    shutil.move(src_path, dst_path)
                    print(f"Sao di chuyển thành công từ '{src_path}' tới '{dst_path}'.")
                except:
                    pass

def mode_folder_AFMAA(source_folder_copy_folder):
    os.mkdir(source_folder_copy_folder + 'AFMAA-H')
    dest_folder = source_folder_copy_folder+ 'AFMAA-H/'
    name = "AFMAA"
    for root, dirs, files in os.walk(source_folder_copy_folder):
        for folder_name in dirs:
            if name in folder_name:
                src_path = os.path.join(root, folder_name)
                dst_path = os.path.join(dest_folder, folder_name)
                dst_path = check_and_rename(dst_path)
                try:
                    shutil.move(src_path, dst_path)
                    print(f"Sao di chuyển thành công từ '{src_path}' tới '{dst_path}'.")
                except:
                    pass

def mode_folder_AFWAA(source_folder_copy_folder):
    os.mkdir(source_folder_copy_folder + 'AFWAA-H')
    dest_folder = source_folder_copy_folder+ 'AFWAA-H/'
    name = "AFWAA"
    for root, dirs, files in os.walk(source_folder_copy_folder):
        for folder_name in dirs:
            if name in folder_name:
                src_path = os.path.join(root, folder_name)
                dst_path = os.path.join(dest_folder, folder_name)
                dst_path = check_and_rename(dst_path)
                try:
                    shutil.move(src_path, dst_path)
                    print(f"Sao di chuyển thành công từ '{src_path}' tới '{dst_path}'.")
                except:
                    pass

def mode_folder_AB8AA(source_folder_copy_folder):
    os.mkdir(source_folder_copy_folder + 'AB8AA-H')
    dest_folder = source_folder_copy_folder+ 'AB8AA-H/'
    name = "AB8AA"  
    for root, dirs, files in os.walk(source_folder_copy_folder):
        for folder_name in dirs:
            if name in folder_name:
                src_path = os.path.join(root, folder_name)
                dst_path = os.path.join(dest_folder, folder_name)
                dst_path = check_and_rename(dst_path)
                try:
                    shutil.move(src_path, dst_path)
                    print(f"Sao di chuyển thành công từ '{src_path}' tới '{dst_path}'.")
                except:
                    pass

def mode_folder_del_folder_ok(source_folder_copy_folder):
    name = "OK"
    for root, dirs, files in os.walk(source_folder_copy_folder):
        for folder_name in dirs:
            if name in folder_name:
                src_path = os.path.join(root, folder_name)
                try:
                    shutil.rmtree(src_path)
                    print(f"delete thành công folder ok từ '{src_path}' ")
                except:
                    pass


def copy_jpg_files_from_AAHAA(source_folder_copy_folder):
    src_folder_MAHANG = source_folder_copy_folder +'AAHAA-H/' 
    try:
        os.mkdir(src_folder_MAHANG + 'CAM1')
        os.mkdir(src_folder_MAHANG + 'CAM2') 
        os.mkdir(src_folder_MAHANG + 'CAM3')
    except:
        pass
    dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
    dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
    dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/'  
    target_folder_name_CAM1 = "Cam 1"
    target_folder_name_CAM2 = "Cam 2"
    target_folder_name_CAM3 = "Cam 3"
    for root, dirs, files in os.walk(src_folder_MAHANG):
        if target_folder_name_CAM1 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1.jpg')
                    except:
                        pass
        if target_folder_name_CAM2 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2.jpg')
                    except:
                        pass
        if target_folder_name_CAM3 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3.jpg')
                    except:
                        pass

def copy_jpg_files_from_AAXAA(source_folder_copy_folder):
    src_folder_MAHANG = source_folder_copy_folder +'AAXAA-H/' 
    try:
        os.mkdir(src_folder_MAHANG + 'CAM1')
        os.mkdir(src_folder_MAHANG + 'CAM2') 
        os.mkdir(src_folder_MAHANG + 'CAM3')
    except:
        pass
    dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
    dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
    dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/'  
    target_folder_name_CAM1 = "Cam 1"
    target_folder_name_CAM2 = "Cam 2"
    target_folder_name_CAM3 = "Cam 3"
    for root, dirs, files in os.walk(src_folder_MAHANG):
        if target_folder_name_CAM1 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1.jpg')
                    except:
                        pass
        if target_folder_name_CAM2 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input1_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2.jpg')
                    except:
                        pass
        if target_folder_name_CAM3 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3.jpg')
                    except:
                        pass

def copy_jpg_files_from_ABNAA(source_folder_copy_folder):
    src_folder_MAHANG = source_folder_copy_folder +'ABNAA-H/' 
    try:
        os.mkdir(src_folder_MAHANG + 'CAM1')
        os.mkdir(src_folder_MAHANG + 'CAM2') 
        os.mkdir(src_folder_MAHANG + 'CAM3')
    except:
        pass
    dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
    dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
    dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/'  
    target_folder_name_CAM1 = "Cam 1"
    target_folder_name_CAM2 = "Cam 2"
    target_folder_name_CAM3 = "Cam 3"
    for root, dirs, files in os.walk(src_folder_MAHANG):
        if target_folder_name_CAM1 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1.jpg')
                    except:
                        pass
        if target_folder_name_CAM2 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2.jpg')
                    except:
                        pass
        if target_folder_name_CAM3 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3.jpg')
                    except:
                        pass
            
def copy_jpg_files_from_AB8AA(source_folder_copy_folder):
    src_folder_MAHANG = source_folder_copy_folder +'AB8AA-H/' 
    try:
        os.mkdir(src_folder_MAHANG + 'CAM1')
        os.mkdir(src_folder_MAHANG + 'CAM2') 
        os.mkdir(src_folder_MAHANG + 'CAM3')
    except:
        pass
    dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
    dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
    dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/'  
    target_folder_name_CAM1 = "Cam 1"
    target_folder_name_CAM2 = "Cam 2"
    target_folder_name_CAM3 = "Cam 3"
    for root, dirs, files in os.walk(src_folder_MAHANG):
        if target_folder_name_CAM1 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1.jpg')
                    except:
                        pass
        if target_folder_name_CAM2 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2.jpg')
                    except:
                        pass
        if target_folder_name_CAM3 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3.jpg')
                    except:
                        pass

def copy_jpg_files_from_AEPAA(source_folder_copy_folder):
    src_folder_MAHANG = source_folder_copy_folder +'AEPAA-H/' 
    try:
        os.mkdir(src_folder_MAHANG + 'CAM1')
        os.mkdir(src_folder_MAHANG + 'CAM2') 
        os.mkdir(src_folder_MAHANG + 'CAM3')
    except:
        pass
    dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
    dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
    dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/'  
    target_folder_name_CAM1 = "Cam 1"
    target_folder_name_CAM2 = "Cam 2"
    target_folder_name_CAM3 = "Cam 3"
    for root, dirs, files in os.walk(src_folder_MAHANG):
        if target_folder_name_CAM1 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") :
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1.jpg')
                    except:
                        pass
        if target_folder_name_CAM2 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2.jpg')
                    except:
                        pass
        if target_folder_name_CAM3 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3.jpg')
                    except:
                        pass

def copy_jpg_files_from_AFMAA(source_folder_copy_folder):
    src_folder_MAHANG = source_folder_copy_folder +'AFMAA-H/' 
    try:
        os.mkdir(src_folder_MAHANG + 'CAM1')
        os.mkdir(src_folder_MAHANG + 'CAM2') 
        os.mkdir(src_folder_MAHANG + 'CAM3')
    except:
        pass
    dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
    dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
    dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/'  
    target_folder_name_CAM1 = "Cam 1"
    target_folder_name_CAM2 = "Cam 2"
    target_folder_name_CAM3 = "Cam 3"
    for root, dirs, files in os.walk(src_folder_MAHANG):
        if target_folder_name_CAM1 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1.jpg')
                    except:
                        pass
        if target_folder_name_CAM2 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2.jpg')
                    except:
                        pass
        if target_folder_name_CAM3 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3.jpg')
                    except:
                        pass
def copy_jpg_files_from_AFWAA(source_folder_copy_folder):
    src_folder_MAHANG = source_folder_copy_folder +'AFWAA-H/' 
    try:
        os.mkdir(src_folder_MAHANG + 'CAM1')
        os.mkdir(src_folder_MAHANG + 'CAM2') 
        os.mkdir(src_folder_MAHANG + 'CAM3')
    except:
        pass
    dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
    dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
    dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/'  
    target_folder_name_CAM1 = "Cam 1"
    target_folder_name_CAM2 = "Cam 2"
    target_folder_name_CAM3 = "Cam 3"
    for root, dirs, files in os.walk(src_folder_MAHANG):
        if target_folder_name_CAM1 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") :
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1.jpg')
                    except:
                        pass
        if target_folder_name_CAM2 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input1_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2.jpg')
                    except:
                        pass
        if target_folder_name_CAM3 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3.jpg')
                    except:
                        pass

def copy_jpg_files_from_AB8AA(source_folder_copy_folder):
    src_folder_MAHANG = source_folder_copy_folder +'AB8AA-H/'
    try:
        os.mkdir(src_folder_MAHANG + 'CAM1')
        os.mkdir(src_folder_MAHANG + 'CAM2') 
        os.mkdir(src_folder_MAHANG + 'CAM3')
    except:
        pass
    dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
    dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
    dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/' 
    target_folder_name_CAM1 = "Cam 1"
    target_folder_name_CAM2 = "Cam 2"
    target_folder_name_CAM3 = "Cam 3"
    for root, dirs, files in os.walk(src_folder_MAHANG):
        if target_folder_name_CAM1 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") :
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1-AB8AA.jpg')
                    except:
                        pass
        if target_folder_name_CAM2 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2-AB8AA.jpg')
                    except:
                        pass
        if target_folder_name_CAM3 in root:
            for file_name in files:
                if file_name.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file_name)
                    name_folder_ng = time_to_name()
                    try:
                        shutil.move(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3-AB8AA.jpg')
                    except:
                        pass

def rename_mahang_AAHAA(source_folder_copy_folder):
    path1 = source_folder_copy_folder + '/AAHAA-H/CAM1/'
    path2 = source_folder_copy_folder + '/AAHAA-H/CAM2/'
    path3 = source_folder_copy_folder + '/AAHAA-H/CAM3/'
    mahang = '-AAHAA'
    for filename in glob(path1+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path2+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path3+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')

def rename_mahang_AAXAA(source_folder_copy_folder):
    path1 = source_folder_copy_folder + '/AAXAA-H/CAM1/'
    path2 = source_folder_copy_folder + '/AAXAA-H/CAM2/'
    path3 = source_folder_copy_folder + '/AAXAA-H/CAM3/'
    mahang = '-AAXAA'
    for filename in glob(path1+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path2+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path3+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')

def rename_mahang_AB8AA(source_folder_copy_folder):
    path1 = source_folder_copy_folder + '/AB8AA-H/CAM1/'
    path2 = source_folder_copy_folder + '/AB8AA-H/CAM2/'
    path3 = source_folder_copy_folder + '/AB8AA-H/CAM3/'
    mahang = '-AB8AA'
    for filename in glob(path1+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path2+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path3+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')

def rename_mahang_ABNAA(source_folder_copy_folder):
    path1 = source_folder_copy_folder + '/ABNAA-H/CAM1/'
    path2 = source_folder_copy_folder + '/ABNAA-H/CAM2/'
    path3 = source_folder_copy_folder + '/ABNAA-H/CAM3/'
    mahang = '-ABNAA'
    for filename in glob(path1+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path2+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path3+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')  

def rename_mahang_AEPAA(source_folder_copy_folder):
    path1 = source_folder_copy_folder + '/AEPAA-H/CAM1/'
    path2 = source_folder_copy_folder + '/AEPAA-H/CAM2/'
    path3 = source_folder_copy_folder + '/AEPAA-H/CAM3/'
    mahang = '-AEPAA'
    for filename in glob(path1+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path2+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path3+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')  

def rename_mahang_AFMAA(source_folder_copy_folder):
    path1 = source_folder_copy_folder + '/AFMAA-H/CAM1/'
    path2 = source_folder_copy_folder + '/AFMAA-H/CAM2/'
    path3 = source_folder_copy_folder + '/AFMAA-H/CAM3/'
    mahang = '-AFMAA'
    for filename in glob(path1+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path2+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path3+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')  

def rename_mahang_AFWAA(source_folder_copy_folder):
    path1 = source_folder_copy_folder + '/AFWAA-H/CAM1/'
    path2 = source_folder_copy_folder + '/AFWAA-H/CAM2/'
    path3 = source_folder_copy_folder + '/AFWAA-H/CAM3/'
    mahang = '-AFWAA'
    for filename in glob(path1+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path2+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')
    for filename in glob(path3+'*.jpg'):
        os.rename(filename,filename[:-4]+mahang+'.jpg')  



# mode_folder_AAHAA(source_folder_copy_folder)
# mode_folder_AAXAA(source_folder_copy_folder)
# mode_folder_ABNAA(source_folder_copy_folder)
# mode_folder_AEPAA(source_folder_copy_folder)
# mode_folder_AFMAA(source_folder_copy_folder)
# mode_folder_AFWAA(source_folder_copy_folder)
# mode_folder_AB8AA(source_folder_copy_folder)
# mode_folder_del_folder_ok(source_folder_copy_folder)
# copy_jpg_files_from_AAHAA(source_folder_copy_folder)
# copy_jpg_files_from_AAXAA(source_folder_copy_folder)
# copy_jpg_files_from_ABNAA(source_folder_copy_folder)
copy_jpg_files_from_AB8AA(source_folder_copy_folder)
# copy_jpg_files_from_AEPAA(source_folder_copy_folder)
# copy_jpg_files_from_AFMAA(source_folder_copy_folder)
copy_jpg_files_from_AFWAA(source_folder_copy_folder)
# copy_jpg_files_from_AB8AA(source_folder_copy_folder)
# rename_mahang_AAHAA(source_folder_copy_folder)
# rename_mahang_AAXAA(source_folder_copy_folder)  
# rename_mahang_AB8AA(source_folder_copy_folder)    
# rename_mahang_ABNAA(source_folder_copy_folder)
# rename_mahang_AEPAA(source_folder_copy_folder)
# rename_mahang_AFWAA(source_folder_copy_folder)
# rename_mahang_AFMAA(source_folder_copy_folder)



# def HIEU(source_folder_copy_folder):
#     src_folder_MAHANG = source_folder_copy_folder
#     try:
#         os.mkdir(src_folder_MAHANG + 'CAM1')
#         os.mkdir(src_folder_MAHANG + 'CAM2') 
#         os.mkdir(src_folder_MAHANG + 'CAM3')
#         # os.mkdir(src_folder_MAHANG + 'CAM4')
#         os.mkdir(src_folder_MAHANG + 'CAM5') 
#         os.mkdir(src_folder_MAHANG + 'CAM6')
#         os.mkdir(src_folder_MAHANG + 'CAM7')
#     except:
#         pass
#     dest_folder_CAM1 = src_folder_MAHANG + 'CAM1/' 
#     dest_folder_CAM2 = src_folder_MAHANG + 'CAM2/' 
#     dest_folder_CAM3 = src_folder_MAHANG + 'CAM3/' 
#     # dest_folder_CAM4 = src_folder_MAHANG + 'CAM4/' 
#     dest_folder_CAM5 = src_folder_MAHANG + 'CAM5/' 
#     dest_folder_CAM6 = src_folder_MAHANG + 'CAM6/' 
#     dest_folder_CAM7 = src_folder_MAHANG + 'CAM7/' 
#     target_folder_name_CAM1 = "CAM1"
#     target_folder_name_CAM2 = "CAM2"
#     target_folder_name_CAM3 = "CAM3"
#     # target_folder_name_CAM4 = "CAM4"
#     target_folder_name_CAM5 = "CAM5"
#     target_folder_name_CAM6 = "CAM6"
#     target_folder_name_CAM7 = "CAM7"
#     for root, dirs, files in os.walk(src_folder_MAHANG):
#         if target_folder_name_CAM1 in root:
#             for file_name in files:
#                 if file_name.lower().endswith(".jpg") :
#                     src_path = os.path.join(root, file_name)
#                     name_folder_ng = time_to_name()
#                     try:
#                         shutil.copy(src_path, dest_folder_CAM1+ str(name_folder_ng)+'-C1-AB8AA.jpg')
#                     except:
#                         pass
#         if target_folder_name_CAM2 in root:
#             for file_name in files:
#                 if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
#                     src_path = os.path.join(root, file_name)
#                     name_folder_ng = time_to_name()
#                     try:
#                         shutil.copy(src_path, dest_folder_CAM2+ str(name_folder_ng)+'-C2-AB8AA.jpg')
#                     except:
#                         pass
#         if target_folder_name_CAM3 in root:
#             for file_name in files:
#                 if file_name.lower().endswith(".jpg"):
#                     src_path = os.path.join(root, file_name)
#                     name_folder_ng = time_to_name()
#                     try:
#                         shutil.copy(src_path, dest_folder_CAM3+ str(name_folder_ng)+'-C3-AB8AA.jpg')
#                     except:
#                         pass
#         # if target_folder_name_CAM4 in root:
#         #     for file_name in files:
#         #         if file_name.lower().endswith(".jpg") :
#         #             src_path = os.path.join(root, file_name)
#         #             name_folder_ng = time_to_name()
#         #             try:
#         #                 shutil.copy(src_path, dest_folder_CAM4+ str(name_folder_ng)+'-C4-AB8AA.jpg')
#         #             except:
#         #                 pass
#         if target_folder_name_CAM5 in root:
#             for file_name in files:
#                 if file_name.lower().endswith(".jpg") and file_name=='Input0_Camera0.jpg':
#                     src_path = os.path.join(root, file_name)
#                     name_folder_ng = time_to_name()
#                     try:
#                         shutil.copy(src_path, dest_folder_CAM5+ str(name_folder_ng)+'-C5-AB8AA.jpg')
#                     except:
#                         pass
#         if target_folder_name_CAM6 in root:
#             for file_name in files:
#                 if file_name.lower().endswith(".jpg"):
#                     src_path = os.path.join(root, file_name)
#                     name_folder_ng = time_to_name()
#                     try:
#                         shutil.copy(src_path, dest_folder_CAM6+ str(name_folder_ng)+'-C6-AB8AA.jpg')
#                     except:
#                         pass
#         if target_folder_name_CAM7 in root:
#             for file_name in files:
#                 if file_name.lower().endswith(".jpg"):
#                     src_path = os.path.join(root, file_name)
#                     name_folder_ng = time_to_name()
#                     try:
#                         shutil.copy(src_path, dest_folder_CAM7+ str(name_folder_ng)+'-C7-AB8AA.jpg')
#                     except:
#                         pass
        
# # HIEU(source_folder_copy_folder)