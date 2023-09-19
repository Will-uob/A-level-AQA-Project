import os
from flask import Flask, render_template, request, send_from_directory
import requests
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'FILE' 

file_counter = 0

#Rendering of templates.
@app.route('/')
def home():
   return render_template('home.html', filecount=file_counter)

#Deal with the uploading of a file.
@app.route('/fileuploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
    return render_template('confirm.html')

#Deals with requests to go back home.
@app.route('/gohome', methods = ['POST'])
def gohome():
   if request.method == 'POST':
      pass
   return render_template('home.html', filecount=file_counter)

#Deals with requesting files from github.
@app.route('/upload-url', methods = ['GET', 'POST'])
def urlsubmit():
   if request.method == 'POST':
      pass
   elif request.method == 'GET':
      pass
   return render_template('confirm.html')

#Deals with the analysis request.
@app.route('/analysis', methods = ['POST'])
def analyse():
    return render_template('analysis.html')

if __name__ == '__main__':
   app.run()
