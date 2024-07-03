import socket
import time
def test_connection(ip, port,delay =1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip,port))
        print(f"Kết nối thành công tới {ip}:{port}")
        time.sleep(delay)
    except Exception as e:
        print(f"Không thể kết nối tới {ip}:{port}, lỗi: {e}")
    finally:
        sock.close()
ip_to_test = '10.7.11.114'
ip_to_test1 = '10.7.11.22'
port_to_test = 7680
while True:
    test_connection(ip_to_test, port_to_test)
    test_connection(ip_to_test1, port_to_test)
