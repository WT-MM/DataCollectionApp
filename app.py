from flask import Flask, render_template, flash, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gestures')
def gestures():
    return render_template('gestures.html')

@app.errorhandler(404) 
def errorPage(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

