# import qrcode

# data = "https://www.youtube.com/watch?v=uSpsBgYn-uM"
# qr = qrcode.QRCode(
#   version=15,
#   box_size=10,
#   border=5
# )
# qr.add_data(data)
# qr.make(fit=True)
# img = qr.make_image(fill="black", back_color="white")
# img.save("test.png")


import qrcode

# Replace with the phone number you want to encode
phone_number = "tel:6469447568"
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
qr.add_data(phone_number)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("phone_qr.png")