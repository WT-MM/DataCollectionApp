import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from modules.gestures import *
import pygsheets
import ast

app = Flask(__name__)

gc = pygsheets.authorize(service_account_env_var='GDRIVE_CREDS')
sh = gc.open('Data Collection App')
wks = sh[0]

thedata = []

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gestures')
def gestures():
    return render_template('gestures.html')

@app.route('/gestures/save', methods=['POST', 'GET'])
def saveGestures():
    if request.method == 'GET':
        return render_template('404.html'), 404
    data=ast.literal_eval(request.form['points'][1:-1])
    logged = getRelPositions(data)
    formatted = str(logged)[1:-1]+ "," + request.form['label']
    thedata.append([formatted])
    return jsonify()

@app.route('/gestures/savedata', methods=['POST', 'GET'])
def sendToSheet():
    global thedata
    if request.method == 'GET':
        return render_template('404.html'), 404
    if thedata:
        print(thedata)
        wks.append_table(values=thedata,start="A1",end="W1")
        thedata = []
        return jsonify(success=True)
    
    return jsonify(success=False)

@app.route('/gestures/help')
def gestureshelp():
    return render_template('gestureinfo.html')
        

@app.errorhandler(404) 
def errorPage(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

