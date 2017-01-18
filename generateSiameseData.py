import os
from PIL import Image
from random import choice

def getClassName(name):
	return name.split('_')[1]	

def areSameClass(im1, im2):
	return getClassName(im1) == getClassName(im2)

def setClassName(im1, im2):
	return "Similar.png" if areSameClass(im1, im2) else "Different.png"

def chooseTwoImages(seq):
	return choice(seq), choice(seq)


if __name__ == '__main__':

	input_path = 'train/'
	output_path = 'siamese_train/'
	files = os.listdir(input_path)
	count = 0
	N = 50000

	for dataPoint in range(N):
		im1, im2 = chooseTwoImages(files)

		images = map(Image.open, [input_path+im1, input_path+im2])
		
		widths, heights = zip(*(i.size for i in images))	

		total_width = sum(widths)
		max_height = max(heights)

		new_im = Image.new('RGB', (total_width, max_height))

		x_offset = 0
		for im in images:
		  new_im.paste(im, (x_offset,0))
		  x_offset += im.size[0]

		new_im.save(output_path + str(count) + '_' + setClassName(im1, im2))

		count += 1