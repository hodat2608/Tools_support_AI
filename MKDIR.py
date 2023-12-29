from TOAN import Test
import os

TM = Test.getPath1()
os.makedirs(TM + 'buichi', exist_ok=True)
os.makedirs(TM + 'divat', exist_ok=True)
os.makedirs(TM + 'hangng', exist_ok=True)
os.makedirs(TM + 'hangok', exist_ok=True)
os.makedirs(TM + 'vunchi', exist_ok=True)
print('done')