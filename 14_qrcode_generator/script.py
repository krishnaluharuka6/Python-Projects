import qrcode as qr


img = qr.make("https://github.com/krishnaluharuka6")
img.save("My_github_qr.png")
