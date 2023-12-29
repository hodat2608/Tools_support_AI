# import sqlite3
# from datetime import datetime
# conn = sqlite3.connect('Test_sql/test_1.db')
# dataset = conn.execute('SELECT * FROM TEST_1')        
# for row in dataset:
#     name = row[0]
#     age = row[1]
#     add = row[2]
#     masv = row[3]
#     gioitinh = row[4]
#     ids = row[5]
#     current_time = datetime.now()
#     conn.execute('UPDATE TEST_1 SET time_start=?  WHERE ids = ? ',(current_time, ids))
#     conn.commit()

# print(current_time,ids)
import sqlite3,keyboard
from datetime import datetime
conn = sqlite3.connect('Test_sql/test_1.db')
#while True:
cursor = conn.cursor()
cursor.execute('SELECT * FROM TEST_1 ')
rows = cursor.fetchall()
for x in rows: 
    if x[5] ==19:
        print('NAME',':', x[0])
        print('AGE' , ':',x[1])
        print('ADD' ,':', x[2])
        print('MASV' , ':',x[3])
        print('GIOITINH' ,':', x[4])
        print('IDS' , ':', x[5])
        print('Date Resgister' , ':', x[6])
        print('-' * 80)
    current_time = datetime.now()
    #
    conn.commit()
cursor.close    
            
    # if keyboard.is_pressed("q"):
    #     print("Exit")
    #     break

