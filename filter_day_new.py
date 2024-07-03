
import threading
import time
import datetime
import glob
import os
import mysql.connector
import pandas as pd

path = 'V:/server_test/server_1/combine_client_excel/10.7.11.24/*.xlsx'
def filter_day_new_continous(path):
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        previous_date = current_date - datetime.timedelta(days=1) 
        now = datetime.datetime.now()
        hour = int(now.strftime("%H"))
        current_date = current_datetime.date()
        next_date = current_date + datetime.timedelta(days=1)
        ca_sang_start_datetime = datetime.datetime.combine(current_date, datetime.time(7, 0))
        ca_sang_end_datetime = datetime.datetime.combine(current_date, datetime.time(19, 0))
        ca_toi_start_datetime = datetime.datetime.combine(current_date, datetime.time(19, 0))
        ca_toi_end_datetime = datetime.datetime.combine(next_date, datetime.time(7, 0))
        previous_date_start_catoi = ca_toi_start_datetime - datetime.timedelta(days=1) 
        previous_date_end_catoi = ca_toi_end_datetime - datetime.timedelta(days=1) 
        
        if current_datetime >= ca_sang_start_datetime and current_datetime <= ca_sang_end_datetime:
            filenames = glob.glob(path)
            for filename in filenames:
                base_name = os.path.basename(filename)
                date_str = base_name.split('_')[0:3]
                print(date_str)
                shift_str = base_name.split('_')[3:4][0].split('.')[0]
                print(shift_str)
                date_str = '_'.join(date_str)
                file_date = datetime.datetime.strptime(date_str, '%Y_%m_%d').date()     
                if file_date == current_date and shift_str == 'Ngay' :              
                    return filename    
               
        if current_datetime >= previous_date_start_catoi and current_datetime <= previous_date_end_catoi:
            filenames = glob.glob(path)
            for filename in filenames:
                base_name = os.path.basename(filename)
                date_str = base_name.split('_')[0:3]
                shift_str = base_name.split('_')[3:4]
                date_str = '_'.join(date_str)
                file_date = datetime.datetime.strptime(date_str, '%Y_%m_%d').date()     
                if file_date == current_date and shift_str[0] == 'Dem':  
                    return filename
                if 0 <= hour <= 7:
                    if file_date == previous_date and shift_str[0] == 'Dem' :
                        return filename
                    
print(filter_day_new_continous(path))