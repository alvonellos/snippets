import Image, ImageDraw
import gc
from random import randint as rint

def rand_image(sizex, sizey, fname):
	im = Image.new('RGB', (sizex, sizey), 'white')
	draw = ImageDraw.Draw(im)

	bufx = []
	for i in xrange(sizex*sizey):
		p = rint(0, 255), rint(0, 255), rint(0, 255)
		bufx.append(p)
	
	im.putdata(bufx)
	im.save(fname + '.png')

if __name__ == "__main__":
	for i in xrange(2):
		print "doing %s" % str(i)
		rand_image(4000,4000, str(i))
			
