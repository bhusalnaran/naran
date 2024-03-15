
import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.instagram.com/naranbhusal127?igsh=MTlnZHdtYXRhZWh1cQ=="
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myinstagram.svg", scale = 8) 
