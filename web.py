from flask import Flask, render_template
# from model import write
from generator import write

app= Flask(__name__)

@app.route('/')
def index():
	return render_template('exp.html',
		ghazal= write(2))


if __name__== '__main__':
	app.debug= True
	app.run(port= 5000)