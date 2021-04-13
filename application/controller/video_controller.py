from application import app
from flask import render_template, request

@app.route('/video/1')
def video():
   return render_template('video.html')

@app.route('/video/2')
def videoDois():
   return render_template('videodois.html')

@app.route('/video/3')
def videoTres():
   return render_template('videotres.html')