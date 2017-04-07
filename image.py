#im = Image.open("petridish.jpg")
#col,row =  im.size
#data = np.zeros((row*col, 5))
#pixels = im.load()
#for i in range(row):
 #   for j in range(col):
  #      r,g,b =  pixels[i,j]
   #     data[i*col + j,:] = r,g,b,i,j


#m.show()

# library to import a jpg file into RGB values as a list
from PIL import Image
#import numpy as np

# opens the selected file
im = Image.open("petridish.jpg", 'r')
width, height = im.size #produces the wigth and height of the picture
pixel_values = list(im.getdata()) #produces a list of all the pixels in the image

# first loop goes through each pixel
results = []
row_counter = 0
lst_rows = []
row_element = []
row_index = 0
for i in range(len(pixel_values) - 1): 
	if row_index == width:
		results.append([row_element])
		row_element = [pixel_values[i]]
		row_index = 0
	else:
		row_element = row_element + [pixel_values[i]]
		row_index += 1
		
print(results[1])

# now there is a list that represents each element as a row of pix

#for i in range(width):
	#if width[i] == #black elements go to next line















