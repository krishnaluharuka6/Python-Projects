import qrcode as qr
from PIL import Image


qr_code = qr.QRCode(version=1,
                    error_correction=qr.constants.ERROR_CORRECT_H,
                    box_size=10, border=4,)

qr_code.add_data("https://krishnaluharuka6.github.io/Portfolio-website/")

qr_code.make(fit=True)

img = qr_code.make_image(fill_color = "rgb(14, 54, 83)", back_color = "rgb(227, 242, 253)")

img.save("portfolio_qrcode.png")

