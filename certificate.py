# imports 
from PIL import Image, ImageDraw, ImageFont 

def coupons(names: list, certificate: str, font_path: str): 
	for name in names: 
		# adjust the position according to 
		# your sample 
		text_y_position = 880
		# opens the image 
		img = Image.open(certificate, mode ='r') 
		# gets the image width 
		image_width = img.width 
		# gets the image height 
		image_height = img.height 
		# creates a drawing canvas overlay 
		# on top of the image 
		draw = ImageDraw.Draw(img) 
		# gets the font object from the 
		# font file (TTF) 
		font = ImageFont.truetype( 
			font_path, 
			200 # change this according to your needs 
		) 
		# fetches the text width for 
		# calculations later on 
		text_width, _ = draw.textsize(name, font = font) 
		draw.text( 
			( 
				# this calculation is done 
				# to centre the image 
				(image_width - text_width) / 2, 
				text_y_position 
			), 
			name, 
			font = font	 ) 
		# saves the image in png format
		img= img.save("{}.png".format(name))
        
# Driver Code 
if __name__ == "__main__": 
	# some example of names 
	NAMES = ['Frank Muller', 
			'Mathew Frankfurt', 
			'Cristopher Greman', 
			'Natelie Wemberg', 
			'John Ken'] 
	# path to font 
	FONT = "E:\Practise\Python\certificate\doc\AGENCYR.TTF"
	# path to sample certificate 
	CERTIFICATE = "E:\Practise\Python\certificate\doc\CYBERNIX.jpg"
	coupons(NAMES, CERTIFICATE, FONT) 
