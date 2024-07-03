from TOAN import Test
import os

TM = Test.getPath1()
os.makedirs(TM + 'c', exist_ok=True)
os.makedirs(TM + 'sat', exist_ok=True)
os.makedirs(TM + 'divat', exist_ok=True)
os.makedirs(TM + 'me', exist_ok=True)
os.makedirs(TM + 'lech_chan', exist_ok=True)
os.makedirs(TM + 'keo_tran', exist_ok=True)
os.makedirs(TM + 'chan_de', exist_ok=True)
os.makedirs(TM + 'chan_tu', exist_ok=True)
os.makedirs(TM + 'di_thuong', exist_ok=True)
os.makedirs(TM + 'tai_ok', exist_ok=True)
os.makedirs(TM + 'tu_dai', exist_ok=True)
os.makedirs(TM + 'me_giua', exist_ok=True)
os.makedirs(TM + 'me_cuoi', exist_ok=True)
os.makedirs(TM + 'mau_ok', exist_ok=True)
os.makedirs(TM + 'mau_ng', exist_ok=True)

print('done')
