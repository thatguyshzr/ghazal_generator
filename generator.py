import joblib
from PIL import Image, ImageFont, ImageDraw
import random

def write(lines=2, min_len= 30, max_len= 40):
	# make_model()
	# update_model()
	model= joblib.load('model.pkl')
	ghazal= []
	count= 0
	while(count<=(lines-1)):    # to make sure we dont count 'None'
		x = model.make_sentence()
		if x!=None and len(x)>=min_len and len(x)<= max_len:
			ghazal.append(x)
			count+=1
            
	return ghazal


def to_image(sher):
	# font = ImageFont.truetype(<font-file>, <font-size>)
	font_name= random.choice(os.listdir("fonts"))

	img = Image.open('background.jpg')
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(r"fonts/{}".format(font_name), 75)
	# draw.text((x, y),"Sample Text",(r,g,b))
	for i,q in enumerate(sher, 1):
	    draw.text((50, (i*100) + 265), q,(255,255,255),font=font)
	img.save('sample-out.jpg')