from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/home/ec2-user/uploads' 

@app.route('/upload/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No se encontro el archivo en la solicitud', 400
    file = request.files['file']
    if file.filename == '':
        return 'No se selecciono ningún archivo',400
    file.save(os.path.join(UPLOAD_FOLDER,file.filename))
    print('EXITO')
    return "Archivo de Usuario Subido Exitosamente", 200

@app.route('/usuario/',methods=['POST'])
def update_usuario():
    if 'file' not in request.files:
        return 'No se encontro el archivo en la solicitud', 400
    file = request.files['file']
    if file.filename == '':
        return 'No se selecciono ningún archivo',400
    file.save(os.path.join(UPLOAD_FOLDER,file.filename))
    print('EXITO')
    return 'Archivo de Usuario Subido Exitosamente',200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)