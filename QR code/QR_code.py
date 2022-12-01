import pyqrcode
my_page = pyqrcode.create("https://www.linkedin.com/in/simon-atiegar/")
my_page.png('linkedin.png', scale = 8)
my_page.show()