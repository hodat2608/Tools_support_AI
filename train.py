import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import subprocess

def run_training():
    command = ["python", "C:/yolov5/htdtrain.py", "--img", "640", "--batch", "10", "--epochs", "300", "--data", "C:/yolov5/data.yaml", "--weights", "", "--cfg", "C:/yolov5/models/training.yaml"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    for line in iter(process.stdout.readline, ''):
        console_text.insert(tk.END, line)
    for line in iter(process.stderr.readline, ''):
        console_text.insert(tk.END, line)
    process.stdout.close()
    process.stderr.close()
    process.wait()

# Tạo cửa sổ gốc
root = tk.Tk()
root.title("YOLOv5 Training Console")

# Tạo các widget
console_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
console_text.pack(fill=tk.BOTH, expand=True)

# Tạo một tiến trình con để chạy lệnh training
training_thread = Thread(target=run_training)
training_thread.start()

root.mainloop()