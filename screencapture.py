import pyscreenshot as ImageGrab
from PIL import Image
import os
import time
import pytesseract

center_box = (347,501,369,523)

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
def screenGrab():
	#box holds the 4 parameters of the bounding box of the screenshot
#    box = (194+1, 394+1, 522, 676)
#    im = ImageGrab.grab()
#    
#    im.save(os.getcwd() + '\\recognize.png', 'PNG')
	im = Image.open('colortest.png')
	# R, G, B = im.convert('RGB').split()
	# r = R.load()
	# g = G.load()
	# b = B.load()
	# w, h = im.size

	# # Convert non-black pixels to white
	# for i in range(w):
	#     for j in range(h):
	#         if(r[i, j] != 0 or g[i, j] != 0 or b[i, j] != 0):
	#             r[i, j] = 255 # Just change R channel

	# # Merge just the R channel as all channels
	# im = Image.merge('RGB', (R, R, R))
	text = pytesseract.image_to_string(im)
	im.save(os.getcwd() + '\\export.png', 'PNG')
	print("text recognized is : " + str(text))

if __name__ == '__main__':
	screenGrab()