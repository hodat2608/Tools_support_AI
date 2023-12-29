import sqlite3
from datetime import date
from datetime import datetime

conn = sqlite3.connect('Test_sql/test_1.db')
#current_time = date.today()
from datetime import datetime


birth_date  = datetime.date
conn.execute("INSERT INTO TEST_1 (NAME, AGE, ADDRESS , MASV , GIOITINH , time_start) VALUES (?,?,?,?,?,?)",
            ('Ho Minh Tien', 22, 'quang ngai', 1811505,'nam', birth_date ))
conn.commit() 