import os
import math
import random
import matplotlib.pyplot as plt 
import numpy as np    
from PIL import Image

def slope(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    return m

def find_second_point(slope,x0,y0):
    # this function returns a point which belongs to the line that has the slope 
    # inserted by the user and that intercepts the point (x0,y0) inserted by the user
    q = y0 - (slope*x0)  # calculate q
    new_x = x0 + 10  # generate random x adding 10 to the intersect x coordinate
    new_y = (slope*new_x) + q  # calculate new y corresponding to random new_x created

    return new_x, new_y

def print_line(my_slope):
		x = np.arange(10)
		plt.plot(x,my_slope*x)
		print(math.degrees(math.atan(my_slope)))
		return
	

if __name__ == '__main__':



	#get coordinates from xml
		# x1 = float(input())
		# y1 = float(input())
		# x2 = float(input())
		# y2 = float(input())


		slp = slope(x1, y1, x2 , y2);
		slp = float(input())

		#alpha is the value that needs to be calculated
		alpha = 20 + random.uniform(0, 5)




		angle_with_horizontal = math.degrees(math.atan(slp))
		print_line(slp)

		
		filename = os.path.dirname(os.path.realpath(__file__)) + "/imgs/96.jpg"

		with Image.open(filename) as im:
			if(angle_with_horizontal > 0 ):
				anglw_to_rotate = -angle_with_horizontal + alpha
			else :
				anglw_to_rotate = -angle_with_horizontal - alpha
			im = im.rotate(anglw_to_rotate)
			im.save(os.path.join( os.path.dirname(os.path.realpath(__file__)) + "/rotated_img/rotated_96.jpeg",  ))
			im.show()


		angle_with_horizontal -= angle_with_horizontal
		angle_with_horizontal += alpha
		my_slope = math.tan(angle_with_horizontal/180 * 3.142)
		print_line(my_slope)
	