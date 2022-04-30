import qrcode
import string   
import secrets 

path="Qrcode"
res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.ascii_uppercase + string.ascii_lowercase) for x in range(30))  
  

qr = qrcode.QRCode(version = 1,
				box_size = 10,
				border = 5)


qr.add_data(res)

qr.make(fit = True)
img = qr.make_image()
img.show('MyQRCode2.png')



for i in range(1,50): 
     with open('Data/data.txt', 'w') as file:
        
         books = [res]
        
         file.writelines("% s" % data for data in books)