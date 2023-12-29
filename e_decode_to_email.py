import html

import html

def encode_email(email):
    encoded_email = "".join(["&#{};".format(ord(char)) for char in email])
    return html.escape(encoded_email)

# Sử dụng hàm encode_email để mã hóa email
email = "thieunao2o@gmail.com"
encoded_email = encode_email(email)

print("Email sau khi mã hóa:", encoded_email)
