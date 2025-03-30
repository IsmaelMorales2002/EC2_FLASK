from flask import Flask,request,jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = '/home/ec2-user'
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

@app.route('/uploads',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'Error': 'No file part'}),400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'Error': 'No selected file'}),400
    
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER,filename))
    return jsonify({'Message': 'File uploaded','path':f"/files/{filename}"}),200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)