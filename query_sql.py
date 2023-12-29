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

# cursor = conn.cursor()
# cursor.execute('SELECT * FROM TEST_1 ')
# rows = cursor.fetchall()
# kq1=[]
# for column in cursor.description:
#     kq1.append((column[0]))
# print(kq1)
# for x in rows: 
#     if x[3] == 12727:
#         print('NAME',':', x[0])
#         print('AGE' , ':',x[1])
#         print('ADD' ,':', x[2])
#         print('MASV' , ':',x[3])
#         print('GIOITINH' ,':', x[4])
#         print('IDS' , ':', x[5])
#         print('Date Resgister' , ':', x[6])
#         print('-' * 80)
#         current_time = datetime.now()
#         #conn.execute('UPDATE TEST_1 SET time_end=?  WHERE ids = ? ',(current_time, x[5]))
#         conn.commit()
# cursor.close    

cursor = conn.cursor()

for i in range(0,1000):
    id = i 
    if id > 0:
        cursor.execute("DELETE FROM TEST_1 WHERE ids=?", (id,))
        conn.commit()

# Đóng kết nối
conn.close()


