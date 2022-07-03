import pyqrcode
import png
link = "https://portal.abuad.edu.ng/PortalHome"
qr_code = pyqrcode.create(link)
qr_code.png("portal.png", scale=5)