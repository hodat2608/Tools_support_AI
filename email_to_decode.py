import html
def decode_email(encoded_email):
    parts = encoded_email.split(";")[:-1]  # Loại bỏ ký tự ';' cuối cùng
    decoded_email = "".join([html.unescape("&#{};".format(part[2:])) for part in parts])
    return decoded_email

# Sử dụng hàm decode_email để giải mã email
encoded_email = "&#116;&#104;&#105;&#101;&#117;&#110;&#97;&#111;&#50;&#111;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;"
decoded_email = decode_email(encoded_email)
print("Email sau khi giải mã:", decoded_email)
