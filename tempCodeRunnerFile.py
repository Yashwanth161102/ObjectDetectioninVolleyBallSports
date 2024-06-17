from flask import Flask, request, redirect, url_for, send_from_directory, render_template
import os
import cv2
import subprocess
app = Flask(__name__)

# Configure upload and processed directories
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'Output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Ensure upload and processed directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/volley',methods=['POST','GET'])
def send():
    return render_template('volley.html', flag = False)

@app.route('/volley1',methods=['POST','GET'])
def send1():
    return render_template('volley1.html', flag = False)

@app.route('/volley2',methods=['POST','GET'])
def send2():
    return render_template('volley2.html', flag = False)


@app.route('/upload', methods=['POST','GET'])
def upload_file():
    if 'video' not in request.files:
        return redirect(request.url)
    file = request.files['video']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        if file.filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], "original.jpg")
            file.save(filepath)
            processed_filepath = balltrack01(filepath)
            return redirect(url_for('download_file', filename=os.path.basename(processed_filepath)))
        else :
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], "original.mp4")
            file.save(filepath)
            processed_filepath = balltrack0(filepath)
            return render_template('volley.html', flag = True)
    
def balltrack0(filepath):
    result = subprocess.run(['python', '/Users/yashwanthponugoti/Documents/major/Action_detection/main.py'], capture_output=True, text=True)
    processed_filename = os.path.join(app.config['PROCESSED_FOLDER'], "original.mp4")
    return processed_filename
def balltrack01(filepath):
    result = subprocess.run(['python', '/Users/yashwanthponugoti/Documents/major/Action_detection/maini.py'], capture_output=True, text=True)
    processed_filename = os.path.join(app.config['PROCESSED_FOLDER'], "original.jpg")
    return processed_filename

@app.route('/upload1', methods=['POST','GET'])
def upload_file1():
    if 'video' not in request.files:
        return redirect(request.url)
    file = request.files['video']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        if file.filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], "original.jpg")
            file.save(filepath)
            processed_filepath = balltrack12(filepath)
            return redirect(url_for('download_file', filename=os.path.basename(processed_filepath)))
        else :
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], "original.mp4")
            file.save(filepath)
            processed_filepath = balltrack1(filepath)
            return render_template('volley2.html', flag = True)
    
def balltrack1(filepath):
    result = subprocess.run(['python', '/Users/yashwanthponugoti/Documents/major/Player_detection/main.py'], capture_output=True, text=True)
    processed_filename = os.path.join(app.config['PROCESSED_FOLDER'], "original.mp4")
    return processed_filename
def balltrack12(filepath):
    result = subprocess.run(['python', '/Users/yashwanthponugoti/Documents/major/Player_detection/maini.py'], capture_output=True, text=True)
    processed_filename = os.path.join(app.config['PROCESSED_FOLDER'], "original.jpg")
    return processed_filename

@app.route('/upload2', methods=['POST','GET'])
def upload_file2():
    if 'video' not in request.files:
        return redirect(request.url)
    file = request.files['video']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        if file.filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], "original.jpg")
            file.save(filepath)
            processed_filepath = balltrack21(filepath)
            return redirect(url_for('download_file', filename=os.path.basename(processed_filepath)))
        else :
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], "original.mp4")
            file.save(filepath)
            processed_filepath = balltrack2(filepath)
            return render_template('volley2.html', flag = True)
    
def balltrack2(filepath):
    result = subprocess.run(['python', '/Users/yashwanthponugoti/Documents/major/ball_track/detect.py'], capture_output=True, text=True)
    processed_filename = os.path.join(app.config['PROCESSED_FOLDER'], "original.mp4")
    return processed_filename
def balltrack21(filepath):
    result = subprocess.run(['python', '/Users/yashwanthponugoti/Documents/major/ball_track/detecti.py'], capture_output=True, text=True)
    processed_filename = os.path.join(app.config['PROCESSED_FOLDER'], "original.jpg")
    return processed_filename

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory("/Users/yashwanthponugoti/Documents/major/static/images", filename)

# @app.route('/')
# def index():
#     return render_template('test.html')

@app.route('/video/<path:filename>')
def video(filename):
    return send_from_directory('static/videos', filename)

if __name__ == '__main__':
    app.run(debug=True)