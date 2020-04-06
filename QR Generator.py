import pyqrcode
from pyqrcode import QRCode
# String which represent the QR code
u = input("Enter URL: ")
# Generate QR code
url = pyqrcode.create(u)
# Create and save the png file naming "QR.svg"
url.svg("QR.svg", scale = 8)
