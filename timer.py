from plyer import notification
import time

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # Để sử dụng icon mặc định, bạn có thể thay đổi đường dẫn tại đây
        timeout=10  # Thời gian hiển thị thông báo (đơn vị: giây)
    )

def main():
    # Lặp vô hạn để kiểm tra thời gian và hiển thị thông báo khi đến 4 giờ
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == 16 and current_time.tm_min == 00:
            show_notification("Thông báo", "Đã đến 4 giờ. XUỐNG XÓA ẢNH !")
            # Nếu bạn muốn thông báo liên tục, có thể sử dụng một vòng lặp nhỏ ở đây
            time.sleep(1)  # Ngủ 1 phút trước khi kiểm tra lại
        else:
            time.sleep(1)  # Ngủ 1 phút trước khi kiểm tra lại

if __name__ == "__main__":
    main()
