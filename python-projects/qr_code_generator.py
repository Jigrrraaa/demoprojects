import qrcode

data = input("Enter the text or URL :")
file_name = input("Enter the filename")

img = qrcode.make(data)
type(img)
img.save(f'{file_name}.png')
